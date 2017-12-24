# -*- coding: utf-8 -*-

'''
Created on Dec 22, 2017

@author: matthewcowen-green
'''

import pyt.interpreter as pyt

def parse(line):
    return pyt.parse(line,[])




parse(u"15Ř") #[1,2,3,4,5]
parse(u"15ŘƩ") #15
parse(u"12345Σ") #15
parse(u"15ŘΠ") #120
parse(u"12345Π") #120
parse(u"15Řµ") #3
parse(u"12345µ") #3
parse(u"15ŘṀ") #3
parse(u"12345Ṁ") #3
parse(u"123451Ϻ") #1
parse(u"15Ř²")
parse(u"15Ř³")
parse(u"15Ř¹")
parse(u"15Ř⁰")
parse(u"15Ř⁴")
parse(u"15Ř⁵")
parse(u"15Ř⁶")
parse(u"15Ř⁷")
parse(u"15Ř⁸")
parse(u"15Ř⁹")
parse(u"15Ř₀")
parse(u"15Ř₁")
parse(u"15Ř₂")
parse(u"15Ř₃")
parse(u"15Ř₄")
parse(u"15Ř₅")
parse(u"15Ř₆")
parse(u"15Ř₇")
parse(u"15Ř₈")
parse(u"15Ř₉")
parse(u"5⅟")
parse(u"12Ř6*5-")
parse(u"19ŘƧ")
parse(u"277°")
parse(u"299°")
parse(u"93|")
parse(u"9ř!")
parse(u"94÷")
parse(u"9ř↑")
parse(u"9ř↓")
#parse(u"←ř5*")
parse(u"9ř↕")
parse(u"8△")
parse(u"8⬠")
parse(u"8⬡")
parse(u"01∧")
parse(u"11v")
parse(u"10⊼")
parse(u"9√")
parse(u"8∛")
parse(u"4∜")
parse(u"43≠")
parse(u"43=")
parse(u"43>")
parse(u"43<")
parse(u"43≥")
parse(u"43≤")
parse(u"25»")
parse(u"41«")
parse(u"54^")
parse(u"9ř32/^")
parse(u"49ř²∈")
parse(u"∞5>")
parse(u"5~")
parse(u"9˜")
parse(u"5ř3%")
parse(u"93%")
parse(u"92/⌊")
parse(u"92/⌈")
parse(u"59*2+7/⎶")
parse(u"58*3+4‰")
parse(u"5ř4ř×")
parse(u"45*3+~Å")
parse(u"94*²Ƈ")
parse(u"43*7*ḋ")
parse(u"39*₫")
parse(u"26*Ḟ")
parse(u"29*47*Ǥ")
parse(u"39*Ħ")
#parse(u"←44*Ĩ")
parse(u"5řǰ")
parse(u"12345ǰ")
parse(u"54/Ɩ")
parse(u"25*²Ḷ")
parse(u"35*²Ḷ")
parse(u"é5^Ļ")
parse(u"93Ľ")
parse(u"459Π6Ĺ")
parse(u"45*řŁ")
parse(u"12345Ł")
parse(u"9Ŀ")
parse(u"8ļ")
parse(u"ɬ")
parse(u"ɫ")
parse(u"ɳ")
parse(u"98*5Ṕ")
parse(u"78*Ƿ")
parse(u"6!1-Ҏ")
parse(u"6!3-Ɩ₽")
parse(u"25*²1+ṗ")
parse(u"437Πϼ")
parse(u"ɫҏ")
parse(u"5řҏ")
parse(u"63₱")
parse(u"ɽ")
parse(u"59ɾ")
parse(u"ɹ")
parse(u"9ř²ʀ")
parse(u"9řŞ")
parse(u"9řŞş")
parse(u"43*!Ś")
parse(u"5řҏỤ")
parse(u"ʊ")
parse(u"5ř5řŽ")
parse(u"9ř0^≡")
parse(u"9ř≡")


parse(u"←←")