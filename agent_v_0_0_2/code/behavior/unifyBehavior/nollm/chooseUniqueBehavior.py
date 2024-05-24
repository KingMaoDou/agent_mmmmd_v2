#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： hit-itnlp-wzj
# datetime： 2024/5/21 20:16 
# FileName： chooseUniqueBehavior.py
# software： PyCharm
from agent_v_0_0_2.code.behavior.uniqueBehavior.nollm.moveToRight import MoveToRight
from agent_v_0_0_2.code.behavior.uniqueBehavior.startNewDialogue import StartNewDialogue
from agent_v_0_0_2.code.behavior.unifyBehavior.nollm.wait import Wait
from agent_v_0_0_2.code.behavior.uniqueBehavior.responseDialogue import ResponseDialogue


class ChooseUniqueBehavior(object):
    def __init__(self,agent, environment, SBNAME):
        super(ChooseUniqueBehavior,self).__init__()
        self.UNIQUE_BEHAVIOR_LIST = ['向右移动', '发起新的对话', '原地等待', '回复正在进行的对话']
        self.agent = agent
        self.environment = environment
        self.SBNAME = SBNAME


    def chooseUniqueBehavior(self):



        if self.SBNAME not in self.UNIQUE_BEHAVIOR_LIST:
            print('不支持该具体行动，大模型的输出报错了！')
            exit(-1)
        else:
            if '向右移动' == self.SBNAME:
                return MoveToRight(self.agent, self.environment)
            elif '发起新的对话' == self.SBNAME:
                return StartNewDialogue(self.agent, self.environment)
            elif '原地等待' == self.SBNAME:
                return Wait(self.agent, self.environment)
            elif '回复正在进行的对话' == self.SBNAME:
                return ResponseDialogue(self.agent, self.environment)
