# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 14:47:31 2014

@author: Reinhard
"""

from textblob import TextBlob


afinn = dict(map(lambda (k,v): (k,int(v)), 
                     [ line.split('\t') for line in open("./AFINN/AFINN-111.txt") ]))

def calc_sentiment_word(word, word_before):    
    score = afinn.get(word, 0)
        
    if (word_before == "not"):
        score = score * -1
        
    if (word_before == "no"):
        score = score * -1
    
    return score
        

def calc_sentiment_sentence(sentence):
    sentence = sentence.lower()
    sentence = TextBlob(sentence)
    not_no_count = 0
    
    score = 0
    for i in range(0, len(sentence.words)):        
        word = sentence.words[i].singularize()
        word_before = ""
        if i > 0:
            word_before = sentence.words[i-1]
        
        if (word == "not" or word == "no"):
            not_no_count = not_no_count + 1
        else:
            score = score + calc_sentiment_word(word, word_before)
    
    return score / float((len(sentence.words) - not_no_count)), sentence.sentiment.polarity