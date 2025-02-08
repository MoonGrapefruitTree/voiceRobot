from pydub import AudioSegment
from pydub.playback import play
import torchaudio

class Speaker:
    def __init__(self):
        pass

    def speak(self,file_path):
        # 加载音频文件
        waveform, sample_rate = torchaudio.load(file_path)

        # 将PyTorch张量转换为numpy数组
        waveform_np = waveform.numpy().T  # 注意：需要转置以匹配pydub期望的格式

        # 创建AudioSegment对象
        audio_segment = AudioSegment(
                waveform_np.tobytes(), 
                frame_rate=sample_rate,
                sample_width=waveform_np.dtype.itemsize,  # 样本宽度（字节）
                channels=waveform_np.shape[1]  # 声道数
            )

        # 播放音频
        play(audio_segment)