#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： hit-itnlp-wzj
# datetime： 2024/5/6 11:15 
# FileName： main.py.py
# software： PyCharm
from agent_v_0_0_2.code.agent import Agent
from agent_v_0_0_2.code.environment import Environment
from agent_v_0_0_2.code.behavior.unifyBehavior.nollm.observe import Observe
from agent_v_0_0_2.code.behavior.unifyBehavior.nollm.remember import Remember
from agent_v_0_0_2.code.behavior.unifyBehavior.decide import Decide
from agent_v_0_0_2.code.behavior.unifyBehavior.getRelatedAttribute import GetRelatedAttribute
from agent_v_0_0_2.code.behavior.unifyBehavior.decisionPlan import DecisionPlan
from agent_v_0_0_2.code.behavior.unifyBehavior.getRelatedBehavior import GetRelatedBehavior
from agent_v_0_0_2.code.behavior.unifyBehavior.specificBehavior import SpecificBehavior
from agent_v_0_0_2.code.behavior.unifyBehavior.nollm.chooseUniqueBehavior import ChooseUniqueBehavior
from agent_v_0_0_2.code.behavior.unifyBehavior.specificBehaviorEvaluation import SpecificBehaviorEvaluation
from agent_v_0_0_2.code.behavior.unifyBehavior.decisionEvaluation import DecisionEvaluation
from agent_v_0_0_2.code.behavior.unifyBehavior.decisionSummary import DecisionSummary
from agent_v_0_0_2.code.behavior.unifyBehavior.relfect import Reflect

a = Agent(r'G:\毕业设计\pythonProject\agent_v1\agent_v_0_0_2\config\agent\史蒂夫.txt')
e = Environment(agent_list=[a])

while True:
    input('按回车开始一次循环')
    # 1.观察
    o = Observe(a, e)
    o.observe()

    # r = Remember(a)
    # print(r.remember())

    # 2.决策 4O
    d = Decide(a)
    d.decide()

    #3.获取相关属性 haiku
    ra = GetRelatedAttribute(a)
    ra.getRelatedAttribute()

    # #4.决策实施计划 4O
    dp = DecisionPlan(a)
    dp.decisionPlan()
    #
    # #5.获取相关行动 haiku
    rb = GetRelatedBehavior(a)
    rb.getRelatedBehavior()

    DECISION_STATUS = '[UNK]'
    while '正常完成' != DECISION_STATUS[0]:

        #6.采取具体行动 4O
        sb = SpecificBehavior(a)
        SBNAME = sb.specificBehavior()
        print(SBNAME)


        #7.具体行动结果
        cub = ChooseUniqueBehavior(a,e,SBNAME[0])
        ub = cub.chooseUniqueBehavior()
        ub.uniqueBehavior()


        #8.再次观察
        o = Observe(a, e)
        o.observe()

        #9.具体行动结果评估
        sbe = SpecificBehaviorEvaluation(a)
        sbe.specificBehaviorEvaluation()

        #10.决策实施计划状态评估
        de = DecisionEvaluation(a)
        DECISION_STATUS = de.decisionEvaluation()
        print(f'DECISION_STATUS:{DECISION_STATUS[0]}')

# # 6.采取具体行动 (4O or Haiku)
# sb = SpecificBehavior(a)
# SBNAME = sb.specificBehavior()
# print(SBNAME)
# #

# # 7.具体行动结果
# SBNAME = ['原地等待']
# cub = ChooseUniqueBehavior(a, e, SBNAME[0])
# ub = cub.chooseUniqueBehavior()
# ub.uniqueBehavior()

# # 8.再次观察
# o = Observe(a, e)
# o.observe()
#
# # 9.具体行动结果评估 haiku
# sbe = SpecificBehaviorEvaluation(a)
# sbe.specificBehaviorEvaluation()

# 10.决策实施计划状态评估 haiku
# de = DecisionEvaluation(a)
# DECISION_STATUS = de.decisionEvaluation()
# print(DECISION_STATUS)

    # 11.决策总结
    ds = DecisionSummary(a)
    ds.decisionSummary()

    # 12.反思 haiku
    rf = Reflect(a)
    rf.reflect()