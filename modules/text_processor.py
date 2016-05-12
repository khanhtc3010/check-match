#!/usr/bin/python
#-*- coding:utf-8 -*-
from models.sentence import *

########################################
def check_match(src_sentence, check_sentence):
	src_sentence_conv = Sentence.convert_hiratext(src_sentence.encode('utf-8'))
	check_sentence_conv = Sentence.convert_hiratext(check_sentence.encode('utf-8'))
	if(src_sentence_conv == check_sentence_conv):
		return True
	else:
		return False