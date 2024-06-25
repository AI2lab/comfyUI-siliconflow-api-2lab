
import os
import json
from openai import OpenAI

from .constants import get_project_category, get_project_name, project_root

configFile = os.path.join(project_root, 'config.json')
with open(configFile, 'r') as file:
    data = file.read()
json_data = json.loads(data)
key = json_data["API_KEY"]

NODE_CATEGORY = get_project_category("llm")

class FreeChat:
    NAME = get_project_name('FreeChat')
    CATEGORY = NODE_CATEGORY
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "doWork"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True}),
                 "model": (["Qwen/Qwen2-7B-Instruct",
                            "Qwen/Qwen2-1.5B-Instruct",
                            "Qwen/Qwen1.5-7B-Chat",
                            "THUDM/glm-4-9b-chat",
                            "THUDM/chatglm3-6b",
                            "01-ai/Yi-1.5-9B-Chat-16K",
                            "01-ai/Yi-1.5-6B-Chat"
                            ],{"default": "Qwen/Qwen2-7B-Instruct"}),
            },
        }

    def doWork(self,  prompt, model):
        client = OpenAI(api_key=key, base_url="https://api.siliconflow.cn/v1")

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt},
            ],
            stream=False
        )

        print(response.choices[0].message.content)
        return {"result": (response.choices[0].message.content,)}

class PaidChat:
    NAME = get_project_name('PaidChat')
    CATEGORY = NODE_CATEGORY
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "doWork"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True}),
                 "model": (["Qwen/Qwen2-72B-Instruct",
                            "Qwen/Qwen2-57B-A14B-Instruct",
                            "Qwen/Qwen1.5-110B-Chat",
                            "Qwen/Qwen1.5-32B-Chat",
                            "Qwen/Qwen1.5-14B-Chat",
                            "deepseek-ai/DeepSeek-Coder-V2-Instruct",
                            "deepseek-ai/DeepSeek-V2-Chat",
                            "deepseek-ai/deepseek-llm-67b-chat",
                            "01-ai/Yi-1.5-34B-Chat-16K"
                            ],{"default": "Qwen/Qwen2-72B-Instruct"}),
            },
        }

    def doWork(self,  prompt, model):
        client = OpenAI(api_key=key, base_url="https://api.siliconflow.cn/v1")

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt},
            ],
            stream=False
        )

        print(response.choices[0].message.content)
        return {"result": (response.choices[0].message.content,)}
