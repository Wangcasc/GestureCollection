


# 华南理工大学
# 王熙来
# 开发时间：2025/3/17 16:52


import cv2
import numpy as np
import pyrealsense2 as rs
import time
import concurrent.futures as futures
import os

import pyzed.sl as sl
import cv2

class ZEDTask:
    def __init__(self,NS,record_save,frameRates):

        self.NS = NS # namespace
        self.record_save = record_save # record_save flag
        self.frameRates = frameRates # frameRates dict

        self.executor = futures.ThreadPoolExecutor(max_workers=1) # 储存线程

        self.zed = sl.Camera()

        init_parameters = sl.InitParameters()
        init_parameters.camera_resolution = sl.RESOLUTION.HD720  # 相机分辨率设置
        init_parameters.depth_mode = sl.DEPTH_MODE.NEURAL
        init_parameters.camera_fps = 60
        init_parameters.coordinate_units = sl.UNIT.METER
        init_parameters.depth_minimum_distance = 0.15  # Set the minimum depth perception distance to 15cm
        init_parameters.depth_maximum_distance = 7  # Set the maximum depth perception distance to 40m
        # parse_args(init_parameters)

        # self.zed.set_camera_settings(sl.VIDEO_SETTINGS.EXPOSURE, 50)
        # Set white balance to 4600K
        # self.zed.set_camera_settings(sl.VIDEO_SETTINGS.WHITE_BALANCE, 4600)
        # Reset to auto exposure
        # self.zed.set_camera_settings(sl.VIDEO_SETTINGS.EXPOSURE, -1)


        # Open the camera
        returned_state = self.zed.open(init_parameters)
        if returned_state != sl.ERROR_CODE.SUCCESS:
            print("Camera Open", returned_state, "Exit program.")
            exit()
        else:
            print("Camera Opened Successfully")

        resolution = self.zed.get_camera_information().camera_configuration.resolution

        # Create a Mat to store images
        self.zed_image = sl.Mat(resolution.width, resolution.height, sl.MAT_TYPE.U8_C4, sl.MEM.CPU)
        self.zed_depth_image = sl.Mat(resolution.width, resolution.height, sl.MAT_TYPE.U8_C4, sl.MEM.CPU)




        self.recording = 0
        self.save = 0

    def grab(self):
        try:
            returned_state = self.zed.grab()
            if returned_state == sl.ERROR_CODE.SUCCESS:
                # Retrieve left image
                self.zed.retrieve_image(self.zed_image, sl.VIEW.SIDE_BY_SIDE)  # SIDE_BY_SIDE, LEFT, RIGHT
                self.zed.retrieve_image(self.zed_depth_image, sl.VIEW.DEPTH)

                cvImage = self.zed_image.get_data()
                cvDepthImage = self.zed_depth_image.get_data()

                # cvImage = cv2.resize(cvImage, (0, 0), fx=0.5, fy=0.5)
                # cvDepthImage = cv2.resize(cvDepthImage, (0, 0), fx=0.5, fy=0.5)

                # cv2.imshow("rgb", cvImage)
                # cv2.imshow("depth", cvDepthImage)

            return cvImage,cvDepthImage,True

        except Exception as e:
            # print(e)
            return None, None,None,None,False


    def save_video(self):

        path=self.NS.save_id_path
        sample_camera_path_1 = os.path.join(path, "ZED_RGB")
        sample_camera_path_2 = os.path.join(path, "ZED_Depth")
        if not os.path.exists(sample_camera_path_1):
            os.mkdir(sample_camera_path_1)
        if not os.path.exists(sample_camera_path_2):
            os.mkdir(sample_camera_path_2)

        for index, img in enumerate(self.RGB_buffer):
            if index<120:
                img_path = os.path.join(sample_camera_path_1, '%03d.jpg' % (index + 1))
                img_path2 = os.path.join(sample_camera_path_2, '%03d.jpg' % (index + 1))
                # cv2.imshow("{}".format(camera), img)
                # cv2.waitKey(1)
                # print("img_path:",img_path)

                cv2.imwrite(img_path, img)
                cv2.imwrite(img_path2, self.Depth_buffer[index])


        self.RGB_buffer = []
        self.Depth_buffer = []

        print('zed采集完成')
        self.NS.ZED_saved = True

    def run(self,pipe,pipe2,stop_event):
        num=0
        self.RGB_buffer = []
        self.Depth_buffer = []
        # self.PCD_buffer = []
        num_frames = 0
        start_time = time.time()

        # 相机分辨率为：
        print("Camera Resolution:",self.zed.get_camera_information().camera_configuration.resolution.width,
              self.zed.get_camera_information().camera_configuration.resolution.height)
        # 相机帧率为：
        print("Camera FPS:",self.zed.get_camera_information())

        while not stop_event.is_set():
            try:
                # print(num_frames)

                color_image,depth_image ,ret= self.grab()

                # 都上下翻转一下
                color_image = cv2.flip(color_image, 0)
                depth_image = cv2.flip(depth_image, 0)

                # color_image是

                if ret:
                    # color_image = cv2.flip(color_image, 1)
                    # depth_image = cv2.flip(depth_image, 1)
                    # self.signal_changeFrame_RGB.emit([color_image, self.win.ui.label_realsense_RGB])
                    # self.signal_changeFrame_Depth.emit([depth_image, self.win.ui.label_realsense_Depth])

                    # 计算帧率
                    num_frames += 1
                    elapsed_time = time.time() - start_time
                    if elapsed_time > 0:
                        fps = num_frames / elapsed_time
                    else:
                        fps = 0
                    if num_frames>60:
                        num_frames=0
                        start_time=time.time()

                    # print("fps:",fps)
                    # print(num_frames)

                    if num_frames % 2 == 0:


                        frame_show = cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB)
                        frame_show = cv2.resize(frame_show, (320,160))
                        pipe.send(frame_show)

                        frame_show_2=cv2.cvtColor(depth_image, cv2.COLOR_BGR2RGB)
                        frame_show_2= cv2.resize(frame_show_2, (160,160))
                        pipe2.send(frame_show_2)
                        self.frameRates["ZED"] = fps
                        # cv2.imshow("depth",frame_show_2)
                        # cv2.imshow("stereo",frame_show)
                        # cv2.waitKey(1)
                        # print("fps:", fps)

                    #
                    # print(color_image.shape)
                    # 丢掉arpha通道
                    color_image = color_image[:, :, :3]
                    # 720, 2560 是两个720,1280的图片，中心裁剪成两个720,800
                    color_image1 = color_image[:, 240:1040, :]
                    color_image2 = color_image[:, 1280 + 240:1280 + 1040, :]
                    color_image = np.concatenate((color_image1, color_image2), axis=1)

                    depth_image=depth_image[:, :, :3]
                    depth_image1 = depth_image[:, 240:1040, :]

                    if self.record_save["ZED"] == 1:
                        num+=1

                        self.RGB_buffer.append(color_image.copy())
                        self.Depth_buffer.append(depth_image1.copy())
                        # self.Depth_Color_buffer.append(depth_color_image.copy())
                        # self.PCD_buffer.append(pcd.copy())

                        # self.signal_changenum.emit(int(num / self.win.sample_frame * 100))

                        if len(self.RGB_buffer) == 1:
                            start_time2 = time.time()
                        # print(len(self.imgs_buffer))
                        if len(self.RGB_buffer) == 120:
                            end_time2 = time.time()
                            print("采集完成，耗时：",end_time2-start_time2)
                            self.executor.submit(self.save_video)

                            self.record_save["ZED"] = 0

                    end=time.time()
                    # print("time:",1/(end - start))
            except Exception as e:
                print(e)


        print("ZED stop")
        # # 停止管道数据传输
        # self.pipeline.stop()
        #
        # # 获取深度传感器的设备
        # depth_sensor = self.pipeline.get_active_profile().get_device().first_depth_sensor()
        # # 关闭深度传感器
        # depth_sensor.stop()




def runZED(pipe,pipe2,stop_event,NS,record_save,frameRates):
    task = ZEDTask(NS,record_save,frameRates)
    task.run(pipe,pipe2,stop_event)