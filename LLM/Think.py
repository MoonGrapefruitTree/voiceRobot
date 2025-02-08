from transformers import AutoModelForCausalLM, AutoTokenizer
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() 
local_llm_model_path = os.environ.get('LOCAL_LLM_MODEL_PATH')
glm_api_key = local_llm_model_path = os.environ.get('GLM_API_KEY')
glm_base_url = local_llm_model_path = os.environ.get('GLM_BASE_URL')

class ThinkerLocal:
    def __init__(self,model_name_or_path=local_llm_model_path):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
        self.tokenizer.pad_token_id = self.tokenizer.eos_token_id
        self.model = AutoModelForCausalLM.from_pretrained(model_name_or_path,is_decoder=True)

    def think(self, input):
        # 对输入文本进行编码
        prompt = input
        input_ids = self.tokenizer(prompt, return_tensors="pt")

        # 生成模型的输出
        output = self.model.generate(**input_ids, max_length=50, num_return_sequences=1)
        output_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return output_text
    


class ThinkerGLM:
    def __init__(self):
        self.client = OpenAI(
                        api_key=glm_api_key,
                        base_url=glm_base_url,
                        )

    def think(self, input):
        completion = self.client.chat.completions.create(
                                                    model="glm-4-flash",
                                                    messages=[
                                                            {"role": "system", "content": "你叫图图，是一个陪伴机器人，请你有感情且简短的回答用户问题."},
                                                            {"role": "user", "content": input}
                                                              ]
                                                    )
        return completion.choices[0].message.content