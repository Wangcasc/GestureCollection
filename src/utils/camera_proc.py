
import cv2
import time
import numpy as np
import multiprocessing
import threading
from PyQt5.QtCore import QThread, pyqtSignal,QMutex
import concurrent.futures as futures
import os

import utils.mvsdk as mvsdk

def setROI(hCamera,iWidth,iHeight,iHOffsetFOV,iVOffsetFOV):
    sRoiReslution = mvsdk.tSdkImageResolution()  # 实例化变量
    sRoiReslution.iIndex = 0xff  # 赋值
    sRoiReslution.iWidth = iWidth
    sRoiReslution.iWidthFOV = iWidth
    sRoiReslution.iHeight = iHeight
    sRoiReslution.iHeightFOV = iHeight
    sRoiReslution.iHOffsetFOV = iHOffsetFOV
    sRoiReslution.iVOffsetFOV = iVOffsetFOV
    mvsdk.CameraSetImageResolution(hCamera, sRoiReslution)
        
class camera_task:
    def __init__(self,DevInfo,NS,record_save,frameRates):
        self.DevInfo = DevInfo
        self.NS = NS
        self.record_save = record_save
        self.frameRates = frameRates
        #缓存
        self.imgs_buffer = []
        self.executor = futures.ThreadPoolExecutor(max_workers=1)

        # 打开相机
        self.hCamera = 0
        try:
            self.hCamera = mvsdk.CameraInit(DevInfo, -1, -1)
        except mvsdk.CameraException as e:
            print("CameraInit Failed({}): {}".format(e.error_code, e.message) )
            return
        
        # 获取相机特性描述
        cap = mvsdk.CameraGetCapability(self.hCamera)
        # 判断是黑白相机还是彩色相机
        monoCamera = (cap.sIspCapacity.bMonoSensor != 0)
        # 黑白相机让ISP直接输出MONO数据，而不是扩展成R=G=B的24位灰度
        if monoCamera:
            mvsdk.CameraSetIspOutFormat(self.hCamera, mvsdk.CAMERA_MEDIA_TYPE_MONO8)
        else:
            mvsdk.CameraSetIspOutFormat(self.hCamera, mvsdk.CAMERA_MEDIA_TYPE_BGR8)


        if self.DevInfo.GetSn() == "044011420148":  # 041182220233  044062320120
            setROI(self.hCamera, 800, 800, 430, 112)
        else:
            setROI(self.hCamera, 800, 800, 240, 112)
        # 相机模式切换成连续采集
        mvsdk.CameraSetTriggerMode(self.hCamera, 2)#2是外部触发
        # 手动曝光，曝光时间30ms
        mvsdk.CameraSetAeState(self.hCamera, 0)#0是手动曝光
        mvsdk.CameraSetExposureTime(self.hCamera,8 * 1000)#8是曝光时间（ms）
        # if self.DevInfo.GetSn()=="044011420148":
        #     mvsdk.CameraSetGain(self.hCamera, iRGain=109, iGGain=100, iBGain=114)
        # else:
        #     mvsdk.CameraSetGain(self.hCamera, iRGain=140, iGGain=114, iBGain=100)
        # 让SDK内部取图线程开始工作
        mvsdk.CameraPlay(self.hCamera)
        # 计算RGB buffer所需的大小，这里直接按照相机的最大分辨率来分配
        FrameBufferSize = cap.sResolutionRange.iWidthMax * cap.sResolutionRange.iHeightMax * (1 if monoCamera else 3)
        # 分配RGB buffer，用来存放ISP输出的图像
        # 备注：从相机传输到PC端的是RAW数据，在PC端通过软件ISP转为RGB数据（如果是黑白相机就不需要转换格式，但是ISP还有其它处理，所以也需要分配这个buffer）
        self.pFrameBuffer = mvsdk.CameraAlignMalloc(FrameBufferSize, 16)



    def save_video(self):
        if self.DevInfo.GetSn()=="044011420148":   #041182220233  044062320120
            camera = "RGB_1"
        elif self.DevInfo.GetSn()=="044030620196":  #044062320105   042092320674
            camera = "RGB_2"
        elif self.DevInfo.GetSn()=="044062320120":
            camera = "RGB_3"
        elif self.DevInfo.GetSn()=="044062320129":
            camera ="RGB_4"
        elif self.DevInfo.GetSn()=="044030620195":
            camera ="RGB_5"
        elif self.DevInfo.GetSn()=="043051920299":
            camera="inf"
        elif self.DevInfo.GetSn()=="044062320137":
            camera ="RGB_6"
        elif self.DevInfo.GetSn()=="044062320105":
            camera="RGB_7"


        path=self.NS.save_id_path
        sample_camera_path = os.path.join(path, camera)
        if not os.path.exists(sample_camera_path):
            os.mkdir(sample_camera_path)

        for index, img in enumerate(self.imgs_buffer):
            img_path = os.path.join(sample_camera_path, '%03d.jpg' % (index + 1))
            # cv2.imshow("{}".format(camera), img)
            # cv2.waitKey(1)
            cv2.imwrite(img_path, img)


        self.imgs_buffer = []

        print('{}采集完成'.format(camera))
        # time.sleep(0.1)

    def run(self,pipe,stop_event):
        num_frames = 0
        start_time = time.time()
        while not stop_event.is_set():
            try:
                pRawData, FrameHead = mvsdk.CameraGetImageBuffer(self.hCamera, 200)
                mvsdk.CameraImageProcess(self.hCamera, pRawData, self.pFrameBuffer, FrameHead)
                mvsdk.CameraReleaseImageBuffer(self.hCamera, pRawData)
                # 计算帧率
                num_frames += 1
                elapsed_time = time.time() - start_time
                if elapsed_time > 0:
                    fps = num_frames / elapsed_time
                else:
                    fps = 0
                if num_frames>300:
                    num_frames=0
                    start_time=time.time()
                # print("fps:",fps)
                # print(self.NS)
                # print(self.record_save)
                # 此时图片已经存储在pFrameBuffer中，对于彩色相机pFrameBuffer=RGB数据，黑白相机pFrameBuffer=8位灰度数据
                # 把pFrameBuffer转换成opencv的图像格式以进行后续算法处理
                frame_data = (mvsdk.c_ubyte * FrameHead.uBytes).from_address(self.pFrameBuffer)
                frame = np.frombuffer(frame_data, dtype=np.uint8)
                frame = frame.reshape((FrameHead.iHeight, FrameHead.iWidth, 1 if FrameHead.uiMediaType == mvsdk.CAMERA_MEDIA_TYPE_MONO8 else 3) )

                if self.DevInfo.GetSn() == "044011420148":
                    frame=cv2.flip(frame,0)
                    print(num_frames)
                elif self.DevInfo.GetSn() == "044030620196":  # 044062320105   042092320674
                    frame=cv2.flip(frame,0)
                elif self.DevInfo.GetSn() == "044062320120":
                    frame=cv2.flip(frame,1)
                elif self.DevInfo.GetSn() == "044062320129":
                    frame=cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
                    frame=cv2.flip(frame,1)
                elif self.DevInfo.GetSn() == "044030620195":
                    frame=cv2.rotate(frame,cv2.ROTATE_90_COUNTERCLOCKWISE)
                    frame=cv2.flip(frame,1)
                elif self.DevInfo.GetSn() == "044062320137":
                    frame=cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
                    frame=cv2.flip(frame,1)
                elif self.DevInfo.GetSn() == "044062320105":
                    frame=cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
                    frame=cv2.flip(frame,1)
                elif self.DevInfo.GetSn() == "044030620196":
                    pass

                # frame = cv2.resize(frame, (640,480), interpolation = cv2.INTER_LINEAR)
                if num_frames % 10 == 0:
                    frame_show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame_show = cv2.resize(frame_show, (160,160))
                    pipe.send(frame_show)
                    self.frameRates[self.DevInfo.GetSn()] = fps

                if self.record_save[self.DevInfo.GetSn()]==1:
                    self.imgs_buffer.append(frame)
                    if len(self.imgs_buffer) == 1:
                        start_time2 = time.time()
                    # print(len(self.imgs_buffer))
                    if len(self.imgs_buffer) == self.NS.sample_frame:
                        end_time2 = time.time()
                        print("采集完成，耗时：",end_time2-start_time2)
                        self.executor.submit(self.save_video)

                        self.record_save[self.DevInfo.GetSn()] = 0

            except mvsdk.CameraException as e:
                if e.error_code != mvsdk.CAMERA_STATUS_TIME_OUT:
                    print("CameraGetImageBuffer failed({}): {}".format(e.error_code, e.message))


        mvsdk.CameraStopRecord(self.hCamera)
        # 关闭相机
        mvsdk.CameraUnInit(self.hCamera)
        # 释放帧缓存
        mvsdk.CameraAlignFree(self.pFrameBuffer)
        print("Camera stopped")
        
# def run_camera(index,pipe,stop_event):
#     camera = camera_task(index)
#     camera.run(pipe,stop_event)
    
def run_camera(devinfo,pipe,stop_event,NS,record_save,frameRates):
    camera = camera_task(devinfo,NS,record_save,frameRates)
    camera.run(pipe,stop_event) 
    
    
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=run_camera, args=(0,))
    p2 = multiprocessing.Process(target=run_camera, args=(1,))
    
    # p1 = threading.Thread(target=run_camera, args=(0,))
    # p2 = threading.Thread(target=run_camera, args=(1,))    

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()