# !/usr/bin/python
#-*- coding:utf-8 -*-
import MeCab

#######################################
class Sentence(object):
	def __init__(self):
		pass

	@staticmethod
	def refine_sentence(sentence):
		""" replace ['、' ; '。'; '\t' ; ' ' ; '.' ; '…' ; ' ']  """
		return sentence.replace('\xE3\x80\x81','')\
					   .replace('\xE3\x80\x82','')\
					   .replace('\x5C\x74','')\
					   .replace('%20','')\
					   .replace('\x2E','')\
					   .replace('\xE2\x80\xA6','')\
					   .replace('\xE3\x80\x80','')

	@staticmethod
	def convert_hiratext(sentence):
		hira_text = ""
		tagger = MeCab.Tagger("-Ochasen")
		node = tagger.parseToNode(Sentence.refine_sentence(sentence))
		while node:
			hira_text += node.feature.split(',')[-1]
			node = node.next
		return hira_text