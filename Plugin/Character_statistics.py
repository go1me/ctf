#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
{
title:字符类型统计
author:1me
type:crypto
dialog:
detail:统计大小写，标点符号，数字个数
}
'''
import string
def main(ciphertext):
    digitNum = 0
    upperNum = 0
    lowerNum = 0
    spaceNum = 0
    alphaNum = 0
    otherNum = 0
    punctNum = 0
    punc = string.punctuation
    for i in ciphertext:
        if i.isdigit():
            digitNum = digitNum + 1
        elif i.isspace():
            spaceNum = spaceNum + 1
        elif i.isalpha():
            alphaNum += 1
        elif i in punc:
            punctNum+=1
        else:
            otherNum += 1
        if i.isupper():
            upperNum+=1
        elif i.islower():
            lowerNum+=1
    return " digit %d\r\n space %d\r\n alpha %d\r\n upper%d\r\n lower %d\r\n punctuation %d\r\n other %d"%(digitNum,spaceNum,alphaNum,upperNum,lowerNum,punctNum,otherNum)