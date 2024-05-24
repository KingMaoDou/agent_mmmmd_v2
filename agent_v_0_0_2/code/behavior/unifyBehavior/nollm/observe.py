#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： hit-itnlp-wzj
# datetime： 2024/5/5 22:13 
# FileName： observe.py
# software： PyCharm

from agent_v_0_0_2.code.tools import read_agent_config
from agent_v_0_0_2.code.agent import Agent
from agent_v_0_0_2.code.environment import Environment
from agent_v_0_0_2.code.behavior.unifyBehavior.nollm.memorize import Memorize
class Observe(object):
    def __init__(self,agent,environment):
        super(Observe,self).__init__()
        self.agent = agent
        self.type = '观察'
        self.emt = environment
        self.memorize = Memorize(agent)

    def observe(self):
        c = read_agent_config(self.agent.agent_config_path)
        name = c['角色']['姓名']
        observation = self.emt.get_info(name)

        if observation.empty():
            result = '暂时没有观察到新的信息。'
        else:
            result = ''
            while not observation.empty():
                result = result + observation.get() + '\n'


        print(result)
        self.memorize.memorize(type=self.type, record=result)


if __name__ == '__main__':
    a = Agent()
    e = Environment(agent_list=[a])
    o = Observe(a,e)
    o.observe()



