import requests
import json


with open(r'G:\毕业设计\pythonProject\agent_v1\agent_v_0_0_2\code\text.txt', mode='r', encoding='utf-8') as file:
    text = file.read()

url = "https://api.openai-proxy.org/anthropic/v1/messages"
headers = {
    'x-api-key': 'sk-sqPZa78uy27sIvpvlv6VyGc2dFTdt1uQ52jzhHxu2FOWQLvL',
    'anthropic-version': '2023-06-01',
    'content-type': 'application/json',
}
data = {
    "model": "claude-3-haiku-20240307",
    "max_tokens": 1024,
    "stream": False,
    "messages": [
        {"role": "user", "content": text}
    ]
}

response = requests.request("POST", url, headers=headers, data=json.dumps(data))

print(response.json()['content'][0]['text'])

import pdb
pdb.set_trace()