#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
{
title:获取小写字母
author:1me
type:crypto
dialog:
detail:获取小写字母
}
'''

def main(ciphertext):
	mm=""
	for i in ciphertext:
		if i.islower():
			mm+=i
	return mm