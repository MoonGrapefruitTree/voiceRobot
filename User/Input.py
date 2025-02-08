import pyaudio
import wave


class Recorder:
    def __init__(self, filename, channels=2, rate=44100, chunk=1024, format = pyaudio.paInt16):
        self.filename = filename
        self.channels = channels
        self.rate = rate
        self.chunk = chunk
        self.format = format

        self.frames = []
        
        self.recording = False
        
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk,
                    stream_callback=self.callback)
        
    def callback(self, in_data, frame_count, time_info, status):
        if self.recording:
            self.frames.append(in_data)
        return in_data, pyaudio.paContinue
    
    def start_recording(self):
        print("开始录音... (按住空格键录音，松开以停止)")
        self.recording = True
        self.frames = [] 

    def stop_recording(self):
    
        self.recording = False
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        print(f"录音已停止并保存为 {self.filename}")
        

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()