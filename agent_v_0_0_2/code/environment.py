#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： hit-itnlp-wzj
# datetime： 2024/5/5 22:48 
# FileName： envir.py
# software： PyCharm

import json
from queue import Queue
from agent_v_0_0_2.code.tools import read_agent_config

class Environment(object):
    def __init__(self,environment_path='',agent_list=[]):
        super(Environment, self).__init__()
        self.emt_path = environment_path
        self.UI = '史蒂夫在爱丽丝的左侧。并且史蒂夫与爱丽丝相聚五米。'
        self.agent_list = agent_list
        self.agent_info_queue = {}
        self.init_info_queue()

        self.fun()

    def init_info_queue(self):

        for i in self.agent_list:
            c = read_agent_config(i.agent_config_path)
            self.agent_info_queue[c['角色']['姓名']] = Queue()

    def get_info(self,agent_name):

        return self.agent_info_queue[agent_name]

    def fun(self):
        pass
        # self.agent_info_queue['史蒂夫'].put('爱丽丝在我的右侧两米处。')
        # self.agent_info_queue['史蒂夫'].put('爱丽丝似乎不开心')

    def sentInfo(self,src,tar_list,content):

        for tar in tar_list:
            self.agent_info_queue[tar].put(content)

if __name__ == '__main__':


    import pdb
    pdb.set_trace()