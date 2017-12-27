# -*- coding: utf-8 -*-

'''
    Created on Aug 11, 2017
    
    @author: matthewcowen-green
    
    
    STACK-BASED LANGUAGE
    '''


# Codepage: 'ƩΠµṀϺ²³¹⁰⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉¼½¾⅐⅑⅒⅓⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞⅟Ƨ°|!÷↑↓←↕↔⇹¬^«»≤≥<>=≠√∛∜∞∈~˜%/+-*△⬠⬡∧∨⊼⊽⊻⊼⌊⌈⎶‰×ÅąÇČƇçč¢ćĆĉðḋ₫ĐéǝḞǤĦĨƖǰḶĻĽĹŁĿļɬłɫɯɳṔƤǷҎᑭ₽ṕƥṗƿϼҏ₱ŘɽɾɹʀřŕŞŠŜŚşŝšȘŤŦťŧỤʊŽπφ≡_‼`⦋'



import string
import math
from __builtin__ import  pow as ppow

from operator import mul
from numpy import median, Infinity
import numpy as np
from scipy.stats import mode
from math import factorial, sqrt, pow, floor, ceil, sin, cos, tan, cosh, sinh, tanh, acos, acosh, atan, atanh, asin, asinh, log, exp
from itertools import count, islice
import random
from scipy.misc import factorial2


def parse(line, stck):
    l=len(line)
    i=0
    while i in range(l):
        #d=u""
        cc=line[i]
        '''if(cc in u""+string.letters):
            d+=cc
            elif(cc in u""+string.digits or cc==u'.'):
            d+=cc
            elif(d!=u""):
            if(d.replace(u'.',u'',1).isdigit()):
            if(d.contains(u'.')):
            stck.append(float(d))
            else:
            stck.append(int(d))
            else:
            stck.append(d)'''
        #print(stck,cc)
        stck,i=interpret(cc,stck,i,line)
        i+=1
    for j in stck:
        print(j)
    return stck


def interpret(cc,stck,i,line):
    #print(stck,cc)
    if(cc in string.digits):
        stck.append(int(cc))
        return stck,i
    elif cc==u"Σ" or cc==u"Ʃ":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(stck.pop().sum())
        elif(type(stck[-1]) is list):
            q=stck.pop()
            stck.append(sum(q))
        else:
            stckk=stck
            stck=[]
            stck.append(sum(stckk))
    elif cc==u"Π":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(stck.pop().prod())
        elif(isinstance(stck[-1],list)):
            stck.append(reduce(mul,stck.pop(),1))
        else:
            stckk=stck
            stck=[]
            stck.append(reduce(mul,stckk,1))
    elif cc==u"µ":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(stck.pop().mean())
        elif(isinstance(stck[-1],list)):
            q=stck.pop()
            stck.append(sum(q)/len(q))
        else:
            stckk=stck
            stck=[]
            stck.append(sum(stckk)/len(stckk))
    elif cc==u"Ṁ":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.median(stck.pop()))
        elif(isinstance(stck[-1],list)):
            stck.append(median(stck.pop()))
        else:
            stckk=stck
            stck=[]
            stck.append(median(stckk))
    elif cc==u"Ϻ":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(stck.pop().tolist())
        if(isinstance(stck[-1],list)):
            stck.append(mode(stck.pop())[0,0])
        else:
            stckk=stck
            stck=[]
            stck.append(mode(stckk)[0][0])
    elif cc==u"²":
        if(isinstance(stck[-1],list) or isinstance(stck[-1],np.ndarray)):
            stck.append(np.power(stck.pop(),2))
        else:
            stck.append(stck.pop()**2)
    elif cc==u"³":
        if(isinstance(stck[-1],list) or isinstance(stck[-1],np.ndarray)):
            stck.append(np.power(stck.pop(),3))
        else:
            stck.append(stck.pop()**3)
    elif cc==u"¹":
        if(isinstance(stck[-1],list) or isinstance(stck[-1],np.ndarray)):
            stck.append(np.power(stck.pop(),11))
        else:
            stck.append(stck.pop()**11)
    elif cc==u"⁰":
        if(isinstance(stck[-1],list) or isinstance(stck[-1],np.ndarray)):
            stck.append(np.power(stck.pop(),10))
        else:
            stck.append(stck.pop()**10)
    elif cc==u"⁴":
        if(isinstance(stck[-1],list) or isinstance(stck[-1],np.ndarray)):
            stck.append(np.power(stck.pop(),4))
        else:
            stck.append(stck.pop()**4)
    elif cc==u"⁵":
        if(isinstance(stck[-1],list) or isinstance(stck[-1],np.ndarray)):
            stck.append(np.power(stck.pop(),5))
        else:
            stck.append(stck.pop()**5)
    elif cc==u"⁶":
        if(isinstance(stck[-1],list) or isinstance(stck[-1],np.ndarray)):
            stck.append(np.power(stck.pop(),6))
        else:
            stck.append(stck.pop()**6)
    elif cc==u"⁷":
        if(isinstance(stck[-1],list) or isinstance(stck[-1],np.ndarray)):
            stck.append(np.power(stck.pop(),7))
        else:
            stck.append(stck.pop()**7)
    elif cc==u"⁸":
        if(isinstance(stck[-1],list) or isinstance(stck[-1],np.ndarray)):
            stck.append(np.power(stck.pop(),8))
        else:
            stck.append(stck.pop()**8)
    elif cc==u"⁹":
        if(isinstance(stck[-1],list) or isinstance(stck[-1],np.ndarray)):
            stck.append(np.power(stck.pop(),9))
        else:
            stck.append(stck.pop()**9)
    elif cc==u"₀":
        if(isinstance(stck[-1],list)):
            stck.append(np.array(stck.pop(), dtype='f')/10)
        else:
            stck.append(stck.pop()/10)
    elif cc==u"₁":
        if(isinstance(stck[-1],list)):
            stck.append(np.array(stck.pop(), dtype='f')/11)
        else:
            stck.append(stck.pop()/11)
    elif cc==u"₂":
        if(isinstance(stck[-1],list)):
            stck.append(np.array(stck.pop(), dtype='f')/2)
        else:
            stck.append(stck.pop()/2)
    elif cc==u"₃":
        if(isinstance(stck[-1],list)):
            stck.append(np.array(stck.pop(), dtype='f')/3)
        else:
            stck.append(stck.pop()/3)
    elif cc==u"₄":
        if(isinstance(stck[-1],list)):
            stck.append(np.array(stck.pop(), dtype='f')/4)
        else:
            stck.append(stck.pop()/4)
    elif cc==u"₅":
        if(isinstance(stck[-1],list)):
            stck.append(np.array(stck.pop(), dtype='f')/5)
        else:
            stck.append(stck.pop()/5)
    elif cc==u"₆":
        if(isinstance(stck[-1],list)):
            stck.append(np.array(stck.pop(), dtype='f')/6)
        else:
            stck.append(stck.pop()/6)
    elif cc==u"₇":
        if(isinstance(stck[-1],list)):
            stck.append(np.array(stck.pop(), dtype='f')/7)
        else:
            stck.append(stck.pop()/7)
    elif cc==u"₈":
        if(isinstance(stck[-1],list)):
            stck.append(np.array(stck.pop(), dtype='f')/8)
        else:
            stck.append(stck.pop()/8)
    elif cc==u"₉":
        if(isinstance(stck[-1],list)):
            stck.append(np.array(stck.pop(), dtype='f')/9)
        else:
            stck.append(stck.pop()/9)
    elif cc==u"¼":
        stck.append(1./4)
    elif cc==u"½":
        stck.append(1./2)
    elif cc==u"¾":
        stck.append(3./4)
    elif cc==u"⅐":
        stck.append(1./7)
    elif cc==u"⅑":
        stck.append(1./9)
    elif cc==u"⅒":
        stck.append(1./10)
    elif cc==u"⅓":
        stck.append(1./3)
    elif cc==u"⅕":
        stck.append(1./5)
    elif cc==u"⅖":
        stck.append(2./5)
    elif cc==u"⅗":
        stck.append(3./5)
    elif cc==u"⅘":
        stck.append(4./5)
    elif cc==u"⅙":
        stck.append(1./6)
    elif cc==u"⅚":
        stck.append(5./6)
    elif cc==u"⅛":
        stck.append(1./8)
    elif cc==u"⅜":
        stck.append(3./8)
    elif cc==u"⅝":
        stck.append(5./8)
    elif cc==u"⅞":
        stck.append(7./8)
    elif cc==u"⅟":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(stck.pop().tolist())
        if(isinstance(stck[-1],list)):
            stck.append([1./x for x in stck.pop()])
        else:
            stck.append(1./stck.pop())
    elif cc==u"Ƨ":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(stck.pop().tolist())
        if(isinstance(stck[-1],list)):
            stck.append(stck.pop()[::2])
        else:
            stckk=stck
            stck=[]
            stck=stckk[::2]
    elif cc==u"°":
        if(isinstance(stck[-2],list) and isinstance(stck[-3],list)):
            q=int(stck.pop())
            qq=stck.pop()
            qqq=stck.pop()
            stck.append([ppow(qqq[o],qq[o],q) for o in range(len(qq))])
        else:
            q=stck.pop()
            qq=stck.pop()
            stck.append(ppow(stck.pop(),qq,q))
    elif cc==u"|":
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(q,list)):
            if(isinstance(qq,list)):
                stck.append([qq[j]%q[j]==0 for j in range(min(len(qq),len(q)))])
            else:
                stck.append([qq%x==0 for x in q])
        else:
            if(isinstance(qq,list)):
                stck.append([x%q==0 for x in qq])
            else:
                stck.append(qq%q==0)
    elif cc==u"!":
        q=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(q,list)):
            stck.append([factorial(x) for x in q])
        else:
            stck.append(factorial(q))
    elif cc==u"÷":
        q=stck.pop()
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(stck.pop()//q)
        elif(isinstance(stck[-1],list)):
            stck.append([int(x/q) for x in stck.pop()])
        else:
            stck.append(int(stck.pop()/q))
    elif cc==u"↑":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.nanmax(stck.pop()))
        elif(isinstance(stck[-1],list)):
            stck.append(max(stck.pop()))
        else:
            stckk=stck
            stck=[]
            stck.append(max(stckk))
    elif cc==u"↓":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.nanmin(stck.pop()))
        elif(isinstance(stck[-1],list)):
            stck.append(min(stck.pop()))
        else:
            stckk=stck
            stck=[]
            stck.append(min(stckk))
    elif cc==u"←":
        q=raw_input()
        try:
            qq=float(q)
        except ValueError:
            qq=q
        if(q[0]=='[' and q[-1]==']'):
            stck.append(eval(q))
        else:
            stck.append(qq)
    #stck.append(raw_input())
    elif cc==u"↕":
        if(isinstance(stck[-1],np.ndarray)):
            q=stck.pop()
            stck.append([np.nanmin(q),np.nanmax(q)])
        elif(isinstance(stck[-1],list)):
            q=stck.pop()
            stck.append([min(q),max(q)])
        else:
            stckk=stck
            stck=[]
            stck.append([min(stckk),max(stckk)])
    elif cc==u"↔":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(stck.pop().tolist())
        if(isinstance(stck[-1],list)):
            stck[-1].reverse()
        else:
            stck.reverse()
    elif cc==u"⇹":
        q=stck.pop()
        qq=stck.pop()
        stck.append(q)
        stck.append(qq)
    elif cc==u"¬":
        stck.append(not stck.pop())
    elif cc==u"^":
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(qq,list)):
            stck.append(np.power(qq,q))
        elif(isinstance(q,list)):
            stck.append([pow(qq,x) for x in q])
        else:
            stck.append(math.pow(qq,q))
    elif cc==u"«":
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(qq,list)):
            stck.append([x<<q for x in qq])
        else:
            stck.append(qq<<q)
    elif cc==u"»":
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(qq,list)):
            stck.append([x>>q for x in qq])
        else:
            stck.append(qq>>q)
    elif cc==u"≤":
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(q,list)):
            if(isinstance(qq,list)):
                stck.append([qq[j]<=q[j] for j in range(min(len(qq),len(q)))])
            else:
                stck.append([qq<=x for x in q])
        else:
            if(isinstance(qq,list)):
                stck.append([x<=q for x in qq])
            else:
                stck.append(qq<=q)
    elif cc==u"≥":
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(q,list)):
            if(isinstance(qq,list)):
                stck.append([qq[j]>=q[j] for j in range(min(len(qq),len(q)))])
            else:
                stck.append([qq>=x for x in q])
        else:
            if(isinstance(qq,list)):
                stck.append([x>=q for x in qq])
            else:
                stck.append(qq>=q)
    elif cc==u"<":
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(q,list)):
            if(isinstance(qq,list)):
                stck.append([qq[j]<q[j] for j in range(min(len(qq),len(q)))])
            else:
                stck.append([qq<x for x in q])
        else:
            if(isinstance(qq,list)):
                stck.append([x<q for x in qq])
            else:
                stck.append(qq<q)
    elif cc==u">":
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(q,list)):
            if(isinstance(qq,list)):
                stck.append([qq[j]>q[j] for j in range(min(len(qq),len(q)))])
            else:
                stck.append([q>x for x in q])
        else:
            if(isinstance(qq,list)):
                stck.append([x>q for x in qq])
            else:
                stck.append(qq>q)
    elif cc==u"=":
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(q,list)):
            if(isinstance(qq,list)):
                stck.append([qq[j]==q[j] for j in range(min(len(qq),len(q)))])
            else:
                stck.append([qq==x for x in q])
        else:
            if(isinstance(qq,list)):
                stck.append([x==q for x in qq])
            else:
                stck.append(qq==q)
    elif cc==u"≠":
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(q,list)):
            if(isinstance(qq,list)):
                stck.append([qq[j]!=q[j] for j in range(min(len(qq),len(q)))])
            else:
                stck.append([qq!=x for x in q])
        else:
            if(isinstance(qq,list)):
                stck.append([x!=q for x in qq])
            else:
                stck.append(qq!=q)
    elif cc==u"√":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.pow(stck.pop(),1./2))
        elif(isinstance(stck[-1],list)):
            stck.append([sqrt(float((x))) for x in stck.pop()])
        else:
            stck.append(sqrt(float(stck.pop())))
    elif cc==u"∛":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.pow(stck.pop(),1./3))
        elif(isinstance(stck[-1],list)):
            stck.append([pow(x,1./3) for x in stck.pop()])
        else:
            stck.append(pow(stck.pop(),1./3))
    elif cc==u"∜":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.pow(stck.pop(),1./4))
        elif(isinstance(stck[-1],list)):
            stck.append([pow(x,1./4) for x in stck.pop()])
        else:
            stck.append(pow(stck.pop(),1./4))
    elif cc==u"∞":
        stck.append(Infinity)
    elif cc==u"∈":
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,list)):
            stck.append([x in q for x in qq])
        else:
            stck.append(qq in q)
    elif cc==u"~":
        q=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(q,list)):
            stck.append([-x for x in q])
        else:
            stck.append(-q)
    elif cc==u"˜": #unsigned two's-complement
        q=stck.pop()
        if(isinstance(q,list)):
            stck.append([int(2**ceil(log(x,2))-x) for x in q])
        else:
            stck.append(int(2**ceil(log(q,2))-q))
    elif cc==u"%":
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,list)):
            if(isinstance(q,list)):
                stck.append([qq[j]%q[j] for j in range(min(len(qq),len(q)))])
            else:
                stck.append([x%q for x in qq])
        else:
            if(isinstance(q,list)):
                stck.append([qq%x for x in q])
            else:
                stck.append(qq%q)
    elif cc==u"/":
        if(isinstance(stck[-1],np.ndarray) and isinstance(stck[-2],np.ndarray)):
           q=stck.pop()
           stck.append(np.divide(stck.pop(),q))
        elif(isinstance(stck[-1],list) and isinstance(stck[-2],np.ndarray)):
            q=np.array(stck.pop())
            stck.append(np.divide(stck.pop(),q).tolist())
        elif(isinstance(stck[-1],np.ndarray) and isinstance(stck[-2],list)):
            q=stck.pop()
            stck.append(np.divide(np.array(stck.pop()),q))
        elif(isinstance(stck[-1],list) and isinstance(stck[-2],list)):
            q=stck.pop()
            stck.append(np.divide(np.array(stck.pop()),np.array(q)))
        else:
            q=float(stck.pop())
            if(isinstance(stck[-1],list)):
                stck.append(np.divide(np.array(stck.pop()),q))
            else:
                stck.append(stck.pop()/q)
    elif cc==u"+":
        if(isinstance(stck[-1],np.ndarray) and isinstance(stck[-2],np.ndarray)):
            q=stck.pop()
            stck.append(np.add(stck.pop(),q))
        elif(isinstance(stck[-1],list) and isinstance(stck[-2],np.ndarray)):
            q=np.array(stck.pop())
            stck.append(np.add(stck.pop(),q).tolist())
        elif(isinstance(stck[-1],np.ndarray) and isinstance(stck[-2],list)):
            q=stck.pop()
            stck.append(np.add(np.array(stck.pop()),q))
        elif(isinstance(stck[-1],list) and isinstance(stck[-1],list)):
            q=stck.pop()
            stck.append(np.add(np.array(stck.pop()),np.array(q)).tolist())
        else:
            q=float(stck.pop())
            if(isinstance(stck[-1],list)):
                stck.append(np.add(np.array(stck.pop()),q))
            else:
                stck.append(stck.pop()+q)

    elif cc==u"-":
        if(isinstance(stck[-1],np.ndarray) and isinstance(stck[-2],np.ndarray)):
            q=stck.pop()
            stck.append(np.subtract(stck.pop(),q))
        elif(isinstance(stck[-1],list) and isinstance(stck[-1],list)):
            q=stck.pop()
            stck.append(np.subtract(np.array(stck.pop()),np.array(q)).tolist())
        elif(isinstance(stck[-1],np.ndarray) and isinstance(stck[-2],list)):
            q=stck.pop()
            stck.append(np.subtract(np.array(stck.pop()),q))
        elif(isinstance(stck[-1],list) and isinstance(stck[-2],np.ndarray)):
            q=np.array(stck.pop())
            stck.append(np.subtract(stck.pop(),q).tolist())
        else:
            q=float(stck.pop())
            if(isinstance(stck[-1],list)):
                stck.append(np.subtract(np.array(stck.pop()),q))
            else:
                stck.append(stck.pop()-q)
    elif cc==u"*":
        if(isinstance(stck[-1],np.ndarray) and isinstance(stck[-2],np.ndarray)):
            q=stck.pop()
            stck.append(np.multiply(stck.pop(),q))
        elif(isinstance(stck[-1],list) and isinstance(stck[-2],np.ndarray)):
            q=np.array(stck.pop())
            stck.append(np.multiply(stck.pop(),q).tolist())
        elif(isinstance(stck[-1],np.ndarray) and isinstance(stck[-2],list)):
            q=stck.pop()
            stck.append(np.multiply(np.array(stck.pop()),q))
        elif(isinstance(stck[-1],list) and isinstance(stck[-1],list)):
            q=stck.pop()
            stck.append(np.multiply(np.array(stck.pop()),np.array(q)).tolist())
        elif(isinstance(stck[-1],np.ndarray)):
            q=stck.pop()
            stck.append(np.multiply(q,stck.pop()).tolist())
        else:
            q=float(stck.pop())
            if(isinstance(stck[-1],list)):
                stck.append(np.multiply(np.array(stck.pop()),q))
            else:
                stck.append(stck.pop()*q)
    elif cc==u"△":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(stck.pop().tolist())
        if(isinstance(stck[-1],list)):
            stck.append([(x**2+x)/2 for x in stck.pop()])
        else:
            q=stck.pop()
            stck.append((q**2+q)/2)
    elif cc==u"⬠":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(stck.pop().tolist())
        if(isinstance(stck[-1],list)):
            stck.append([(3*x**2-x)/2 for x in stck.pop()])
        else:
            q=stck.pop()
            stck.append((3*q**2-q)/2)
    elif cc==u"⬡":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(stck.pop().tolist())
        if(isinstance(stck[-1],list)):
            stck.append([2*x**2-x for x in stck.pop()])
        else:
            q=stck.pop()
            stck.append(2*q**2-q)
    elif cc==u"∧":
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,list)):
            if(isinstance(q,list)):
                stck.append([qq[j] and q[j] for j in range(min(len(q),len(qq)))])
            else:
                stck.append([x and q for x in qq])
        else:
            if(isinstance(q,list)):
                stck.append([qq and x for x in q])
            else:
                stck.append(qq and q)
    elif cc==u"∨":
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,list)):
            if(isinstance(q,list)):
                stck.append([qq[j] or q[j] for j in range(min(len(q),len(qq)))])
            else:
                stck.append([x or q for x in qq])
        else:
            if(isinstance(q,list)):
                stck.append([qq or x for x in q])
            else:
                stck.append(qq or q)
    elif cc==u"⊼": #NAND
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,list)):
            if(isinstance(q,list)):
                stck.append([not(qq[j] and q[j]) for j in range(min(len(q),len(qq)))])
            else:
                stck.append([not(x and q) for x in qq])
        else:
            if(isinstance(q,list)):
                stck.append([not(qq and x) for x in q])
            else:
                stck.append(not(qq and q))
    elif cc==u"⊽": #NOR
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,list)):
            if(isinstance(q,list)):
                stck.append([not(qq[j] or q[j]) for j in range(min(len(q),len(qq)))])
            else:
                stck.append([not(x or q) for x in qq])
        else:
            if(isinstance(q,list)):
                stck.append([not(qq or x) for x in q])
            else:
                stck.append(not(qq or q))
    elif cc==u"⊻": #XOR
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,list)):
            if(isinstance(q,list)):
                stck.append([(qq[j] and not q[j]) or (not qq[j] and q[j]) for j in range(min(len(q),len(qq)))])
            else:
                stck.append([(x and not q) or (not x and q) for x in qq])
        else:
            if(isinstance(q,list)):
                stck.append([(qq and not x) or (not qq and x) for x in q])
            else:
                stck.append((qq and not q) or (q and not qq))
    elif cc==u"⊼": #XNOR
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,list)):
            if(isinstance(q,list)):
                stck.append([(qq[j] and q[j]) or not(qq[j] or q[j]) for j in range(min(len(q),len(qq)))])
            else:
                stck.append([(x and q) or not(x or q) for x in qq])
        else:
            if(isinstance(q,list)):
                stck.append([(qq and x) or not(qq or x) for x in q])
            else:
                stck.append((qq and q) or not(qq or q))
    elif cc==u"⌊":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.floor(stck.pop()))
        elif(isinstance(stck[-1],list)):
            stck.append([floor(x) for x in stck.pop()])
        else:
            stck.append(floor(stck.pop()))
    elif cc==u"⌈":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.ceil(stck.pop()))
        elif(isinstance(stck[-1],list)):
            stck.append([ceil(x) for x in stck.pop()])
        else:
            stck.append(ceil(stck.pop()))
    elif cc==u"⎶": #ROUND TO NEAREST INTEGER
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.rint(stck.pop()))
        elif(isinstance(stck[-1],list)):
            stck.append([round(x) for x in stck.pop()])
        else:
            stck.append(round(stck.pop()))
    elif cc==u"‰": #INTEGER DIVISION AND REMAINDER
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,list)):
            if(isinstance(q,list)):
                stck.append([[int(qq[j]/q[j]),qq[j]%q[j]] for j in range(min(len(q),len(qq)))])
            else:
                stck.append([[int(x/q),x%q] for x in qq])
        else:
            if(isinstance(q,list)):
                stck.append([[int(qq/x),qq%x] for x in q])
            else:
                stck.append([int(qq/q),qq%q])
    elif cc==u"×":
        x=stck.pop()
        y=stck.pop()
        stck.append(np.transpose([np.tile(y, len(x)), np.repeat(x, len(y))]))
    elif cc==u"Å":
        q=stck.pop()
        if(isinstance(q,np.ndarray)):
            stck.append(np.absolute(q))
        elif(isinstance(q,list)):
            stck.append([abs(x) for x in q])
        else:
            stck.append(abs(q))
    elif cc==u"ą": #convert number to array of digits
        q=stck.pop()
        qq=list(str(q))
        stck.append([int(x) for x in qq])
    elif cc==u"á": #put contents of stack in an array
        stckk=[stck]
        stck=stckk
    elif cc==u"ɓ": #convert to binary string (less the 0b)
        q=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(q,list)):
            stck.append([bin(int(x))[2:] for x in q])
        else:
            stck.append(bin(int(q))[2:])
    elif cc==u"Ç":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.arccosh(stck.pop()))
        elif(isinstance(stck[-1],list)):
            stck.append([acosh(x) for x in stck.pop()])
        else:
            stck.append(acosh(stck.pop()))
    elif cc==u"Č":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.cosh(stck.pop()))
        elif(isinstance(stck[-1],list)):
            stck.append([cosh(x) for x in stck.pop()])
        else:
            stck.append(cosh(stck.pop()))
    elif cc==u"Ƈ":
        q=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(q,list)):
            stck.append([unichr(int(x)) for x in q])
        else:
            stck.append(unichr(int(q)))
    elif cc==u"ç":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.arccos(stck.pop()))
        elif(isinstance(stck[-1],list)):
            stck.append([acos(x) for x in stck.pop()])
        else:
            stck.append(acos(stck.pop()))
    elif cc==u"č":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.cos(stck.pop()))
        elif(isinstance(stck[-1],list)):
            stck.append([cos(x) for x in stck.pop()])
        else:
            stck.append(cos(stck.pop()))
    elif cc==u"¢":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(stck.pop().tolist())
        if(isinstance(stck[-1],list)):
            stck.append([1-x for x in stck.pop()])
        else:
            stck.append(1-stck.pop())
    elif cc==u"ć":
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(qq,list)):
            if(isinstance(q,list)):
                stck.append([factorial(qq[j])/(factorial(q[j])*factorial(qq[j]-q[j])) for j in range(min(len(qq),len(q)))])
            else:
                stck.append([factorial(x)/(factorial(q)*factorial(x)) for x in qq])
        else:
            if(isinstance(q,list)):
                stck.append([factorial(qq)/(factorial(x)*factorial(qq-x)) for x in q])
            else:
                stck.append(factorial(qq)/(factorial(q)*factorial(qq-q)))
    elif cc==u"Ć":
        n=stck.pop()
        if(isinstance(n,np.ndarray)):
            n=n.tolist()
        if(isinstance(n,list)):
            stck.append([factorial(2*x)/(factorial(x+1)*factorial(x)) for x in n])
        else:
            stck.append(factorial(2*n)/(factorial(n+1)*factorial(n)))
    elif cc==u"ĉ":
        stck=[]
    elif cc==u"ḋ":
        stck.append(primeFactors(stck.pop()))
    elif cc==u"₫":
        q=(""+str(int(stck.pop())))[::-1]
        stck.append(int(q))
    elif cc==u"ð":
        q=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(q,list)):
            stck.append([divisors(int(x)) for x in q])
        else:
            stck.append(divisors(int(q)))
    elif cc==u"Đ": #duplicate item on top of stack
        q=stck.pop()
        stck+=[q,q]
    elif cc==u"é":
        stck.append(2.71828182845904523536028747135266249775724709369995)
    elif cc==u"Ḟ":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(stck.pop().tolist())
        if(isinstance(stck[-1],list)):
            stck.append([fib(x) for x in stck.pop()])
        else:
            stck.append(fib(stck.pop()))
    elif cc==u"Ǥ":
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(qq,list)):
            if(isinstance(q,list)):
                stck.append([gcd(qq[j],q[j]) for j in range(min(len(qq),len(q)))])
            else:
                stck.append([gcd(x,q) for x in qq ])
        else:
            if(isinstance(q,list)):
                stck.append([gcd(qq,x) for x in q])
            else:
                stck.append(gcd(qq,q))
    elif cc==u"Ħ":
        q=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(q,list)):
            stck.append([hamming(x) for x in q])
        else:
            stck.append(hamming(q))
    elif cc==u"Ĩ":
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(qq,list)):
            if(isinstance(q,list)):
                stck.append([readasbase(str(int(qq[j])),int(q[j])) for j in range(min(len(qq),len(q)))])
            else:
                stck.append([readasbase(str(int(x)),int(q)) for x in qq ])
        else:
            if(isinstance(qq,float)):
                qq=int(qq)
            if(isinstance(q,list)):
                stck.append([readasbase(str(qq),int(x)) for x in q])
            else:
                stck.append(readasbase(str(qq),int(q)))
    elif cc==u"ǰ":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(stck.pop().tolist())
        if(isinstance(stck[-1],list)):
            stck.append(str(stck.pop()).replace('[','').replace(']','').replace(',',''))
        else:
            stckk=stck
            stck=[]
            stck.append(str(stckk).replace('[','').replace(']','').replace(',',''))
    elif cc==u"Ɩ":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(stck.pop().tolist())
        if(isinstance(stck[-1],list)):
            stck.append([int(x) for x in stck.pop()])
        else:
            stck.append(int(stck.pop()))
    elif cc==u"Ḷ":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.log10(stck.pop()))
        elif(isinstance(stck[-1],list)):
            stck.append([log(x,10) for x in stck.pop()])
        else:
            stck.append(log(stck.pop(),10))
    elif cc==u"Ļ":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.log(stck.pop()))
        elif(isinstance(stck[-1],list)):
            stck.append([log(x) for x in stck.pop()])
        else:
            stck.append(log(stck.pop()))
    elif cc==u"Ľ":
        q=stck.pop()
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(stck.pop().tolist())
        if(isinstance(stck[-1],list)):
            stck.append([log(x,q) for x in stck.pop()])
        else:
            stck.append(log(stck.pop(),q))
    elif cc==u"Ĺ":
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(qq,list)):
            if(isinstance(q,list)):
                stck.append([int(qq[j])*int(q[j])/gcd(int(qq[j]),int(q[j])) for j in range(min(len(qq),len(q)))])
            else:
                stck.append([int(x)*int(q)/gcd(int(x),int(q)) for x in qq])
        else:
            if(isinstance(q,list)):
                stck.append([int(qq)*int(x)/gcd(int(qq),int(x)) for x in q])
            else:
                stck.append(int(qq)*int(q)/gcd(int(qq),int(q)))
    elif cc==u"Ł":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(stck.pop().tolist())
        if(isinstance(stck[-1],list)):
            stck.append(len(stck.pop()))
        else:
            stckk=stck
            stck=[]
            stck.append(len(stckk))
    elif cc==u"Ŀ":
        q=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(q,list)):
            stck.append([lucas(x) for x in q])
        else:
            stck.append(lucas(q))
    elif cc==u"ļ":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.log2(stck.pop()))
        elif(isinstance(stck[-1],list)):
            stck.append([log(x,2) for x in stck.pop()])
        else:
            stck.append(log(stck.pop(),2))
    elif cc==u"ɬ":
        stck.append("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    elif cc==u"ɫ":
        stck.append("abcdefghijklmnopqrstuvwxyz")
    elif cc==u"ɯ": #modular inverse
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(qq,list)):
            if(isinstance(q,list)):
                stck.append([mulinv(int(qq[j]),int(q[j])) for j in range(min(len(qq),len(q)))])
            else:
                stck.append([mulinv(int(x),int(q)) for x in qq])
        else:
            if(isinstance(q,list)):
                stck.append([mulinv(int(qq),int(x)) for x in q])
            else:
                stck.append(mulinv(int(qq),int(q)))
    elif cc==u"ɳ":
        stck.append("0123456789")
    elif cc==u"Ṕ":
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(qq,list)):
            if(isinstance(q,list)):
                print([str(base(int(qq[j]),int(q[j]))) for j in range(min(len(qq),len(q)))]+"\n")
            else:
                print([str(base(int(x),int(q))) for x in qq ]+"\n")
        else:
            if(isinstance(q,list)):
                print([str(base(int(qq),int(x))) for x in q]+"\n")
            else:
                print(str(base(int(qq),int(q)))+"\n")
    elif cc==u"Ƥ":
        print(str(stck.pop())+"\n")
    elif cc==u"Ƿ":
        q=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(q,list)):
            print([bin(int(x)) for x in q]+"\n")
        else:
            print(bin(int(q))+"\n")
    elif cc==u"Ҏ":
        q=stck.pop()
        w=str(int(q))
        k=1
        for j in w:
            k*=int(j)
        stck.append(k)
    elif cc==u"ᑭ": #Polygonal number
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(qq,list)):
            if(isinstance(q,list)):
                stck.append([1./2*int(qq[j])*((int(q[j])-2)*int(qq[j])-(int(q[j])-4)) for j in range(min(len(qq),len(q)))])
            else:
                q=int(q)
                stck.append([1./2*int(x)*((q-2)*int(x)-(q-4)) for x in qq])
        else:
            if(isinstance(q,list)):
                qq=int(qq)
                stck.append([1./2*qq*((int(x)-2)*qq-(int(x)-4)) for x in q])
            else:
                q=int(q)
                qq=int(qq)
                stck.append(1./2*qq*((q-2)*qq-(q-4)))
    elif cc==u"₽":
        q=stck.pop()
        stck.append(str(q)==str(q)[::-1])
    elif cc==u"ṕ":
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,np.ndarray)):
            qq=qq.tolist()
        if(isinstance(qq,list)):
            if(isinstance(q,list)):
                print([str(base(int(qq[j]),int(q[j]))) for j in range(min(len(qq),len(q)))])
            else:
                print([str(base(int(x),int(q))) for x in qq ])
        else:
            if(isinstance(q,list)):
                print([str(base(int(qq),int(x))) for x in q])
            else:
                print(str(base(int(qq),int(q))))
    elif cc==u"ƥ":
        print(stck.pop())
    elif cc==u"ṗ":
        q=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(q,list)):
            stck.append([isPrime(int(x)) for x in q])
        else:
            stck.append(isPrime(int(q)))
    elif cc==u"ƿ":
        q=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(q,list)):
            print([bin(int(x)) for x in q])
        else:
            print(bin(int(q)))
    elif cc==u"ϼ":
        q=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(q,list)):
            stck.append([getUnique(primeFactors(int(x))) for x in q])
        else:
            stck.append(getUnique(primeFactors(int(q))))
    elif cc==u"ҏ":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(stck.pop().tolist())
        if(isinstance(stck[-1],list)):
            q=stck.pop()
            stck.append(q+q[::-1])
        elif(isinstance(stck[-1],str)):
            q=stck.pop()
            stck.append(q+q[::-1])
        else:
            stckk=stck
            stck=stckk+stckk[::-1]
    elif cc==u"₱":
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(qq,np.ndarray)):
                qq=qq.tolist()
        if(isinstance(qq,list)):
            if(isinstance(q,list)):
                stck.append([factorial(int(qq[j]))/factorial(int(qq[j])-int(q[j])) for j in range(min(len(qq),len(q)))])
            else:
                stck.append([factorial(int(x))/factorial(int(x)-int(q)) for x in qq ])
        else:
            if(isinstance(q,list)):
                stck.append([factorial(int(qq))/factorial(int(qq)-int(x)) for x in q])
            else:
                stck.append(factorial(int(q))/factorial(int(qq)-int(q)))
    elif cc==u"Ř":
        q=list(range(int(stck[-2]),int(stck[-1])+1))
        stck.pop()
        stck.pop()
        stck.append(q)
    elif cc==u"ɽ":
        stck.append(int(random.random()*(2**32)))
    elif cc==u"ɾ":
        aa=int(stck.pop())
        bb=int(stck.pop())
        stck.append(random.randrange(bb,aa))
    elif cc==u"ɹ":
        stck.append(random.getrandbits(1))
    elif cc==u"ʀ":
        stck.append(random.choice(stck.pop()))
    elif cc==u"ṛ":
        stck.append(random.random())
    elif cc==u"ř":
        stck.append(range(1,int(stck.pop())+1))
    elif cc==u"Ş":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(stck.pop().tolist())
        if(isinstance(stck[-1],list)):
            stck.append(sorted(stck.pop())[::-1])
        else:
            stck=sorted(stck)[::-1]
    elif cc==u"Š":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.sinh(stck.pop()))
        elif(isinstance(stck[-1],list)):
            stck.append([sinh(x) for x in stck.pop()])
        else:
            stck.append(sinh(stck.pop()))
    elif cc==u"Ŝ":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.arcsinh(stck.pop()))
        elif(isinstance(stck[-1],list)):
            stck.append([asinh(x) for x in stck.pop()])
        else:
            stck.append(asinh(stck.pop()))
    elif cc==u"Ś":
        q=stck.pop()
        w=str(int(q))
        k=0
        for j in w:
            k+=int(j)
        stck.append(k)
    elif cc==u"ş" or cc==u"ş":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(stck.pop().tolist())
        if(isinstance(stck[-1],list)):
            stck.append(sorted(stck.pop()))
        else:
            stck=sorted(stck)
    elif cc==u"ŝ":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.arcsin(stck.pop()))
        elif(isinstance(stck[-1],list)):
            stck.append([asin(x) for x in stck.pop()])
        else:
            stck.append(asin(stck.pop()))
    elif cc==u"š":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.sin(stck.pop()))
        elif(isinstance(stck[-1],list)):
            stck.append([sin(x) for x in stck.pop()])
        else:
            stck.append(sin(stck.pop()))
    elif cc==u"Ș": # Reverse last k items (in stack if not list)
        q=stck.pop()
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(stck.pop().tolist())
        if(isinstance(stck[-1],list)):
            qq=stck.pop()
            qqq=qq[-q:]
            stck.append(qq[0:-q]+qqq[::-1])
        else:
            stckk=stck[-q:]
            stckk=stckk[::-1]
            stckkk=stck[:-q]
            stck=stckkk+stckk
    elif cc==u"Ť":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.tanh(stck.pop()))
        elif(isinstance(stck[-1],list)):
            stck.append([tanh(x) for x in stck.pop()])
        else:
            stck.append(tanh(stck.pop()))
    elif cc==u"Ŧ":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.arctanh(stck.pop()))
        elif(isinstance(stck[-1],list)):
            stck.append([atanh(x) for x in stck.pop()])
        else:
            stck.append(atanh(stck.pop()))
    elif cc==u"ť":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.tan(stck.pop()))
        elif(isinstance(stck[-1],list)):
            stck.append([tan(x) for x in stck.pop()])
        else:
            stck.append(tan(stck.pop()))
    elif cc==u"ŧ":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.arctan(stck.pop()))
        elif(isinstance(stck[-1],list)):
            stck.append([atan(x) for x in stck.pop()])
        else:
            stck.append(atan(stck.pop()))
    elif cc==u"Ụ":
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(np.unique(stck.pop()))
        if(isinstance(stck[-1],list)):
            stck.append(getUnique((stck.pop())))
        else:
            stckk=stck
            stck=[]
            stck.append(getUnique((stckk)))
    elif cc==u"ʊ":
        stck.append("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    elif cc==u"Ž":
        qqq=stck.pop()
        qq=zip(stck.pop(),qqq)
        q=[]
        for j in range(len(qq)):
            q.append(qq[j][0])
            q.append(qq[j][1])
        stck.append(q)
    elif cc==u"π":
        stck.append(math.pi)
    elif cc==u"φ":
        stck.append((1+math.sqrt(5))/2)
    elif cc==u"≡":
        if(isinstance(stck[-1],np.ndarray)):
            q=stck.pop()
            stck.append((q==q[0]).all())
        elif(isinstance(stck[-1],list)):
            q=stck.pop()
            stck.append(all(x==q[0] for x in q))
        else:
            stckk=stck
            stck=[]
            stck.append(all(x==stckk[0] for x in stckk))
    elif cc==u"‼": #Double factorial
        q=stck.pop()
        if(isinstance(q,np.ndarray)):
            q=q.tolist()
        if(isinstance(q,list)):
            stck.append([factorial2(int(x)).tolist() for x in q])
        else:
            stck.append(factorial2(q))
    elif cc==u"ł": #loop to last instance of "`" if top of stack is not 0
        if(stck[-1]!=0):
            i=string.rfind(line,"`",0,i)
    elif cc==u"ŕ": #pop top of stack and do nothing
        stck.pop()
    elif cc==u"ǝ": #exp(x)
        q=stck.pop()
        if(isinstance(q,np.ndarray)):
            stck.append(np.exp(q))
        elif(isinstance(q,list)):
            stck.append([exp(x) for x in q])
        else:
            stck.append(exp(q))
    elif cc==u"⦋": #Get the xth entry in y
        q=stck.pop()
        if(isinstance(stck[-1],np.ndarray)):
            stck.append(stck.pop().tolist())
        stck.append(stck.pop()[int(q)])
    return stck,i


    #²³¹⁰⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉¼½¾⅐⅑⅒⅓⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞⅟°|!÷↑↓↕↔¬^«»≤≥<>=≠√∛∜∞∈~˜.%/+-*△⬠⬡∧∨⊼⊽⌊⌈⎶Å∀ḄƁÇČƇçč¢ḋ₫ĐéḞƑǤĦḤĨƖĮĻĽĹŁĿļɬɫṀɳỌꝎṔƤǷҎᑭ₽ṕƥṗƿϼҏŘɽɼɾɹʀʁŞŠŜŚşŝšŤŦťŧỤʊŽǂǁΣΠμϺπφ


def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def primeFactors(n):
    """Returns all the prime factors of a positive integer"""
    factors=[]
    d=2
    while n>1:
        while n%d==0:
            factors.append(d)
            n/=d
        d=d+1
        if d*d>n:
            if n>1:
                factors.append(int(n))
            break
    return factors

def getUnique(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    return b

def hamming(a):
    return sum(c1=='1' for c1 in bin(int(a)))

def fib(a):
    if a==0:
        return 1
    elif a==1:
        return 1
    else:
        i=1
        fi=1
        fj=1
        while i<a:
            fj+=fi
            fi=fj-fi
            i+=1
        return fj

def lucas(a):
    if a==0:
        return 2
    elif a==1:
        return 1
    else:
        i=1
        fi=2
        fj=1
        while i<a:
            fj+=fi
            fi=fj-fi
            i+=1
        return fj

def base(num,bb):
    digits=u"0123456789ABCDEFGHIJKLMNPOQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`-=[]\\;\',./~!@#$%^&*()_+{}|:\"<>?ĀĒḠĪŌS̄ŪǕȲĂĔĬŎŬÇḐȨĢḨĶĻŅŖŞŢÁĆÉǴÍḰĹḾŃÓṔŔŚÚǗẂÝŹḚḬṴḘṶḆḎH̱ḴḺṈṞṮẔƠƯŐŰÅŮĐǤĦƗŁƟŦƵĄĘĮǪŲÃẼĨÑÕŨṼỸØȘȚŒȂȆȊȎȒȖÞÄËḦÏÖT̈ÜẄẌŸǍČĎĚǦȞǏJ̌ǨĽŇǑŘŠŤǓǙŽȦĊḊĖḞĠḢİṀṄȮṖṘṠṪẆẊẎŻẠḄḌẸḤỊḲḶṂṆỌṚṢṬỤṾẈỴẒȀȄȈȌȐȔẢẺỈỎỦỶÀÈÌǸÒÙǛỲÂĈÊĜĤÎĴÔŜÛŴŶẐƏƆƎƔǶȠƜŊƢƦƱǷȜƷƧƐƼƄȢƁƇƊƑƓƖƘƝƤƮƩƬƲƳȤÆāēḡīōūǖȳăĕĭŏŭçḑȩģḩķļņŗşţáćéǵíḱĺḿńóṕŕśúǘẃýźḛḭṵḙṷḇḏẖḵḻṉṟṯẕơưőűåůẙƀđǥħɨłɵŧʉƶąęįǫųãẽĩñõũṽỹøșțœȃȇȋȏȓȗþäëḧïöẗüẅẍÿǎčďěǧȟǐǰǩľňǒřšťǔǚžȧḃċḋėḟġḣıṁṅȯṗṙṡṫẇẋẏżạḅḍẹḥịḳḷṃṇọṛṣṭụṿẉỵẓȁȅȉȍȑȕảẻỉỏủỷàèìǹòùǜẁỳâĉêĝĥîĵôŝûŵŷẑɔǝɣƕƞĸɯŋƣʀſʊʌƿȝʒƨɛƽƅ⁊ȣɓƈɗƒɠɦɩƙɲƥʠʈʃƭʋɖƴȥæ"
    st=u""
    while(num>0):
        st+=digits[num%bb]
        num/=bb
        num=int(num)
    return st[::-1]

def gcd(aa,bb):
    if(aa<bb):
        c=aa
        aa=bb
        bb=c
    while(bb!=0):
        t=bb
        bb=aa%bb
        aa=t
    return aa

def readasbase(st,bb):
    i=0
    while(st!=""):
        i*=bb
        c=st[0]
        if(c in ['0','1','2','3','4','5','6','7','8','9']):
            i+=int(c)
        elif(c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            i+=ord(c)-55
        elif(c in 'abcdefghijklmnopqrstuvwxyz'):
            i+=ord(c)-61
        st=st[1:]
    return i

def divisors(n):
    i=1
    divs=[]
    while(i<=n/2):
        if(n%i==0):
            divs.append(i)
            divs.append(n/i)
        i+=1
    return sorted(getUnique(divs))


def egcd(b,n):
    x0,x1,y0,y1=1, 0, 0, 1
    while n!=0:
        q, b, n = b//n, n, b%n
        x0, x1 = x1, x0-q*x1
        y0, y1 = y1, y0-q*y1
    return b,x0,y0

def mulinv(b,n):
    g, x, _ = egcd(b,n)
    if g==1:
        return x%n