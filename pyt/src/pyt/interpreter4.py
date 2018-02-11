# -*- coding: utf-8 -*-

'''
    Created on Aug 11, 2017
    
    @author: matthewcowen-green
    
    
    STACK-BASED LANGUAGE
    '''


# Codepage: '⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉¼½¾⅐⅑⅒⅓⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞⅟Ƨ°|!÷↑↓←↕↔⇹¬^«»≤≥<>=≠√∛∜∞∈~˜%/+-*△⬠⬡∧∨⊼⊽⊻⊙⌊⌈⎶‰×ÅÁąáɐɓÇČƇĆçč¢ćĉɔĐðḋ₫éǝᴇḞƑᵮǤĦĨƖǰḶĻĽĹŁĿļɬłɫṀϺɯɳṔƤǷҎᑭ₽Ṗ₱ᒆṕƥṗƿϼҏᵱᵽŘɽɾɹʀřŕṛŞŠŜŚȘşŝšŤŦȚ⊤ťŧỤʊŽžµΠπƩφ≡‼`⦋⁺⁻₊₋0123456789⑴·?:;±\\'



import string
import math
from customlist import customlist

from operator import mul
from numpy import median, Infinity
import numpy as np
from scipy.stats import mode
from math import factorial, sqrt, floor, ceil, sin, cos, tan, cosh, sinh, tanh, acos, acosh, atan, atanh, asin, asinh, log, exp, pi
from itertools import count, islice, permutations
import random
from scipy.misc import factorial2
from collections import Counter


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
    #print(stck,cc,unicode(i))
    if(cc in string.digits):
        stck.append(int(cc))
        return stck,i
    elif cc==u"Σ" or cc==u"Ʃ":
        if(type(stck[-1]) is list):
            q=stck.pop()
            stck.append(sum(q))
        else:
            stckk=stck
            stck=customlist()
            stck.append(sum(stckk.data))
    elif cc==u"Π":
        if(isinstance(stck[-1],list)):
            stck.append(reduce(mul,stck.pop(),1))
        else:
            stckk=stck
            stck=customlist()
            stck.append(reduce(mul,stckk.data,1))
    elif cc==u"µ":
        if(isinstance(stck[-1],list)):
            q=stck.pop()
            stck.append(sum(q)*1./len(q))
        else:
            stckk=stck
            stck=customlist()
            stck.append(sum(stckk.data)*1./len(stckk.data))
    elif cc==u"Ṁ":
        if(isinstance(stck[-1],list)):
            stck.append(median(stck.pop()))
        else:
            stckk=stck
            stck=customlist()
            stck.append(median(stckk.data))
    elif cc==u"Ϻ":
        if(isinstance(stck[-1],list)):
            stck.append(mode(stck.pop())[0,0])
        else:
            stckk=stck
            stck=customlist()
            stck.append(mode(stckk.data)[0][0])
    elif cc==u"²":
        stck.append(ppowconst(stck.pop(),2))
    elif cc==u"³":
        stck.append(ppowconst(stck.pop(),3))
    elif cc==u"¹":
        stck.append(ppowconst(stck.pop(),11))
    elif cc==u"⁰":
        stck.append(ppowconst(stck.pop(),10))
    elif cc==u"⁴":
        stck.append(ppowconst(stck.pop(),4))
    elif cc==u"⁵":
        stck.append(ppowconst(stck.pop(),5))
    elif cc==u"⁶":
        stck.append(ppowconst(stck.pop(),6))
    elif cc==u"⁷":
        stck.append(ppowconst(stck.pop(),7))
    elif cc==u"⁸":
        stck.append(ppowconst(stck.pop(),8))
    elif cc==u"⁹":
        stck.append(ppowconst(stck.pop(),9))
    elif cc==u"₀":
        stck.append(pdivconst(stck.pop(),10))
    elif cc==u"₁":
        stck.append(pdivconst(stck.pop(),11))
    elif cc==u"₂":
        stck.append(pdivconst(stck.pop(),2))
    elif cc==u"₃":
        stck.append(pdivconst(stck.pop(),3))
    elif cc==u"₄":
        stck.append(pdivconst(stck.pop(),4))
    elif cc==u"₅":
        stck.append(pdivconst(stck.pop(),5))
    elif cc==u"₆":
        stck.append(pdivconst(stck.pop(),6))
    elif cc==u"₇":
        stck.append(pdivconst(stck.pop(),7))
    elif cc==u"₈":
        stck.append(pdivconst(stck.pop(),8))
    elif cc==u"₉":
        stck.append(pdivconst(stck.pop(),9))
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
        stck.append(pmultiplicateinv(stck.pop()))
    elif cc==u"Ƨ":
        if(isinstance(stck[-1],list)):
            stck.append(stck.pop()[::2])
        else:
            stckk=stck
            stck=customlist()
            stck.data=stckk[::2]
    elif cc==u"°":
        q=stck.pop()
        qq=stck.pop()
        qqq=stck.pop()
        stck.append(pmodpow(q,qq,qqq))
    elif cc==u"|":
        q=stck.pop()
        qq=stck.pop()
        stck.append(pdivides(qq,q))
    elif cc==u"!":
        stck.append(pfactorial(stck.pop()))
    elif cc==u"÷":
        q=stck.pop()
        qq=stck.pop()
        stck.append(pintdiv(qq,q))
    elif cc==u"↑":
        if(isinstance(stck[-1],list)):
            stck.append(max(stck.pop()))
        else:
            stckk=stck
            stck=customlist()
            stck.append(max(stckk.data))
    elif cc==u"↓":
        if(isinstance(stck[-1],list)):
            stck.append(min(stck.pop()))
        else:
            stckk=stck
            stck=customlist()
            stck.append(min(stckk.data))
    elif cc==u"←":
        q=raw_input().decode('utf-8')
        try:
            qq=float(q)
            if("." not in q):
                qq=int(q)
        except ValueError:
            qq=q
        if(q[0]=='[' and q[-1]==']'):
            stck.append(eval(q))
        else:
            stck.append(qq)
    #stck.append(raw_input())
    elif cc==u"↕":
        if(isinstance(stck[-1],list)):
            q=stck.pop()
            stck.append([min(q),max(q)])
        else:
            stckk=stck
            stck=customlist()
            stck.append([min(stckk.data),max(stckk.data)])
    elif cc==u"↔":
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
        stck.append(pnot(stck.pop()))
    elif cc==u"^":
        q=stck.pop()
        qq=stck.pop()
        stck.append(ppow(qq,q))
    elif cc==u"«":
        q=stck.pop()
        qq=stck.pop()
        stck.append(pbitshiftleft(qq,q))
    elif cc==u"»":
        q=stck.pop()
        qq=stck.pop()
        stck.append(pbitshiftright(qq,q))
    elif cc==u"≤":
        q=stck.pop()
        qq=stck.pop()
        stck.append(plteq(qq,q))
    elif cc==u"≥":
        q=stck.pop()
        qq=stck.pop()
        stck.append(pgteq(qq,q))
    elif cc==u"<":
        q=stck.pop()
        qq=stck.pop()
        stck.append(plessthan(qq,q))
    elif cc==u">":
        q=stck.pop()
        qq=stck.pop()
        stck.append(pgreaterthan(qq,q))
    elif cc==u"=":
        q=stck.pop()
        qq=stck.pop()
        stck.append(peq(qq,q))
    elif cc==u"≠":
        q=stck.pop()
        qq=stck.pop()
        stck.append(pneq(qq,q))
    elif cc==u"√":
        stck.append(ppowconst(stck.pop(),1./2))
    elif cc==u"∛":
        stck.append(ppowconst(stck.pop(),1./3))
    elif cc==u"∜":
        stck.append(ppowconst(stck.pop(),1./4))
    elif cc==u"∞":
        stck.append(Infinity)
    elif cc==u"∈":
        q=stck.pop()
        qq=stck.pop()
        if(isinstance(qq,list)):
            stck.append([x in q for x in qq])
        else:
            stck.append(qq in q)
    elif cc==u"~":
        stck.append(pnegate(stck.pop()))
    elif cc==u"˜": #unsigned two's-complement
        stck.append(ptwocomp(stck.pop()))
    elif cc==u"%":
        q=stck.pop()
        qq=stck.pop()
        stck.append(pmod(qq,q))
    elif cc==u"/":
        q=stck.pop()
        qq=stck.pop()
        stck.append(pdivide(qq,q))
    elif cc==u"+":
        q=stck.pop()
        qq=stck.pop()
        stck.append(pplus(qq,q))
    elif cc==u"-":
        q=stck.pop()
        qq=stck.pop()
        stck.append(pminus(qq,q))
    elif cc==u"*":
        q=stck.pop()
        qq=stck.pop()
        stck.append(pmultiply(qq,q))
    elif cc==u"△":
        stck.append(ptriangular(stck.pop()))
    elif cc==u"⬠":
        stck.append(ppentagonal(stck.pop()))
    elif cc==u"⬡":
        stck.append(phexagonal(stck.pop()))
    elif cc==u"∧":
        q=stck.pop()
        qq=stck.pop()
        stck.append(pand(qq,q))
    elif cc==u"∨":
        q=stck.pop()
        qq=stck.pop()
        stck.append(por(qq,q))
    elif cc==u"⊼": #NAND
        q=stck.pop()
        qq=stck.pop()
        stck.append(pnand(qq,q))
    elif cc==u"⊽": #NOR
        q=stck.pop()
        qq=stck.pop()
        stck.append(pnor(qq,q))
    elif cc==u"⊻": #XOR
        q=stck.pop()
        qq=stck.pop()
        stck.append(pxor(qq,q))
    elif cc==u"⊙": #XNOR
        q=stck.pop()
        qq=stck.pop()
        stck.append(pxnor(qq,q))
    elif cc==u"⌊":
        stck.append(pfloor(stck.pop()))
    elif cc==u"⌈":
        stck.append(pceil(stck.pop()))
    elif cc==u"⎶": #ROUND TO NEAREST INTEGER
        stck.append(pround(stck.pop()))
    elif cc==u"‰": #INTEGER DIVISION AND REMAINDER
        q=stck.pop()
        qq=stck.pop()
        stck.append(pintdiv(qq,q))
    elif cc==u"×":
        x=stck.pop()
        y=stck.pop()
        stck.append(np.transpose([np.tile(y, len(x)), np.repeat(x, len(y))]).tolist())
    elif cc==u"Å" or cc==u"Å":
        stck.append(pabs(stck.pop()))
    elif cc==u"Á":
        q=stck.pop()
        for x in q:
            stck.append(x)
    elif cc==u"ą": #convert number to array of digits
        stck.append(pdigitarray(stck.pop()))
    elif cc==u"á": #put contents of stack in an array
        stckk=stck.data
        stck=customlist()
        stck.append(stckk)
    elif cc==u"ɐ": #modifier character (for functions that can handle two arrays - (e.g., ɐ+ with [1,2,3] and [4,5,6] on the stack pushes [[1+4,1+5,1+6],[2+4,2+5,2+6],[3+4,3+5,3+6]]))
        i+=1
        cc=line[i]
        if cc==u"°":
            q=stck.pop()
            qq=stck.pop()
            qqq=stck.pop()
            if(isinstance(q,list)):
                if(isinstance(qq,list)):
                    if(isinstance(qqq,list)):
                        stck.append([[[pow(int(z),int(y),int(x)) for x in q] for y in qq] for z in qqq])
                    else:
                        stck.append([[pow(int(qqq),int(y),int(x)) for x in q] for y in qq])
                else:
                    stck.append([[pow(int(z),int(qq),int(x)) for x in q] for z in qqq])
            else:
                stck.append([[pow(int(z),int(y),int(q)) for y in qq] for z in qqq])
        elif cc==u"|":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[y%x==0 for x in q] for y in qq])
        elif cc==u"÷":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[y//x for x in q] for y in qq])
        elif cc==u"^":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[pow(y,x) for x in q] for y in qq])
        elif cc==u"«":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[y<<x for x in q] for y in qq])
        elif cc==u"»":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[y>>x for x in q] for y in qq])
        elif cc==u"≤":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[y<=x for x in q] for y in qq])
        elif cc==u"≥":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[y>=x for x in q] for y in qq])
        elif cc==u"<":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[y<x for x in q] for y in qq])
        elif cc==u">":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[y>x for x in q] for y in qq])
        elif cc==u"=":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[y==x for x in q] for y in qq])
        elif cc==u"≠":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[y!=x for x in q] for y in qq])
        elif cc==u"∈":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[y in x for x in q] for y in qq])
        elif cc==u"%":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[y%x for x in q] for y in qq])
        elif cc==u"/":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[y/x for x in q] for y in qq])
        elif cc==u"+":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[y+x for x in q] for y in qq])
        elif cc==u"-":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[y-x for x in q] for y in qq])
        elif cc==u"*":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[y*x for x in q] for y in qq])
        elif cc==u"∧":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[(y&x) for x in q] for y in qq])
        elif cc==u"∨":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[(y|x) for x in q] for y in qq])
        elif cc==u"⊻":
            q=stck.pop()
            qq=stck.pop()
            qqqq=[[max(y.bit_length(),x.bit_length()) for x in q] for y in qq]
            qqq=[[y|x for x in q] for y in qq]
            for j in range(len(qqq)):
                for k in range(len(qqq[j])):
                    qqq[j][k]=2**max(qqqq[j][k],qqq[j][k].bit_length())-qqq[j][k]-1
            stck.append(qqq)
        elif cc==u"⊼":
            q=stck.pop()
            qq=stck.pop()
            qqqq=[[max(y.bit_length(),x.bit_length()) for x in q] for y in qq]
            qqq=[[y&x for x in q] for y in qq]
            for j in range(len(qqq)):
                for k in range(len(qqq[j])):
                    qqq[j][k]=2**max(qqqq[j][k],qqq[j][k].bit_length())-qqq[j][k]-1
            stck.append(qqq)
        elif cc==u"⊽":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[(x^y) for x in q] for y in qq])
        elif cc==u"⊙":
            q=stck.pop()
            qq=stck.pop()
            qqq=[[y^x for x in q] for y in qq]
            qqqq=[[max(y.bit_length(),x.bit_length()) for x in q] for y in qq]
            for j in range(len(qqq)):
                for k in range(len(qqq[j])):
                    qqq[j][k]=2**max(qqqq[j][k],qqq[j][k].bit_length())-qqq[j][k]-1
            stck.append(qqq)
        elif cc==u"‰":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[[y//x,y%x] for x in q] for y in qq])
        elif cc==u"×":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[np.transpose([np.tile(y, len(x)), np.repeat(x, len(y))]).tolist() for x in q] for y in qq])
        elif cc==u"ć":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[factorial(y)/(factorial(x)*factorial(y-x)) for x in q] for y in qq])
        elif cc==u"ɔ":
            q=stck.pop()
            qq=stck.pop()
            qqq=[Counter(x) for x in q]
            stck.append([[qqq[j][y] for j in range(len(q))] for y in qq])
        elif cc==u"Ǥ":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[gcd(y,x) for x in q] for y in qq])
        elif cc==u"Ĩ":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[readasbase(unicode(y),int(x)) for x in q] for y in qq])
        elif cc==u"Ĺ":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[int(y)*int(x)/gcd(int(y),int(x)) for x in q] for y in qq])
        elif cc==u"Ľ":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[log(y,x) for x in q] for y in qq])
        elif cc==u"ɯ":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[mulinv(int(y),int(x)) for x in q] for y in qq])
        elif cc==u"Ṕ":
            q=stck.pop()
            qq=stck.pop()
            print([[unicode(base(int(y),int(x))) for x in q] for y in qq]+"\n")
        elif cc==u"ᑭ":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[1./2*y*((x-2)*y-(x-4)) for x in q] for y in qq])
        elif cc==u"₱":
            q=stck.pop()
            qq=stck.pop()
            stck.append([[factorial(y)/factorial(y-x) for x in q] for y in qq])
        elif cc==u"ṕ":
            q=stck.pop()
            qq=stck.pop()
            print([[unicode(base(int(y),int(x))) for x in q] for y in qq])
    elif cc==u"ɓ": #convert to binary string (less the 0b)
        stck.append(pbin(stck.pop()))
    elif cc==u"Ç":
        stck.append(pacosh(stck.pop()))
    elif cc==u"Č":
        stck.append(pcosh(stck.pop()))
    elif cc==u"Ƈ":
        stck.append(pchar(stck.pop()))
    elif cc==u"ç":
        stck.append(pacos(stck.pop()))
    elif cc==u"č":
        stck.append(pcos(stck.pop()))
    elif cc==u"¢":
        stck.append(pcomplement(stck.pop()))
    elif cc==u"ć":
        q=stck.pop()
        qq=stck.pop()
        stck.append(pncr(qq,q))
    elif cc==u"Ć":
        stck.append(pcatalan(stck.pop()))
    elif cc==u"ĉ":
        stck=customlist()
    elif cc==u"ɔ": #count occurrences of x in y
        q=stck.pop()
        qq=stck.pop()
        qqq=Counter(q)
        if(isinstance(qq,list)):
            stck.append([qqq[x] for x in qq])
        else:
            stck.append(qqq[qq])
    elif cc==u"ḋ":
        stck.append(pprimefactors(stck.pop()))
    elif cc==u"₫":
        stck.append(prevdigits(stck.pop()))
    elif cc==u"ð":
        stck.append(pdivisors(stck.pop()))
    elif cc==u"Đ": #duplicate item on top of stack
        q=stck.pop()
        stck.append(q)
        if(isinstance(q,list)):
            stck.append([x for x in q])
        else:
            stck.append(q)
    elif cc==u"é":
        stck.append(2.71828182845904523536028747135266249775724709369995)
    elif cc==u"ᴇ":
        stck.append(pe(stck.pop()))
    elif cc==u"Ḟ":
        stck.append(pfib(stck.pop()))
    elif cc==u"Ƒ": #flatten array
        stck.append(flatten(stck.pop()))
    elif cc==u"ᵮ":
        stck.append(pfloat(stck.pop()))
    elif cc==u"Ǥ":
        q=stck.pop()
        qq=stck.pop()
        stck.append(pgcd(qq,q))
    elif cc==u"Ħ":
        stck.append(phamming(stck.pop()))
    elif cc==u"Ĩ":
        q=stck.pop()
        qq=stck.pop()
        stck.append(preadasbase(qq,q))
    elif cc==u"Ɩ":
        stck.append(pint(stck.pop()))
    elif cc==u"ǰ":
        if(isinstance(stck[-1],list)):
            q=stck.pop()
            qq=[]
            for x in q:
                if not isinstance(x,str) or not isinstance(x,unicode):
                    qq.append(unicode(x))
                else:
                    qq.append(x)
            stck.append(u"".join(qq))
        else:
            stckk=stck
            stck=customlist()
            q=stckk.data
            qq=[]
            for x in q:
                if not isinstance(x,str) or not isinstance(x,unicode):
                    qq.append(unicode(x))
                else:
                    qq.append(x)
            stck.append(u"".join(qq))
    elif cc==u"Ḷ":
        stck.append(plog10(stck.pop()))
    elif cc==u"Ļ":
        stck.append(plog(stck.pop()))
    elif cc==u"Ľ":
        q=stck.pop()
        qq=stck.pop()
        stck.append(plogx(qq,q))
    elif cc==u"Ĺ":
        q=stck.pop()
        qq=stck.pop()
        stck.append(plcm(qq,q))
    elif cc==u"Ł":
        if(isinstance(stck[-1],list)):
            stck.append(len(stck.pop()))
        else:
            stckk=stck
            stck=customlist()
            stck.append(len(stckk))
    elif cc==u"Ŀ":
        stck.append(plucas(stck.pop()))
    elif cc==u"ļ":
        stck.append(plog2(stck.pop()))
    elif cc==u"ɬ":
        stck.append("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    elif cc==u"ɫ":
        stck.append("abcdefghijklmnopqrstuvwxyz")
    elif cc==u"ɯ": #modular inverse
        q=stck.pop()
        qq=stck.pop()
        stck.append(pmulinv(qq,q))
    elif cc==u"ɳ":
        stck.append("0123456789")
    elif cc==u"Ṕ":
        q=stck.pop()
        qq=stck.pop()
        print(ptobase(qq,q)+"\n")
    elif cc==u"Ƥ":
        print(unicode(stck.pop())+"\n")
    elif cc==u"Ƿ":
        print(pbin(stck.pop())+"\n")
    elif cc==u"Ҏ":
        stck.append(pdigitprod(stck.pop()))
    elif cc==u"ᑭ": #Polygonal number
        q=stck.pop()
        qq=stck.pop()
        stck.append(ppolygon(qq,q))
    elif cc==u"₽":
        q=stck.pop()
        if(isinstance(q,list)):
            stck.append(q==q[::-1])
        else:
            stck.append(unicode(q)==unicode(q)[::-1])
    elif cc==u"Ṗ":
        stck.append(pselfpow(stck.pop()))
    elif cc==u"ᒆ": #enumerates all partitions
        q=stck.pop()
        if(isinstance(q,unicode) or isinstance(q,str)):
            stck.append([''.join(p) for p in permutations(q)])
        else:
            stck.append(list([list(x) for x in permutations(q)]))
    elif cc==u"ṕ":
        q=stck.pop()
        qq=stck.pop()
        print(stck.append(ptobase(qq,q)))
    elif cc==u"ƥ":
        print(unicode(stck.pop()))
    elif cc==u"ṗ":
        stck.append(pisprime(stck.pop()))
    elif cc==u"ƿ":
        print(stck.append(pbin(stck.pop())))
    elif cc==u"ϼ":
        stck.append(puniqueprimefactors(stck.pop()))
    elif cc==u"ҏ":
        if(isinstance(stck[-1],list)):
            q=stck.pop()
            stck.append(q+q[::-1])
        elif(isinstance(stck[-1],str) or isinstance(stck[-1],unicode)):
            q=stck.pop()
            stck.append(q+q[::-1])
        else:
            stckk=stck
            stck.data=stckk.data+stckk.data.reverse()
    elif cc==u"ᵱ":
        q=stck.pop()
        if(isinstance(q,list)):
            stck.append([len(accel_asc(int(x))) for x in q])
        else:
            stck.append([len(accel_asc(int(q)))])
    elif cc==u"ᵽ":
        stck.append(pnprime(stck.pop()))
    elif cc==u"₱":
        q=stck.pop()
        qq=stck.pop()
        stck.append(pnpk(qq,q))
    elif cc==u"Ř":
        q=stck.pop()
        qq=stck.pop()
        stck.append(prange2ends(qq,q))
    elif cc==u"ɽ":
        stck.append(int(random.random()*(2**32)))
    elif cc==u"ɾ":
        q=int(stck.pop())
        qq=int(stck.pop())
        stck.append(prandrange(qq,q))
    elif cc==u"ɹ":
        stck.append(random.getrandbits(1))
    elif cc==u"ʀ":
        stck.append(random.choice(stck.pop()))
    elif cc==u"ṛ":
        stck.append(random.random())
    elif cc==u"ř":
        stck.append(prange(stck.pop()))
    elif cc==u"ʁ": #reduce array by operation (arr2[i]=oper(arr[i],arr[i+1])) of next character
        i+=1
        cc=line[i]
        if cc==u"|":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pdivides(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pdivides(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"÷":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pintdiv(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pintdiv(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"^":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(ppow(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(ppow(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"«":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pbitshiftleft(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pbitshiftleft(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"»":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pbitshiftright(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pbitshiftright(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"≤":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(plteq(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(plteq(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"≥":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pgteq(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pgteq(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"<":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(plessthan(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(plessthan(q[j],q[j+1]))
                stck.data=qq
        elif cc==u">":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pgreaterthan(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pgreaterthan(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"=":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(peq(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(peq(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"≠":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pneq(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pneq(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"%":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pmod(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pmod(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"/":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pdiv(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pdiv(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"+":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pplus(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pplus(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"-":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pminus(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pminus(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"*":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pmultiply(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pmultiply(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"∧":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pand(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pand(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"∨":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(por(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(por(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"⊼":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pnand(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pnand(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"⊽":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pnor(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pnor(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"⊻":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pxor(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pxor(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"⊙":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pxnor(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pxnor(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"‰":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pdivrem(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pdivrem(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"ć":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pncr(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pncr(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"Ǥ":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pgcd(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pgcd(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"Ĩ":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(preadasbase(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(preadasbase(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"Ľ":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(plogx(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(plogx(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"Ĺ":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(plcm(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pclm(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"ɯ":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pmulinv(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pmulinv(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"Ṕ":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    print(ptobase(q[j],q[j+1])+"\n")
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    print(ptobase(q[j],q[j+1])+"\n")
                stck.data=qq
        elif cc==u"ᑭ":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(ppolygon(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(ppolygon(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"ṕ":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    print(ptobase(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    print(ptobase(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"₱":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pnpk(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(pnpk(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"Ř":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(prange2ends(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(prange2ends(q[j],q[j+1]))
                stck.data=qq
        elif cc==u"ɾ":
            if isinstance(stck[-1],list):
                q=stck.pop()
                qq=[]
                for j in range(len(q)-1):
                    qq.append(prandrange(q[j],q[j+1]))
                stck.append(qq)
            else:
                q=stck.data
                qq=[]
                for j in range(len(q)-1):
                    qq.append(prandrange(q[j],q[j+1]))
                stck.data=qq
    elif cc==u"Ş":
        if(isinstance(stck[-1],list)):
            stck.append(sorted(stck.pop())[::-1])
        else:
            stck.data=sorted(stck.data)[::-1]
    elif cc==u"Š":
        stck.append(psinh(stck.pop()))
    elif cc==u"Ŝ":
        stck.append(pasinh(stck.pop()))
    elif cc==u"Ś":
        stck.append(psumdigits(stck.pop()))
    elif cc==u"ş" or cc==u"ş":
        if(isinstance(stck[-1],list)):
            stck.append(sorted(stck.pop()))
        else:
            stck.data=sorted(stck.data)
    elif cc==u"ŝ":
        stck.append(pasin(stck.pop()))
    elif cc==u"š":
        stck.append(psin(stck.pop()))
    elif cc==u"Ș": # Reverse last k items (in stack if not list)
        q=stck.pop()
        if(isinstance(stck[-1],list)):
            qq=stck.pop()
            qqq=qq[-q:]
            stck.append(qq[0:-q]+qqq[::-1])
        else:
            stckk=stck[-q:]
            stckk=stckk[::-1]
            stckkk=stck[:-q]
            stck.data=stckkk+stckk
    elif cc==u"Ť":
        stck.append(ptanh(stck.pop()))
    elif cc==u"Ŧ":
        stck.append(patanh(stck.pop()))
    elif cc==u"Ț":
        stck.append(peulertot(stck.pop()))
    elif cc==u"⊤":
        stck.append(np.transpose(np.array(stck.pop())).tolist())
    elif cc==u"ť":
        stck.append(ptan(stck.pop()))
    elif cc==u"ŧ":
        stck.append(patan(stck.pop()))
    elif cc==u"Ụ":
        if(isinstance(stck[-1],list)):
            stck.append(getUnique(stck.pop()))
        elif(isinstance(stck[-1],unicode) or isinstance(stck[-1],str)):
            stck.append(getUnique(stck.pop()))
        else:
            stckk=stck
            stck=customlist()
            stck.append(getUnique(stckk.data))
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
    elif cc==u"ž": #Remove zeroes from list
        q=stck.pop()
        stck.append([x for x in q if x!=0])
    elif cc==u"π":
        stck.append(pi)
    elif cc==u"φ":
        stck.append((1+sqrt(5))/2)
    elif cc==u"≡":
        if(isinstance(stck[-1],list)):
            q=stck.pop()
            stck.append(all(x==q[0] for x in q))
        else:
            stckk=stck
            stck=customlist()
            stck.append(all(x==stckk[0] for x in stckk.data))
    elif cc==u"‼": #Double factorial
        stck.append(pdoublefac(stck.pop()))
    elif cc==u"ł": #loop to last instance of "`" if top of stack is not 0
        if(stck[-1]!=0):
            i=string.rfind(line,"`",0,i)
    elif cc==u"ŕ": #pop top of stack and do nothing
        stck.pop()
    elif cc==u"ǝ": #exp(x)
        stck.append(pexpon(stck.pop()))
    elif cc==u"⦋": #Get the xth entry in y
        q=stck.pop()
        qq=stck.pop()
        stck.append(qq[int(q)])
    elif cc==u"⁺":
        stck.append(pincrement(stck.pop()))
    elif cc==u"⁻":
        stck.append(pdecrement(stck.pop()))
    elif cc==u"₋":
        q=stck.pop()
        stck.append([j-k for k, j in zip(q[:-1], q[1:])])
    elif cc==u"₊":
        q=stck.pop()
        stck.append([j+k for k, j in zip(q[:-1], q[1:])])
    elif cc==u"⑴":
        stck.append([1 for j in range(int(stck.pop()))])
    elif cc==u"·": #Dot product
        q=stck.pop()
        qq=stck.pop()
        stck.append(np.dot(np.array(q),np.array(qq)).tolist())
    elif cc==u"?":
        if(stck[-1]==0):
            i=string.find(line,":",i)
    elif cc==u":":
        i=string.find(line,";",i)
    elif cc==u"±":
        stck.append(np.sign(stck.pop()).tolist())
    elif cc==u"\\":
        stck.append(psetdifference(stck.pop(),stck.pop()))
    return stck,i


def pdivconst(q,const):
    if isinstance(q,list):
        return [pdivconst(q2,const) for q2 in q]
    return  q/const


def pmultiplicateinv(q):
    if isinstance(q,list):
        return [pmultiplicateinv(qq) for qq in q]
    return 1./q


def pmodpow(q,qq,qqq):
    if isinstance(qq,list):
        if isinstance(q,list):
            if isinstance(qqq,list):
                return [pmodpow(qqq[i],qq[i],q[i]) for i in range(min(len(qq),len(q),len(qqq)))]
            return [pmodpow(qqq,qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        if isinstance(qqq,list):
            return [pmodpow(qqq[i],qq[i],q) for i in range(min(len(qq),len(qqq)))]
        return [pmodpow(qqq,qq2,q) for qq2 in qq]
    if isinstance(q,list):
        if isinstance(qqq,list):
            return [pmodpow(qqq[i],qq,q[i]) for i in range(min(len(q),len(qqq)))]
        return [pmodpow(qqq,qq,q2) for q2 in q]
    if isinstance(qqq,list):
        return [pmodpow(qqq2,qq,q) for qqq2 in qqq]
    return [pow(int(qqq),int(qq),int(q))]

def pdivides(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [pdivides(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [pdivides(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [pdivides(qq,q2) for q2 in q]
    return qq%q==0

def pfactorial(q):
    if isinstance(q,list):
        return [pfactorial(qq) for qq in q]
    return factorial(int(q))

def pintdiv(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [pintdiv(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [pintdiv(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [pintdiv(qq,q2) for q2 in q]
    return int(qq//q)

def pnot(q):
    if isinstance(q,list):
        return [pnot(qq) for qq in q]
    return not(q)

def ppow(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [ppow(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [ppow(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [ppow(qq,q2) for q2 in q]
    if isinstance(qq,int) and isinstance(q,int):
        return qq**q
    return pow(qq,q)

def pbitshiftleft(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [pbitshiftleft(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [pbitshiftleft(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [pbitshiftleft(qq,q2) for q2 in q]
    return qq<<int(q)

def pbitshiftright(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [pbitshiftright(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [pbitshiftright(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [pbitshiftright(qq,q2) for q2 in q]
    return qq>>int(q)

def plteq(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [plteq(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [plteq(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [plteq(qq,q2) for q2 in q]
    return qq<=q

def pgteq(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [pgteq(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [pgteq(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [pgteq(qq,q2) for q2 in q]
    return qq>=q

def plessthan(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [plessthan(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [plessthan(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [plessthan(qq,q2) for q2 in q]
    return qq<q

def pgreaterthan(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [pgreaterthan(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [pgreaterthan(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [pgreaterthan(qq,q2) for q2 in q]
    return qq>q

def peq(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [peq(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [peq(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [peq(qq,q2) for q2 in q]
    return qq==q

def pneq(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [pneq(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [pneq(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [pneq(qq,q2) for q2 in q]
    return qq==q

def ppowconst(q,const):
    if isinstance(q,list):
        return [ppowconst(q2,const) for q2 in q]
    return pow(q,const)

def pnegate(q):
    if isinstance(q,list):
        return [pnegate(qq) for qq in q]
    return -q

def ptwocomp(q):
    if isinstance(q,list):
        return [ptwocomp(qq) for qq in q]
    return 2**int(q.bit_length())-int(q)

def pmod(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [pmod(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [pmod(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [pmod(qq,q2) for q2 in q]
    return qq%q

def pdivide(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [pdivide(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [pdivide(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [pdivide(qq,q2) for q2 in q]
    return qq/q

def pplus(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [pplus(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [pplus(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [pplus(qq,q2) for q2 in q]
    return qq+q

def pminus(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [pminus(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [pminus(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [pminus(qq,q2) for q2 in q]
    return qq-q

def pmultiply(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [pmultiply(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [pmultiply(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [pmultiply(qq,q2) for q2 in q]
    return qq*q

def ptriangular(q):
    if isinstance(q,list):
        return [ptriangular(qq) for qq in q]
    return (int(q)**2+int(q))/2

def ppentagonal(q):
    if isinstance(q,list):
        return [ppentagonal(qq) for qq in q]
    return (3*int(q)**2-int(q))/2

def phexagonal(q):
    if isinstance(q,list):
        return [phexagonal(qq) for qq in q]
    return 2*int(q)**2-int(q)

def pand(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [pand(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [pand(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [pand(qq,q2) for q2 in q]
    return int(qq)&int(q)

def por(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [por(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [por(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [por(qq,q2) for q2 in q]
    return int(qq)|int(q)

def pnand(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [pnand(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [pnand(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [pnand(qq,q2) for q2 in q]
    q=int(q)
    qq=int(qq)
    return 2**max(q.bit_length(),qq.bit_length())-(qq&q)-1

def pnor(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [pnor(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [pnor(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [pnor(qq,q2) for q2 in q]
    return 2**(int(q)|int(qq)).bit_length()-(int(q)|int(qq))-1

def pxor(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [pxor(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [pxor(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [pxor(qq,q2) for q2 in q]
    return int(qq)^int(q)

def pxnor(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [(qq,q2) for q2 in q]
    q=int(q)
    qq=int(qq)
    qqq=qq^q
    return 2**max(q.bit_length(),qq.bit_length(),qqq.bit_length())-qqq-1

def pfloor(q):
    if isinstance(q,list):
        return [pfloor(qq) for qq in q]
    return floor(q)

def pceil(q):
    if isinstance(q,list):
        return [pceil(qq) for qq in q]
    return ceil(q)

def pround(q):
    if isinstance(q,list):
        return [pround(qq) for qq in q]
    return round(q)

def pdivrem(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [pdivrem(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [pdivrem(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [pdivrem(qq,q2) for q2 in q]
    return [qq//q,qq%q]

def pabs(q):
    if isinstance(q,list):
        return [pabs(qq) for qq in q]
    return abs(q)


def pdigitarray(q):
    if isinstance(q,list):
        return [pdigitarray(qq) for qq in q]
    return [int(x) for x in list(str(int(q)))]

def pcosh(q):
    if isinstance(q, list):
        return [pcosh(q) for qq in q]
    return cosh(q)

def pacosh(q):
    if isinstance(q,list):
        return [pacosh(qq) for qq in q]
    return acosh(q)

def pchar(q):
    if isinstance(q,list):
        return [pchar(qq) for qq in q]
    return unichr(int(q))

def pcos(q):
    if isinstance(q, list):
        return [pcos(q) for qq in q]
    return cos(q)

def pacos(q):
    if isinstance(q,list):
        return [pacos(qq) for qq in q]
    return acos(q)

def pcomplement(q):
    if isinstance(q,list):
        return [pcomplement(qq) for qq in q]
    return 1-q

def pncr(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [pncr(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [pncr(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [pncr(qq,q2) for q2 in q]
    return factorial(int(qq))/(factorial(int(q))*(factorial(int(qq)-int(q))))

def pcatalan(q):
    if isinstance(q,list):
        return [pcatalan(qq) for qq in q]
    return factorial(2*int(q))/(factorial(int(q)+1)*factorial(int(q)))

def pdivisors(q):
    if isinstance(q,list):
        return [pdivisors(qq) for qq in q]
    return divisors(int(q))

def pe(q):
    if isinstance(q,list):
        return [pe(qq) for qq in q]
    return pow(10,q)

def pfib(q):
    if isinstance(q,list):
        return [pfib(qq) for qq in q]
    return fib(int(q))

def pfloat(q):
    if isinstance(q,list):
        return [pfloat(qq) for qq in q]
    return float(q)

def pgcd(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [pgcd(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [pgcd(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [pgcd(qq,q2) for q2 in q]
    return gcd(int(qq),int(q))

def phamming(q):
    if isinstance(q,list):
        return [phamming(qq) for qq in q]
    return hamming(int(q))

def preadasbase(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [preadasbase(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [preadasbase(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [preadasbase(qq,q2) for q2 in q]
    return readasbase(unicode(qq),int(q))

def pint(q):
    if isinstance(q,list):
        return [pint(qq) for qq in q]
    return int(q)

def plog(q):
    if isinstance(q,list):
        return [plog(qq) for qq in q]
    return log(q)

def plogx(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [plogx(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [plogx(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [plogx(qq,q2) for q2 in q]
    return log(qq,q)

def plog10(q):
    if isinstance(q,list):
        return [plog10(qq) for qq in q]
    return log(q,10)

def plcm(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [plcm(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [plcm(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [plcm(qq,q2) for q2 in q]
    q=int(q)
    qq=int(qq)
    return qq*q/gcd(qq,q)

def plucas(q):
    if isinstance(q,list):
        return [plucas(qq) for qq in q]
    return lucas(int(q))

def plog2(q):
    if isinstance(q,list):
        return [plog2(qq) for qq in q]
    return log(q,2)

def pmulinv(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [pmulinv(qq[i],q[i]) for i in range(min(len(q),len(qq)))]
        return [pmulinv(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [pmulinv(qq,q2) for q2 in q]
    return mulinv(int(qq),int(q))

def pdigitprod(q):
    if isinstance(q,list):
        return [pdigitprod(qq) for qq in q]
    w=str(int(q))
    k=1
    for j in w:
        k*=int(j)
    return k

def ppolygon(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [ppolygon(qq[j],q[j]) for j in range(min(len(qq),len(q)))]
        return [ppolygon(qq2,q) for qq2 in q]
    if isinstance(q,list):
        return [ppolygon(qq,q2) for q2 in q]
    return 1./2*int(qq)*((int(q)-2)*int(qq)-(int(q)-4))

def pselfpow(q):
    if isinstance(q,list):
        return [pselfpow(qq) for qq in q]
    return pow(q,q)

def ptobase(qq,q):
    if isinstance(qq,list):
        if isinstance(q,list):
            return [ptobase(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [ptobase(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [ptobase(qq,q2) for q2 in q]
    return base(int(qq),int(q))

def pisprime(q):
    if isinstance(q,list):
        return [pisprime(qq) for qq in q]
    return isPrime(int(q))

def pbin(q):
    if isinstance(q,list):
        return [pbin(qq) for qq in q]
    return (""+bin(int(q)))[2:]


def pnpk(qq,q):
    if isinstance(qq,list):
        if(isinstance(q,list)):
            return [pnpk(qq[i],q[i]) for i in range(min(len(qq),len(q)))]
        return [pnpk(qq2,q) for qq2 in qq]
    if isinstance(q,list):
        return [pnpk(qq,q2) for q2 in q]
    return factorial(int(qq))/factorial(int(qq)-int(q))

def pnprime(q):
    if(isinstance(q,list)):
        return [pnprime(q2) for q2 in q]
    qq=[2]
    n=3
    while(len(qq)<int(q)):
        for p in qq:
            if n%p==0:
                break
        else:
            qq.append(n)
        n+=2
    return qq[-1]

def puniqueprimefactors(q):
    if isinstance(q,list):
        return [puniqueprimefactors(qq) for qq in q]
    return getUnique(primeFactors(int(q)))

def prange2ends(qq,q):
    if isinstance(q,list):
        if isinstance(qq,list):
            return [prange2ends(qq[i],q[i]) for i in range(min(len(q),len(qq)))]
        return [prange2ends(qq,q2) for q2 in q]
    if isinstance(qq,list):
        return [prange2ends(qq2,q) for qq2 in qq]
    return list(range(int(qq),int(q)+1))

def prandrange(qq,q):
    if isinstance(q,list):
        if isinstance(qq,list):
            return [prandrange(qq[i],q[i]) for i in range(min(len(q),len(qq)))]
        return [prandrange(qq,q2) for q2 in q]
    if isinstance(qq,list):
        return [prandrange(qq2,q) for qq2 in qq]
    return random.randrange(qq,q)

def prange(q):
    if isinstance(q,list):
        return [prange(qq) for qq in q]
    return range(1,int(q)+1)

def psumdigits(q):
    if isinstance(q,list):
        return [psumdigits(qq) for qq in q]
    w=str(int(q))
    k=0
    for j in w:
        k+=int(j)
    return k

def pasinh(q):
    if isinstance(q,list):
        return [pasin(qq) for qq in q]
    return asin(q)

def psinh(q):
    if isinstance(q,list):
        return [psin(qq) for qq in q]
    return sin(q)

def pasin(q):
    if isinstance(q,list):
        return [pasin(qq) for qq in q]
    return asin(q)

def psin(q):
    if isinstance(q,list):
        return [psin(qq) for qq in q]
    return sin(q)

def ptanh(q):
    if isinstance(q,list):
        return [ptanh(qq) for qq in q]
    return tanh(q)

def patanh(q):
    if isinstance(q,list):
        return [patanh(qq) for qq in q]
    return atanh(q)

def peulertot(q):
    if isinstance(q,list):
        return [peulertot(qq) for qq in q]
    return eulertot(int(q))

def ptan(q):
    if isinstance(q, list):
        return [ptan(q) for qq in q]
    return tan(q)

def patan(q):
    if isinstance(q,list):
        return [patan(qq) for qq in q]
    return atan(q)

def pdoublefac(q):
    if isinstance(q,list):
        return [pdoublefac(qq) for qq in q]
    if isinstance(q,int):
        k=1
        kk=q
        while(kk>0):
            k*=kk
            kk-=2
        return k
    return np.asscalar(factorial2(int(q)))

def pexpon(q):
    if isinstance(q,list):
        return [pexpon(qq) for qq in q]
    return exp(q)


def pincrement(q):
    if isinstance(q,list):
        return [pincrement(qq) for qq in q]
    return q+1


def pdecrement(q):
    if isinstance(q,list):
        return [pdecrement(qq) for qq in q]
    return q-1

def pprimefactors(q):
    if isinstance(q,list):
        return [pprimefactors(qq) for qq in q]
    return primeFactors(int(q))

def prevdigits(q):
    if isinstance(q,list):
        return [prevdigits(qq) for qq in q]
    return int((""+str(int(q)))[::-1])

def psetdifference(q,qq):
    if isinstance(q,list):
        qqq=[]
        for qq2 in qq:
            if qq2 not in q:
                qqq.append(qq2)
        return qqq
    qqq=[]
    for qq2 in qq:
        if qq2!=q:
            qqq.append(qq2)
    return qqq


def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def primeFactors(n):
    """Returns all the prime factors of a positive integer"""
    if(n==1):
        return [1]
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
    digits=u"0123456789ABCDEFGHIJKLMNPOQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`-=[]\\;\',./~!@#$%^&*()_+{}|:\"<>?ĀĒḠĪŌS̄ŪǕȲĂĔĬŎŬÇḐȨĢḨĶĻŅŖŞŢÁĆÉǴÍḰĹḾŃÓṔŔŚÚǗẂÝŹḚḬṴḘṶḆḎH̱ḴḺṈṞṮẔƠƯŐŰÅŮĐǤĦƗŁƟŦƵĄĘĮǪŲÃẼĨÑÕŨṼỸØȘȚŒȂȆȊȎȒȖÞÄËḦÏÖT̈ÜẄẌŸǍČĎĚǦȞǏJ̌ǨĽŇǑŘŠŤǓǙŽȦĊḊĖḞĠḢİṀṄȮṖṘṠṪẆẊẎŻẠḄḌẸḤỊḲḶṂṆỌṚṢṬỤṾẈỴẒȀȄȈȌȐȔẢẺỈỎỦỶÀÈÌǸÒÙǛỲÂĈÊĜĤÎĴÔŜÛŴŶẐƏƆƎƔǶȠƜŊƢƦƱǷȜƷƧƐƼƄȢƁƇƊƑƓƖƘƝƤƮƩƬƲƳȤÆāēḡīōūǖȳăĕĭŏŭçḑȩģḩķļņŗşţáćéǵíḱĺḿńóṕŕśúǘẃýźḛḭṵḙṷḇḏẖḵḻṉṟṯẕơưőűåůẙƀđǥħɨłɵŧʉƶąęįǫųãẽĩñõũṽỹøșțœȃȇȋȏȓȗþäëḧïöẗüẅẍÿǎčďěǧȟǐǰǩľňǒřšťǔǚžȧḃċḋėḟġḣıṁṅȯṗṙṡṫẇẋẏżạḅḍẹḥịḳḷṃṇọṛṣṭụṿẉỵẓȁȅȉȍȑȕảẻỉỏủỷàèìǹòùǜẁỳâĉêĝĥîĵôŝûŵŷẑɔǝɣƕƞĸɯŋƣʀſʊʌƿȝʒƨɛƽƅ⁊ȣɓƈɗƒɠɦɩƙɲƥʠʈʃƭʋɖƴȥæ⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉¼½¾⅐⅑⅒⅓⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞⅟Ƨ°÷↑↓←↕↔⇹¬«»≤≥≠√∛∜∞∈˜△⬠⬡∧∨⊼⊽⊻⊙⌊⌈⎶‰×¢ð₫ᴇᵮĿɬɫϺɳҎᑭ₽₱ᒆϼҏᵱɽɾɹʀ⊤µΠπƩφ≡‼⦋⁺⁻₊₋⑴·±"
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
    digits=u"0123456789ABCDEFGHIJKLMNPOQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`-=[]\\;\',./~!@#$%^&*()_+{}|:\"<>?ĀĒḠĪŌS̄ŪǕȲĂĔĬŎŬÇḐȨĢḨĶĻŅŖŞŢÁĆÉǴÍḰĹḾŃÓṔŔŚÚǗẂÝŹḚḬṴḘṶḆḎH̱ḴḺṈṞṮẔƠƯŐŰÅŮĐǤĦƗŁƟŦƵĄĘĮǪŲÃẼĨÑÕŨṼỸØȘȚŒȂȆȊȎȒȖÞÄËḦÏÖT̈ÜẄẌŸǍČĎĚǦȞǏJ̌ǨĽŇǑŘŠŤǓǙŽȦĊḊĖḞĠḢİṀṄȮṖṘṠṪẆẊẎŻẠḄḌẸḤỊḲḶṂṆỌṚṢṬỤṾẈỴẒȀȄȈȌȐȔẢẺỈỎỦỶÀÈÌǸÒÙǛỲÂĈÊĜĤÎĴÔŜÛŴŶẐƏƆƎƔǶȠƜŊƢƦƱǷȜƷƧƐƼƄȢƁƇƊƑƓƖƘƝƤƮƩƬƲƳȤÆāēḡīōūǖȳăĕĭŏŭçḑȩģḩķļņŗşţáćéǵíḱĺḿńóṕŕśúǘẃýźḛḭṵḙṷḇḏẖḵḻṉṟṯẕơưőűåůẙƀđǥħɨłɵŧʉƶąęįǫųãẽĩñõũṽỹøșțœȃȇȋȏȓȗþäëḧïöẗüẅẍÿǎčďěǧȟǐǰǩľňǒřšťǔǚžȧḃċḋėḟġḣıṁṅȯṗṙṡṫẇẋẏżạḅḍẹḥịḳḷṃṇọṛṣṭụṿẉỵẓȁȅȉȍȑȕảẻỉỏủỷàèìǹòùǜẁỳâĉêĝĥîĵôŝûŵŷẑɔǝɣƕƞĸɯŋƣʀſʊʌƿȝʒƨɛƽƅ⁊ȣɓƈɗƒɠɦɩƙɲƥʠʈʃƭʋɖƴȥæ⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉¼½¾⅐⅑⅒⅓⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞⅟Ƨ°÷↑↓←↕↔⇹¬«»≤≥≠√∛∜∞∈˜△⬠⬡∧∨⊼⊽⊻⊙⌊⌈⎶‰×¢ð₫ᴇᵮĿɬɫϺɳҎᑭ₽₱ᒆϼҏᵱɽɾɹʀ⊤µΠπƩφ≡‼⦋⁺⁻₊₋⑴·±"
    i=0
    while(st!=u""):
        i*=bb
        c=st[0]
        p=digits.find(c)
        if(p!=-1):
            i+=p
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


def accel_asc(n):
    return set(accel_asc_yield(n))


def accel_asc_yield(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield tuple(a[:k + 2])
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield tuple(a[:k + 1])

def eulertot(n):
    y=n
    for i in getUnique(primeFactors(n)):
        y-=y/i
    return int(y)


def flatten(lst):
    return sum( (x.flatten().tolist() if isinstance(x, np.ndarray) else [x] if not isinstance(x, list) else flatten(x) for x in lst), [] )