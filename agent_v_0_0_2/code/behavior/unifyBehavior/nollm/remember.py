#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： hit-itnlp-wzj
# datetime： 2024/5/6 11:59 
# FileName： remember.py
# software： PyCharm
from agent_v_0_0_2.code.tools import read_agent_config

class Remember(object):
    def __init__(self,agent):
        super(Remember, self).__init__()
        self.agent = agent

    def remember(self,context=25):
        c = read_agent_config(self.agent.agent_config_path)
        memory = c['记忆']

        recent_memory = memory.tail(context)

        #begin:填充memory#
        temp_memory = '\n'
        for index,row in recent_memory.iterrows():
            temp_memory = temp_memory + f'''{row['时间点']}, [{row['类型']}], {row['内容']}''' + '\n'
        #end:填充memory#

        QA_prompt = self.agent.init_prompt.replace('[MEMORY]', temp_memory)

        return QA_prompt