#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： hit-itnlp-wzj
# datetime： 2024/5/21 20:49 
# FileName： decisionEvaluation.py
# software： PyCharm

#Agent Memory读写
from agent_v_0_0_2.code.behavior.unifyBehavior.nollm.remember import Remember
from agent_v_0_0_2.code.behavior.unifyBehavior.nollm.memorize import Memorize

#tools:处理config；调用大模型
from agent_v_0_0_2.code.tools import read_agent_config, llm, extract, llm_claude


class DecisionEvaluation(object):
    def __init__(self,agent,decisionevaluation_prompt_path=r'G:\毕业设计\pythonProject\agent_v1\agent_v_0_0_2\prompt\unifyBehavior\decisionevaluation.txt'):

        super(DecisionEvaluation, self).__init__()

        self.agent = agent
        self.type = '决策实施计划状态评估'

        self.prompt_path = decisionevaluation_prompt_path

        self.remember = Remember(self.agent)
        self.memorize = Memorize(self.agent)

    def decisionEvaluation(self):

        instruct = self.remember.remember()

        with open(self.prompt_path,mode='r',encoding='utf-8') as file:
            prompt = file.read()


        instruct = instruct + prompt

        print('-----BEGIN-----')
        print(self.type)
        print(instruct)
        print('-----END-----')

        answer = llm(instruct)
        # answer = llm_claude(instruct)

        self.memorize.memorize(self.type,answer)

        return extract(answer, r'我认为最近一条决策实施计划的状态是：\[(.*?)\]')
