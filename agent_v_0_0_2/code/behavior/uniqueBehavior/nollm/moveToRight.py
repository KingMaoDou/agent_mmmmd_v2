#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： hit-itnlp-wzj
# datetime： 2024/5/21 19:46 
# FileName： move.py
# software： PyCharm

#Agent Memory读写
from agent_v_0_0_2.code.behavior.unifyBehavior.nollm.remember import Remember
from agent_v_0_0_2.code.behavior.unifyBehavior.nollm.memorize import Memorize

#tools:处理config；调用大模型
from agent_v_0_0_2.code.tools import read_agent_config, llm, extract


class MoveToRight(object):
    def __init__(self,agent,environment,movetoright_prompt_path=''):

        super(MoveToRight, self).__init__()

        self.agent = agent
        self.type = '具体行动结果'

        self.prompt_path = movetoright_prompt_path

        self.remember = Remember(self.agent)
        self.memorize = Memorize(self.agent)

        ##begin特有行动编码区域##
        self.environment = environment
        ##end特有行动编码区域##

    def uniqueBehavior(self):

        c = read_agent_config(self.agent.agent_config_path)
        role = c['角色']
        name = role['姓名']

        #注1:特有行动必须对环境(广义的环境，包括Agent自身)有输出(参考"智能体-环境"循环)。
        ##begin特有行动编码区域##
        # self.environment.UI = '史蒂夫在爱丽丝的左侧。并且史蒂夫与爱丽丝相聚四米。'
        self.environment.UI = input('[DEBUG-MODEL]请输入更新后的环境:')
        print('**********BEGIN:环境描述**********')
        print(self.environment.UI)
        print('**********END:环境描述**********')
        ##end特有行动编码区域##


        #注1.1:把对智能体的输出暂时写在这里。
        ##begin特有行动编码区域##
        self.environment.sentInfo(src=name,tar_list=[name],content=input('[DEBUG-MODEL]请输入观察结果:'))
        ##end特有行动编码区域##


        #注3:特有行动结果必须形成一次记忆记录。
        ##begin特有行动编码区域##
        desc = '我向右移动了一米。'
        self.memorize.memorize(self.type,desc)
        ##end特有行动编码区域##