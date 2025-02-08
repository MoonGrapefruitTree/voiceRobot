import sys
sys.path.append("./User")
sys.path.append("./ASR")
sys.path.append("./TTS")
sys.path.append("./LLM")
from Input import Recorder
from AutoSpeechRecognition import AutoSpeechRecognizer
from Think import ThinkerGLM
from TextToSpeech import FastTextConverter,TextConverter
from Output import Speaker


import keyboard

print("初始化...")
user_input_file_path = r"D:\daily_work\voiceRobot\Temp\User\temp.wav"
recorder = Recorder(user_input_file_path)
recognizer = AutoSpeechRecognizer()
thinker = ThinkerGLM()
converter = TextConverter()
fastConverter = FastTextConverter()
speaker = Speaker()

# 退出循环标志
recording_continue = True
print("初始化完成")

# 按下空格开始录音
def on_space_key_press_event(e):
    if not recorder.recording:
        recorder.start_recording()
# 松开空格开始回答
def on_space_key_release_event(e):
    if recorder.recording:
        recorder.stop_recording()
        input = recognizer.recognize(user_input_file_path)
        outer = thinker.think(input)
        robot_voice = fastConverter.convert([outer])
        speaker.speak(robot_voice)


keyboard.on_press_key('space', on_space_key_press_event)
keyboard.on_release_key('space', on_space_key_release_event)





print("按住空格键录音，松开以停止，esc退出")
# while recording_continue :  
#     pass
keyboard.wait('esc')