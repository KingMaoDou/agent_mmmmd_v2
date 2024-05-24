#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： hit-itnlp-wzj
# datetime： 2024/5/5 13:18 
# FileName： agent.py.py
# software： PyCharm

import pandas as pd
import json
from agent_v_0_0_2.code.tools import read_agent_config

class Agent(object):
    def __init__(self,agent_config_path=r'G:\毕业设计\pythonProject\agent_v1\agent_v_0_0_2\config\agent\史蒂夫.txt',base_prompt_path=r'G:\毕业设计\pythonProject\agent_v1\agent_v_0_0_2\prompt\base\agent_prompt.txt'):

        super(Agent,self).__init__()

        self.agent_config_path = agent_config_path
        self.base_prompt_path = base_prompt_path

        self.base_prompt = self.get_base_prompt(self.base_prompt_path)
        self.init_prompt = self.get_init_prompt(self.base_prompt,self.agent_config_path)

    def get_base_prompt(self,path):
        '''
        返回字符串类型的base_prompt。
        后续和LLM交互的prompt都是基于base_prompt设计的。
        :param path:
        :return:
        '''
        result = ''

        with open(path,mode='r',encoding='utf-8') as file:
            result = file.read()

        return result

    def get_init_prompt(self,base_prompt,path):
        '''
        填充属性、行动、合作方式、初始记忆
        :param base_prompt:
        :param path:
        :return:
        '''

        c = read_agent_config(path)
        role = c['角色']
        behavior = c['行动']
        cooperation = c['合作方式']
        memory = c['记忆']

        #begin:填充ROLE#
        temp_role = '\n'
        for key,value in role.items():
            temp_role = temp_role+f'[{key}]:{value}' + '\n'
        #end:填充ROLE#
        
        
        #begin:填充behavior#
        temp_behavior = '\n'
        for value in behavior:
            temp_behavior = temp_behavior + f'%{value}%' + '\n'
        #end:填充behavior#
        
        #begin:填充cooperation#
        temp_cooperation = '\n'
        for index,value in enumerate(cooperation):
            temp_cooperation = temp_cooperation + f'({index+1}, {value})' + '\n'
        #end:填充cooperation#
        
        # #begin:填充memory#
        # temp_memory = '\n'
        # for index,row in memory.iterrows():
        #     temp_memory = temp_memory + f'''{row['时间点']}, [{row['类型']}], {row['内容']}''' + '\n'
        # #end:填充memory#

        base_prompt = base_prompt.replace('[NAME]',role['姓名'])
        base_prompt = base_prompt.replace('[ROLE]',temp_role)
        base_prompt = base_prompt.replace('[BEHAVIOR]', temp_behavior)
        # base_prompt = base_prompt.replace('[MEMORY]', temp_memory)
        base_prompt = base_prompt.replace('[COOPERATION]', temp_cooperation)

        return base_prompt

    def life_cycle(self):
        self.observe()
        self.decide()

if __name__ == '__main__':

    a = Agent('../config/agent/史蒂夫.txt')
    pass

