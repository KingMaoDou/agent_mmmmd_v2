#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： hit-itnlp-wzj
# datetime： 2024/5/22 14:39 
# FileName： startNewDialogue.py
# software： PyCharm

#Agent Memory读写
from agent_v_0_0_2.code.behavior.unifyBehavior.nollm.remember import Remember
from agent_v_0_0_2.code.behavior.unifyBehavior.nollm.memorize import Memorize

#tools:处理config；调用大模型
from agent_v_0_0_2.code.tools import read_agent_config, llm, extract, llm_claude
import re

class StartNewDialogue(object):
    def __init__(self,agent,environment,startNewDialogue_prompt_path=r'G:\毕业设计\pythonProject\agent_v1\agent_v_0_0_2\prompt\uniqueBehavior\startnewdialogue.txt'):

        super(StartNewDialogue, self).__init__()

        self.agent = agent
        self.type = '具体行动结果'

        self.prompt_path = startNewDialogue_prompt_path

        self.remember = Remember(self.agent)
        self.memorize = Memorize(self.agent)

        ##begin特有行动编码区域##
        self.environment = environment
        ##end特有行动编码区域##

    def extract_dialogue_info(self,dialogue_string):
        dialogue_initiator_pattern = r'对话发起人：\[([^\]]+)\]'
        target_names_pattern = r'姓名：([^\]]+)'
        dialogue_content_pattern = r'对话内容：\[([^\]]+)\]'

        dialogue_initiators = re.findall(dialogue_initiator_pattern, dialogue_string)
        target_names = re.findall(target_names_pattern, dialogue_string)
        dialogue_contents = re.findall(dialogue_content_pattern, dialogue_string)

        return dialogue_initiators, target_names, dialogue_contents

    def uniqueBehavior(self):

        instruct = self.remember.remember()

        with open(self.prompt_path,mode='r',encoding='utf-8') as file:
            prompt = file.read()

        #end获取属性
        instruct = instruct + prompt

        print('-----BEGIN-----')
        print(self.type)
        print(instruct)
        print('-----END-----')


        # answer = llm_claude(instruct)
        answer = llm(instruct,model='gpt-4o')

        dialogue = self.extract_dialogue_info(answer)
        # import pdb
        # pdb.set_trace()
        src = dialogue[0][0]
        tar_list = dialogue[1]
        content = dialogue[2][0]

        #注1:特有行动必须对环境(广义的环境，包括Agent自身)有输出(参考"智能体-环境"循环)。
        ##begin特有行动编码区域##
        self.environment.UI = src + '对' + ';'.join(tar_list) + '发起了一次新的对话。' + '对话内容是:' + '\n' + content
        print('**********BEGIN:环境描述**********')
        print(self.environment.UI)
        print('**********END:环境描述**********')
        ##end特有行动编码区域##


        #注1.1:把对智能体的输出暂时写在这里。
        ##begin特有行动编码区域##
        # self.environment.sentInfo(src=src,tar_list=tar_list,content= src + '对我发起了一次新的对话。' + '对话内容是:' + '\n' + content)
        ##end特有行动编码区域##


        #注3:特有行动结果必须形成一次记忆记录。
        ##begin特有行动编码区域##
        desc = '我对' + ';'.join(tar_list) + '发起了一次新的对话。' + '对话内容是:' + '\n' + content
        self.memorize.memorize(self.type,desc)
        ##end特有行动编码区域##
