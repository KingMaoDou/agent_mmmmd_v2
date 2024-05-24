#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： hit-itnlp-wzj
# datetime： 2024/5/6 9:59 
# FileName： tools.py
# software： PyCharm
import json
import pandas as pd
import openai
import re
import requests



openai.api_base = ''
openai.api_key = ''




def extract(text,pattern):

    # 使用findall函数提取出所有满足正则表达式的部分
    result = re.findall(pattern, text)

    return result


def llm_claude(instruct):

    url = ""
    headers = {
        'x-api-key': '',
        'anthropic-version': '2023-06-01',
        'content-type': 'application/json',
    }
    data = {
        "model": "claude-3-haiku-20240307",
        "max_tokens": 1024,
        "temperature": 0,
        "stream": False,
        "messages": [
            {"role": "user", "content": instruct}
        ]
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(data))

    LLM_answer = response.json()['content'][0]['text']

    return LLM_answer

def llm(instruct,model='gpt-3.5-turbo'):

    response = openai.ChatCompletion.create(
        model=model,
        # model="gpt-4o",
        temperature = 0,
        # model =  "claude-3-opus-20240229",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": instruct}
        ]
    )

    LLM_answer = response['choices'][0]['message']['content']

    return LLM_answer

def read_agent_config(config_path=r'G:\毕业设计\pythonProject\agent_v1\agent_v_0_0_2\config\agent\史蒂夫.txt'):

    with open(config_path, 'r', encoding='utf-8') as file:
        # 读取文件内容，将json转化为python的数据结构
        config_dict = json.load(file)[0]

    with open(config_dict['角色'], encoding='utf-8') as file:
        role = json.load(file)[0]

    with open(config_dict['行动'], encoding='utf-8') as file:
        behavior = list(json.load(file)[0].keys())

    with open(config_dict['合作方式'], encoding='utf-8') as file:
        cooperation = list(json.load(file)[0].keys())

    memory = pd.read_csv(config_dict['记忆'])

    return {'角色':role,'行动':behavior,'合作方式':cooperation,'记忆':memory}


if __name__ == '__main__':
    x = read_agent_config()
    print(x)