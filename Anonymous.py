#!/usr/bin/env python
##-*- coding: utf-8 -*-
#Выводит бегущуюю стороку с маской
import time, random

def ano(): # r-random f-flow
	x = """999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999993
	999999999999999999999999999999999999999999999                    r99999999999999999999999999999999999999999993
	999999999999999999999999999999999999999                                 X9999999999999999999999999999999999993
	9999999999999999999999999999999999r                                         9999999999999999999999999999999993
	999999999999999999999999999999999                                             99999999999999999999999999999993
	99999999999999999999999999999999                                               9999999999999999999999999999993
	9999999999999999999999999999999                                                9999999999999999999999999999993
	9999999999999999999999999999999                                                 999999999999999999999999999993
	999999999999999999999999999999                                                  999999999999999999999999999993
	999999999999999999999999999999        999999,                    :999999        999999999999999999999999999993
	999999999999999999999999999999     99r  r9999999              9999999s  :99:    ,99999999999999999999999999993
	99999999999999999999999999999s   9     X9999 99999          99999 s9999     X    99999999999999999999999999993
	99999999999999999999999999999               99 9999        9999 99X              99999999999999999999999999993
	99999999999999999999999999999                :99 99        99 99X                99999999999999999999999999993
	99999999999999999999999999999                  S99          S99                  99999999999999999999999999993
	99999999999999999999999999999                   s99        99                    99999999999999999999999999993
	99999999999999999999999999999      ,999999999    299             9999999992      99999999999999999999999999993
	99999999999999999999999999999     99999999999999  99          99999999999999     99999999999999999999999999993
	99999999999999999999999999999   9999999999999999  99          99999999999999:s99 99999999999999999999999999993
	99999999999999999999999999999   r2                999                            99999999999999999999999999993
	99999999999999999999999999999                    X99                             99999999999999999999999999993
	99999999999999999999999999999                    S99                             99999999999999999999999999993
	999999999999999999999999999999                   999                             99999999999999999999999999993
	9999999999999999999999999999999                  999                            299999999999999999999999999993
	999999999999999999999999999992 9                9999                           9999999999999999999999999999993
	999999999999999999999999999999  99            999999        99               9 9999999999999999999999999999993
	9999999999999999999999999999999 99 99        999 999          X    99999999X99 9999999999999999999999999999993
	9999999999999999999999999999999  9: 99       99  999                    99  9  9999999999999999999999999999993
	99999999999999999999999999999999  9  99          99                   S99  9  99999999999999999999999999999993
	999999999999999999999999999999999  9  999r        9       :          999  9s :99999999999999999999999999999993
	9999999999999999999999999999999992  rX 999999    99999999999       9999  9X  999999999999999999999999999999993
	9999999999999999999999999999999999    9  999999999999S :9999999999999s S99  9999999999999999999999999999999993
	99999999999999999999999999999999999    99   X9999999     9999999999    9   99999999999999999999999999999999993
	999999999999999999999999999999999999X   99S        99999ss999r        9   999999999999999999999999999999999993
	9999999999999999999999999999999999999X   999,                        9   9999999999999999999999999999999999993
	99999999999999999999999999999999999999X   99   X                    9   99999999999999999999999999999999999993
	9999999999999999999999999999999999999999  s        :9:.9999        9   999999999999999999999999999999999999993
	99999999999999999999999999999999999999999  9        29999         X  r9999999999999999999999999999999999999993
	999999999999999999999999999999999999999999  9       r9999        r  S99999999999999999999999999999999999999993
	9999999999999999999999999999999999999999999         99999:         X999999999999999999999999999999999999999993
	99999999999999999999999999999999999999999999       9999:99        99999999999999999999999999999999999999999993
	999999999999999999999999999999999999999999999,     9999999       999999999999999999999999999999999999999999993
	9999999999999999999999999999999999999999999999s     99999S      9999999999999999999999999999999999999999999993
	999999999999999999999999999999999999999999999999    99999     X99999999999999999999999999999999999999999999993
	99999999999999999999999999999999999999999999999992  i9999   99999999999999999999999999999999999999999999999993
	99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999993
	99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999993
	99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999993
	99999999999999999999999999999   99   99           999999     999       99       999999999999999999999999999993
	99999999999999999999999999999   9    sS          :999999     999   9    9       999999999999999999999999999993
	99999999999999999999999999999,  r        9    sss999999   9   99   9    9    sss999999999999999999999999999993
	999999999999999999999999999999           9       999999   9   99       99       999999999999999999999999999993
	999999999999999999999999999999     2     9    99999999r       99   9    9    999999999999999999999999999999993
	999999999999999999999999999999     9    99        9999         9   9    9       s99999999999999999999999999993
	999999999999999999999999999999:   99    99        999    99X   s   9    9       s99999999999999999999999999993
	99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999993
	99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999993
	99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999993
	99999999999999     999    9   99       99    9   9   99   9     9     99       9    9   99       9999999999993
	99999999999999      99    9   9    9    9    9   9        9     9     9    9        9   9    9   9999999999993
	9999999999999:  9   99        9    9    9    9   99      99     9     9    9        9   9     :999999999999993
	9999999999999   9   S9        9    9    9        999    999           9    9        9   99       9999999999993
	9999999999999        9   9    9    9    9        999    999   9   i   9    9        9   999999   s999999999993
	999999999999         9   9    9    r    9   9    999    999   9   9   9    s   Ss   i   9    r   9999999999993
	999999999999   999       99   99r     r99   9    999    999   9   9   99      X99S     999      99999999999993
	99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999993"""
	def flow():
		for i in (x.split('\n')):
			for j in i:
				if j != ' ':
					j = str(random.randrange(0, 9))
				else:
					j = ' '
				print(j, end = '')
			print('\n', end = '')
			time.sleep(0.05)
		print("999999999999 We are Anonymous. We are Legion. We do not forgive. We do not forget. Expect us 999999999999999993")
		time.sleep(0.05)
	while True:
		flow()

ano()
