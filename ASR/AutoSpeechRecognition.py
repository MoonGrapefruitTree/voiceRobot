from funasr import AutoModel
from dotenv import load_dotenv
import os

load_dotenv() 
asr_model_path = os.environ.get('ASR_MODEL_PATH')


class AutoSpeechRecognizer:
    def __init__(self,model_name_or_path=asr_model_path):
        self.model = AutoModel(model=model_name_or_path,disable_update=True)

        
    def recognize(self,file_path):
        res = self.model.generate(input=file_path)
        text = res[0]["text"].replace(" ","")
        print(text)
        return text