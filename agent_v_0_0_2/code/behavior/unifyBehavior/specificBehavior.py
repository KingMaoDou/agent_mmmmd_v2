#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： hit-itnlp-wzj
# datetime： 2024/5/21 19:19 
# FileName： specificBehavior.py
# software： PyCharm


#Agent Memory读写
from agent_v_0_0_2.code.behavior.unifyBehavior.nollm.remember import Remember
from agent_v_0_0_2.code.behavior.unifyBehavior.nollm.memorize import Memorize

#tools:处理config；调用大模型
from agent_v_0_0_2.code.tools import read_agent_config, llm, extract, llm_claude


class SpecificBehavior(object):
    def __init__(self,agent,specificbehavior_prompt_path=r'G:\毕业设计\pythonProject\agent_v1\agent_v_0_0_2\prompt\unifyBehavior\specificbehavior.txt'):

        super(SpecificBehavior, self).__init__()

        self.agent = agent
        self.type = '具体行动'

        self.prompt_path = specificbehavior_prompt_path

        self.remember = Remember(self.agent)
        self.memorize = Memorize(self.agent)

    def specificBehavior(self):

        instruct = self.remember.remember()

        with open(self.prompt_path,mode='r',encoding='utf-8') as file:
            prompt = file.read()

        #begin获取行动
        c = read_agent_config(self.agent.agent_config_path)
        behavior = c['行动']

        temp_behavior = '\n'
        for value in behavior:
            temp_behavior = temp_behavior + f'%{value}%' + '\n'

        prompt = prompt.replace('[BEHAVIOR]',temp_behavior)
        #end获取行动


        instruct = instruct + prompt

        print('-----BEGIN-----')
        print(self.type)
        print(instruct)
        print('-----END-----')

        answer = llm(instruct,model='gpt-4o')
        # answer = llm_claude(instruct)

        self.memorize.memorize(self.type,answer)

        print(f'[DEBUG MODEL]具体活动选择--格式检查:{answer}')
        return extract(answer,r'我选择：\[(.*?)\]')
        # return extract(answer,r'我选择：\[(.*?)\]')