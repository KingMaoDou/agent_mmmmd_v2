#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： hit-itnlp-wzj
# datetime： 2024/5/6 11:29 
# FileName： memorize.py.py
# software： PyCharm
from agent_v_0_0_2.code.tools import read_agent_config
from datetime import datetime
import json
class Memorize(object):
    def __init__(self,agent):
        super(Memorize, self).__init__()
        self.agent = agent

    def memorize(self,type,record):
        c = read_agent_config(self.agent.agent_config_path)
        memory = c['记忆']

        timestamp = datetime.now()
        new_record = [timestamp,f'[{type}]',record]

        memory.loc[len(memory)] = new_record

        with open(self.agent.agent_config_path, 'r', encoding='utf-8') as file:
            # 读取文件内容，将json转化为python的数据结构
            config_dict = json.load(file)[0]

        memory.to_csv(config_dict['记忆'],index=None)

