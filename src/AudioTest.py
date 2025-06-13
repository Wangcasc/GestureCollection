import pyttsx3

enguine = pyttsx3.init("sapi5")
enguine.setProperty('rate', 150)  # Set the speech rate
enguine.setProperty('volume', 1)  # Set the volume (0.0 to 1.0)
voice_id = enguine.getProperty('voices')[0].id  # Get the first voice
enguine.setProperty('voice', voice_id)  # Set the voice

def speak(text):
    """
    Function to convert text to speech.
    :param text: The text to be spoken.
    """
    enguine.say(text)
    enguine.runAndWait()

def main():
    # 讲中文
    speak("你好，欢迎使用语音合成测试程序。")
    # 讲英文
    speak("Hello, welcome to the text-to-speech test program.")


if __name__ == "__main__":
    main()
    # 结束语音引擎
    enguine.stop()
    print("语音合成测试完成。")
