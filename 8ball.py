#!/usr/bin/python
import random
while True:
    answers=["yes", 'no', 'maybe', 'ask again', 'tomorrow', 'go poop and ask again', 'absolutely not', 'of course', "you're gonna die before you know that"]
    question=raw_input('what is your question? ')
    if question.find('many') != 1: answers=[0,1,2,3,4,5,6,7]
    r=random.randint(0,len(answers)-1)
    print answers[r]
