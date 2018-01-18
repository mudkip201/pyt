# -*- coding: utf-8 -*-

'''
Created on Dec 22, 2017

@author: matthewcowen-green
'''

import interpreter3 as pyt
import numpy as np
from customlist import customlist
from collections import Counter

def parse(line):
    return pyt.parse(line,customlist())



'''
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
parse(u"9Đ")
parse(u"9ř5Ș")
parse(u"5_")
#parse(u"←←3Đ3Ș⇹Ĩ3Ș⇹Ĩ⇹Ř3ṕ")
parse(u"7ř‼")
parse(u"5ř7ɯ")'''

#parse(u"223+23*+^23+33**2+-23+2**223+^*")
#parse(u"2¹23+33**2+-23+2**223+^*")
#parse(u"2¹23+33**2+-23+2**2⁵*")
#parse(u"2¹59*2+-52**2⁵*")
#parse(u"2   Ʃ*")
#parse(u"99*ř1-")
#parse(u"221+2*^ř1-Đ!⇹2*1+‼/Ʃ2*21+21+22+*ř1+Đ11-^_⇹ĐĐ1-*⇹!*/Ʃ+*")
#parse(u"11+1+11+1+11+11++*ř1+Đ11-^_⇹ĐĐ1-*⇹!*/Ʃ+")
#parse(u"11+1+")
#parse(u"←ĐĐƖ=⇹0≥∧")
#parse(u"←ř²Ʃ")
#parse(u"←Đ2*√⌈ř△∈")
#parse(u"3←*4←*5←*++←-")
#parse(u"←Đř!∈")
#AABB -> ABBA -> ABAB -> ABABB -> ABBBA -> ABBBAA -> ABAABB -> ABABBA -> ABABC -> ABCBA -> ABCAB -> ABC[A,...,B] -> ABD -> ABDD -> ADDB -> ADBD -> AD{B*(1-D)} -> {B*(1-D)}AD -> {B*(1-D)}+{A*D}
#C=B-A
#D=C∈[A,...,B] (1 if true, 0 if false)
#parse(u"←Đ←Đ3Ș⇹Đ3ȘĐ4Ș3Ș-3Ș⇹Ř∈Đ3Ș⇹¢*3Ș⇹*+")
#parse(u"←1+3ĽĐƖ=")
#parse(u"59`⇹Đ+⇹1-ł+")
#parse(u"←1ŕ`Ś")
#parse(u"←1`ŕŚĐ9>łŕ9⇹-")
#parse(u"éǝ")
#C>B≥A
#A -> AB -> ABC -> CBA -> CBA^2 -> CA^2B -> CA^2B^2 -> B^2A^2C -> B^2A^2C^2 C^2A^2B^2
#parse(u"←←←Ş²⇹²↔²↔+=")
#parse(u"←²ĐƩ2/⇹∈")

#xn
#x^[0,1,2,3,...]-> [1,x,x^2,x^3,...] "<x><n>ř1-^"
#<-1>^[0,1,2,3,...] -> [1,-1,1,-1,...] "12-<n>ř1-^"
#[1,-x^2,x^4,-x^6,...] "<x><n>ř1-^²12-<n>ř1-^*"
#[1,x,x^2,x^3,...]^2*[1,-1,1,-1,...] -> [1,x^2,x^4,x^6,...]*[1,-1,1,-1,...] -> 1, -x^2, x^4, -x^6, ...
## xn -> xnn -> xnnn -> nnnx -> nxnn -> nxn[1,-1,1,-1,...] -> n[1,-1,1,-1,...]xn -> n[1,-x^2,x^4,-x^6,...]
#parse(u"←")
#xn -> xnn -> xnnn -> nnnx -> nxnn -> nxnn1 -> nxnn12 -> nxnn(-1) -> nxn(-1)n -> nxn(-1)[1,2,...,n] -> nxn(-1)[0,1,...,n-1] -> nxn[1,-1,1,-1,...]-> nx[1,-1,1,-1,...] -> nx[1,-1,1,-1,...]0 -> 0[1,-1,1,-1,...]xn -> 0[1,-1,1,-1,...]xnn -> nnx[1,-1,1,-1,...]0 -> nnx[1,-1,1,-1,...]04 -> n0[1,-1,1,-1,...]xn -> n0[1,-1,1,-1,...]x[1,2,...,n] -> n0[1,-1,1,-1,...]x[1,2,...,n]1 -> n0[1,-1,1,-1,...]x[0,1,...,n-1] -> n0[1,-1,1,-1,...][1,x,x^2,...,x^(n-1)] -> n0[1,-1,1,-1,...][1,x^2,x^4,...,x^(2n-2)] -> n0[1,-x^2,x^4,...,(-1)^(n-1)x^(2n-2)] -> n0[1,-x^2,x^4,...,(-1)^(n-1)x^(2n-2)]0 -> 0[1,-x^2,x^4,...,(-1)^(n-1)x^(2n-2)]0n -> 0[1,-x^2,x^4,...,(-1)^(n-1)x^(2n-2)]0[1,2,...,n] -> 0[1,-x^2,x^4,...,(-1)^(n-1)x^(2n-2)]0[1,2,...,n]1 -> 0[1,-x^2,x^4,...,(-1)^(n-1)x^(2n-2)]0[0,1,...,n-1] -> 0[1,-x^2,x^4,...,(-1)^(n-1)x^(2n-2)]0[0,1,...,n-1]2 -> 0[1,-x^2,x^4,...,(-1)^(n-1)x^(2n-2)]0[0,2,...,2n-2] -> 0
#parse(u"←←ĐĐ↔3Ș12-⇹ř1-^04Ș⇹ř1-^²*0↔ř1-2*!+/+Ʃ")
#np.ndarray([1,-1,1,-1,1])
#parse(u"5   this is a comment ²")
#6 -> 6 6 -> 6[1,2,3,6] -> 6[1,2,3,6][1,2,3,6] -> 6[1,2,3,6][1,2,3,6]1 -> 6[1,2,3,6][1,2,3,6]1 0 -> 6[1,2,3,6][1,2,3,6]1 -> 6[1,2,3,6][1,2,3,6]1 1 -> 6 [1,2,3,6]1 1[1,2,3,6] -> 6[1,2,3,6]1[1,2,3,6]1 -> 6[1,2,3,6]1 2 -> 6[1,2,3,6]1 2 2 -> 6[1,2,3,6]1 2 -> 6 2 1[1,2,3,6] -> 6 2 1[1,2,3,6]0 -> 0[1,2,3,6]1 2 6 -> 0[1,2,3,6]1 2 6 6 -> 6 6 2 1[1,2,3,6]0 -> 6 6 2 1[1,2,3,6]0 5 -> 6 0[1,2,3,6]1 2 6 -> 6 0[1,2,3,6]1 (1/3) -> 6 0[1,2,3,6]1 3 -> 6 0[1,2,3,6]1 -> 6 0[1,2,3,6]1 1 -> 6 0[1,2,3,6]2 -> 6 0[1,2,3,6]2 3 -> 6 2[1,2,3,6]0 -> 6 2[1,2,3,6] -> 6[1,2,3,6]2 -> 6[1,2,3,6]2 2 -> 2 2[1,2,3,6]6 -> 2 2[1,2,3,6]6 6 -> 6 6[1,2,3,6]2 2 -> 6 6 2 2[1,2,3,6]0 -> 6 6 2 2[1,2,3,6]0 -> 6 6 2 2[1,2,3,6]0 5 -> 6 0[1,2,3,6]2 2 6 -> 6 0[1,2,3,6]2 2 6 -> 6 0[1,2,3,6]2 6 2 -> 6 0[1,2,3,6]2 3 -> 6 0[1,2,3,6]2 9 -> 9 2[1,2,3,6]0 6 -> 9 2[1,2,3,6]0 6 6 -> 6 6 0[1,2,3,6]2 9 -> 6 9 2[1,2,3,6]0 6 -> 6[1,2,3,6]2 9 6 -> 6[1,2,3,6]2 False

#parse(u"←ĐðĐ1`Đ3Ș⇹⦋Đƥ3Ș0↔Đ↔5Ș/⅟ƖƤ1+3Șŕ⇹Đ4Ș⇹/²↔Đ↔5Ș↔≤łŕŕŕŕŕ")
#0[1,2,3,4,6,8,12,24][24,12,8,6,4,3,2,1]1 -> 0[1,2,3,4,6,8,12,24][24,12,8,6,4,3,2,1]1 1 -> 0[1,2,3,4,6,8,12,24]1 1[24,12,8,6,4,3,2,1] -> 0[1,2,3,4,6,8,12,24]1[24,12,8,6,4,3,2,1]1 ->
#parse(u"←ĐðĐ0↔/⅟ƖŽĐŁ₂20`ŕ3ȘĐ05Ș↔ŕ↔Đ4Ș⇹3Ș⦋ƥ⇹1+Ɩ3ȘĐ05Ș↔ŕ↔Đ4Ș⇹3Ș⦋ƤĐ3Ș1+ƖĐ3Ș<łĉ")

#parse(u"←ϼΠ")



#5 -> 5,5 -> 5,[1,2,3,4,5] -> 5,[1,3,6,10,15] -> [1,3,6,10,15],5 -> [1,3,6,10,15],5,5 -> 5,5,[1,3,6,10,15] -> 5,5,[1,3,6,10,15],[1,3,6,10,15] -> 5,5,[1,3,6,10,15],[1,3,6,10,15],0 -> 5,0,[1,3,6,10,15],[1,3,6,10,15],5 -> 5,0,[1,3,6,10,15],[1,1,0,0,0] -> 5,0,[1,3,0,0,0]
#parse(u"←Đř△⇹Đ↔Đ04Ș<*↑+-")


#0
#←←∧
#←←¬∧
#←
#←¬←∧
#←ŕ←
#←←⊻
#←←∨
#←←⊽
#←←⊙
#←ŕ←¬
#←¬←⊼
#←¬
#←←¬⊼
#←←⊼
#1



#parse(u"←Ḟ")
#parse(u"0`ĐḞƤ⁺ł")

#[A,B,C] -> [A,B,C],[A,B,C],[A,B,C] -> [A,B,C],[A,B,C],(A+B+C)/2
#parse(u"←ĐĐƩ₂-~Π8*⇹Π⇹/")
#parse(u"27*²0`ŕĐ₫+Đ₽¬ł")
#parse(u"←△Π")
#parse(u"←ř⁻ḞΠ")
#parse(u"←!ḋĐ5=*Ʃ")




#n -> n,n -> n,n,0,0
#←Đ00
#n,j,k,t0 -> t0,k,j,n -> t0,k,j,n,n -> t0,n,n,j,k -> t0,n,n,j,k,k,k,k -> t0,n,n,k,k,k,k,j -> t0,n,n,k,k,k,k,j,j,j ->t0,n,n,k,k,j,j,j,k,k -> k,k,j,j,j,k,k,n,n,t0 -> k,k,j,j,j,k,k,n,t0,n -> k,k,j,j,j,n,t0,n,k,k -> k,k,j,j,k,k,n,t0,n,j -> k,k,j,n,t0,n,k,k,j,j -> k,k,j,n,t0,n,k,j,j,k -> k,k,j,n,k,j,j,k,n,t0 -> k,k,j,n,k,j,t0,n,k,j -> k,k,j,n,k,j,t0,n,j,k -> k,k,j,n,k,j,t0,k,j,n -> n,j,k,t0,j,k,n,j,k,k
#n,j,k,t0,j,k,n,j,k,k -> n,j,k,t0,j,k,-(3k+3),k,j,n -> n,j,k,t0,j,k,(-3k-3),(n-j-k) -> n,j,k,t0,j,k,(-3k-3),(n-j-k),(n-j-k),(n-j-k),-1 -> n,j,k,t0,j,k,(-3k-3),(n-j-k),(n-j-k),-1^(n-j-k) -> n,j,k,t0,j,k,-1^(n-j-k),(n-j-k),(n-j-k),(-3k-3) -> n,j,k,t0,j,k,-1^(n-j-k),(n-j-k),(n-j-k),(3k+3) -> n,j,k,t0,j,k,-1^(n-j-k),(n-j-k),(3k+3),(2k+3+n-j) -> n,j,k,t0,j,k,-1^(n-j-k),(n-j-k),[3k+3,3k+3+1,...,2k+3+n-j] -> n,j,k,t0,j,k,-1^(n-j-k),(3k+3)*(3k+4)*...*(2k+3+n-j)/(n-j-k)! = n,j,k,t0,j,k,-1^(n-j-k),|Binomial(-3k-3,n-j-k)| -> n,j,k,t0,j,k,Binomial(-3k-3,n-j-k)-> n,j,k,t0,Binomial(-3k-3,n-j-k),k,j -> n,j,k,t0,Binom(-3k-3,n-j-k),k,j,j -> n,j,k,t0,Binom(...),k,j,2^j -> n,j,k,t0,Binom(...),k,2^j/j! -> n,j,k,t0,Binom(...),2^j/j!,k! -> n,j,k,t0+Binom(...)*(2^j/j!)*k!
#n,j,k,t0 -> n,j,t0,k -> n,j,t0,k,k -> n,j,k,k,t0 -> n,j,k,t0,k -> n,j,k,t0,k-1 -> n,j,k-1,t0,k
#⇹Đ3Ș⇹⁻3Ș

#n,j,k,t0 -> n,j,t0,k -> n,j,t0 -> n,t0,j -> n,t0,j,j -> n,t0,j,j,j -> n,j,j,j,t0 -> n,j,t0,j,j -> j,j,t0,j,n -> j,j,t0,j,n,n -> n,n,j,t0,j,j -> n,j,j,t0,j,n -> n,j,j,t0,n,j -> n,j,j,t0,n,j-1 -> n,j,j,t0,n-j+1 -> n,n-j+1,t0,j,j -> n,n-j+1,t0,j,j-1 -> n,j-1,j,t_0,n-j+1 -> n,j-1,j,n-j+1,t_0,j
#⇹ŕ⇹ĐĐ4Ș3Ș↔Đ↔5Ș⇹⁻-4Ș⁻4Ș3Ș
# ←Đ000`ŕ4ȘĐ4ȘĐĐĐ5ȘĐĐ5Ș↔⇹5Ș6Ș8Ș3Ș6Ș4Ș⇹3Ș↔⁺3*~4Ș-+~ĐĐ0⁻⇹^4ȘÅ+Đ3Ș+ŘΠ⇹!/*3ȘĐ2⇹^⇹!/⇹!**+⇹Đ3Ș⇹⁻3Șł⇹ŕ⇹ĐĐ4Ș3Ș↔Đ↔5Ș⇹⁻-4Ș⁻4Ș3Șłŕƥĉ

# n,j,k,t0 -> <?> -> n,j,k,t0,j,k,n,j,k,k
# n,j,k,t0 -> t0,k,j,n -> t0,k,j,n,n -> t0,n,n,j,k -> t0,n,n,j,k,k,k,k -> t0,n,n,k,k,k,k,j -> t0,n,n,k,k,k,k,j,j,j ->t0,n,n,k,k,j,j,j,k,k -> k,k,j,j,j,k,k,n,n,t0 -> k,k,j,j,j,k,k,n,t0,n -> k,k,j,j,j,n,t0,n,k,k -> k,k,j,j,k,k,n,t0,n,j -> k,k,j,n,t0,n,k,k,j,j -> k,k,j,n,t0,n,k,j,j,k -> k,k,j,n,k,j,j,k,n,t0 -> k,k,j,n,k,j,t0,n,k,j -> k,k,j,n,k,j,t0,n,j,k -> k,k,j,n,k,j,t0,k,j,n -> n,j,k,t0,j,k,n,j,k,k
# 4ȘĐ4ȘĐĐĐ5ȘĐĐ5Ș↔⇹5Ș6Ș8Ș3Ș6Ș4Ș⇹3Ș↔

#parse(u"Đ000`ŕ4ȘĐ4ȘĐĐĐ5ȘĐĐ5Ș↔⇹5Ș6Ș8Ș3Ș6Ș4Ș⇹3Ș↔⁺3*~4Ș-+~ĐĐ1~⇹^4ȘÅĐ3Ș⇹+⁻ŘΠ⇹↔Đ↔9Ș↔!3Ș⇹3Ș*⇹!÷*3ȘĐ2⇹^⇹!3Ș4Ș⇹÷*⇹Đ0≥*!*+⇹Đ3Ș⇹⁻3Șłŕ⇹ŕ↔Đ↔⇹3Ș⇹3ȘĐ3Ș⇹⁻Đ5Ș4Ș-3Ș⇹łŕ3Ș↔ŕƥĉ")

#n,j,t0 -> n,j-1,n-(j-1),t0,j
#n,j,t0 -> t0,j,n -> t0,j,n,n -> n,n,j,t0 -> n,n,t0,j -> n,j,t0,n -> n,j,n,t0 -> n,t0,n,j -> n,t0,n,j,j -> n,t0,j,j,n -> n,t0,j,n,j -> n,t0,j,n,j-1 -> n,t0,j,n,j-1,j-1 -> n,j-1,j-1,n,j,t0 -> n,j-1,t0,j,n,j-1 -> n,j-1,t0,j,n-j+1 -> ,n,j-1,n-j+1,j,t0 -> n,j-1,n-j+1,t0,j

#ŕ⇹ŕ⇹Đ↔⇹3Ș⇹3ȘĐ3Ș⇹⁻Đ5Ș4Ș-3Ș⇹łŕ3Ș↔!*ƥĉ

#(3k+3)*(3k+4)*...*(2k+3+n-j)/(n-j-k)!


#←Đ000`+4ȘĐ4ȘĐĐĐ5ȘĐĐ5Ș↔⇹5Ș6Ș8Ș3Ș6Ș4Ș⇹3Ș↔
#parse(u"5řᒆ")
#parse(u"5ř₊")
#parse(u"5ř₋Å")


#parse(u"←Đ!⇹řᒆ0↔0⇹`3Ș₋Å1⇹ɔ1=+⇹⁻łŕƥŕ")

#parse(u"←←Đř²⇹%∈")



#parse(u"3←`⇹ą²Ʃ⇹⁻ł")


#parse(u"←←ŘĐṗ*Ʃ")
#parse(u"←ᵱ")
#parse(u"é⁹₄←ϼ↑>")
#parse(u"89*9⁺²⁺9⁺²8+Đ9⁺²56++2⁵9²6+9⁺²56++92+²7-9⁺²8+9⁺²2⁵⁺áƇǰ")
#parse(u"3ř3*←⁻+26*%⁺")



#parse(u"←ĐĐĐ1⇹1⇹««⇹1⇹«⁻⇹3Ș⁻1⇹«⁺1⇹«*+⇹⁺1⇹«÷")
#parse(u"←ḋĐĐỤ⇹ɔΠ⇹ỤΠ*")

#parse(u"89*9⁺²⁺Đ7+ĐĐ3+7²5-2⁵9²6+6²⁺3*Đ3+Đ6-9⁺²2⁵⁺55^áƇǰ")
#parse(u"←29^Ĩ")
#parse(u"←Đ2*√⌈ř△>žŁ")
#parse(u"7ř↔₂Đƥ66ƥ5řĐƥ°π")



'''
parse(u"5⁰")
parse(u"5ř⁰")
parse(u"5¹")
parse(u"5ř¹")
parse(u"5²")
parse(u"5ř²")
parse(u"5³")
parse(u"5ř³")
parse(u"5⁴")
parse(u"5ř⁴")
parse(u"5⁵")
parse(u"5ř⁵")
parse(u"5⁶")
parse(u"5ř⁶")
parse(u"5⁷")
parse(u"5ř⁷")
parse(u"5⁸")
parse(u"5ř⁸")
parse(u"5⁹")
parse(u"5ř⁹")
parse(u"5₀")
parse(u"5ř₀")
parse(u"5₁")
parse(u"5ř₁")
parse(u"½⅓¼¾⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞⅐⅑⅒")
parse(u"5²⅟")
parse(u"2ᴇřƧ")
parse(u"93|")
parse(u"94|")
parse(u"5!")
parse(u"4³₀!")
parse(u"")
parse(u"")
parse(u"")
parse(u"")
parse(u"")
parse(u"")
parse(u"")
parse(u"")
parse(u"")
parse(u"")
parse(u"")
parse(u"")
parse(u"")
parse(u"")
parse(u"")
parse(u"")
parse(u"")
parse(u"")
parse(u"")
parse(u"")
parse(u"")
parse(u"")
parse(u"")
'''
#parse(u"2⁰2¹2²2³2⁴2⁵2⁶2⁷2⁸2⁹2₀2₁2₂2₃2₄2₅2₆2₇2₈2₉½⅓¼¾⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞⅐⅑⅒Ƨ235°95|93|5!52÷5ř↑5ř↓1¬25^25«25»25≤25≥25<25>25=25≠4√8∛4∜9˜~52%52/52+52-52*5△5⬠5⬡01∧01∨01⊼01⊽01⊻01⊙5₂⌊5₂⌈8₃⎶52‰5ř5ř×5~ÅáÁ5²ą9²ɓ")
#print(u"\u000a")
'''
    ←4≥
    ←6≥
    ←2≥
    ←8≥
    ←2%
    ←8≥
    ←2≥
    ←6≥
    ←4≥
    
    
    ←4≥
    ←6≥
    ←2≥
    ←8≥
    ←2%
    ←8≥
    ←2≥
    ←6≥
    ←4≥
'''
'''parse(u"""←4≥Đ6²⁺3**⇹¢2⁵*+
      2⁵
      ←6≥Đ6²⁺3**⇹¢2⁵*+
      2⁵
      ←2≥Đ6²⁺3**⇹¢2⁵*+
      1ᴇ
      ←8≥Đ6²⁺3**⇹¢2⁵*+
      2⁵
      ←2%Đ6²⁺3**⇹¢2⁵*+
      2⁵
      ←8≥Đ6²⁺3**⇹¢2⁵*+
      1ᴇ
      ←2≥Đ6²⁺3**⇹¢2⁵*+
      2⁵
      ←6≥Đ6²⁺3**⇹¢2⁵*+
      2⁵
      ←4≥Đ6²⁺3**⇹¢2⁵*+
      1ᴇ
      9△ĐĐĐĐ
      1ᴇ
      ←4≥Đ6²⁺3**⇹¢5«+
      2⁵
      ←6≥Đ6²⁺3**⇹¢5«+
      2⁵
      ←2≥Đ6²⁺3**⇹¢5«+
      1ᴇ
      ←8≥Đ6²⁺3**⇹¢5«+
      2⁵
      ←2%Đ6²⁺3**⇹¢5«+
      2⁵
      ←8≥Đ6²⁺3**⇹¢5«+
      1ᴇ
      ←2≥Đ6²⁺3**⇹¢5«+
      2⁵
      ←6≥Đ6²⁺3**⇹¢5«+
      2⁵
      ←4≥Đ6²⁺3**⇹¢5«+áƇǰ""")'''
#parse(u"0?ŕ5:ŕ2;2*:;")
#parse(u"←6²Ĩş3‰")
#parse(u"←ĐĐ3=?1:ŕĐ2⇹Ř03ȘĽ⅟⌊⁺3=0↔+  ;")
#parse(u"3ᴇ")
#parse(u"232°")
#parse(u"ɳᒆʀ")
#parse(u"řĐĐ↔*⇹ḶƖ⁺·")
#parse(u"ĐỤɔƩ")
#xx=u"ĐɔƩ"
#xxx=Counter(xx)
#parse(u"ĐỤ⇹ɔƩ")
#parse(u"ĐĐĐĐ≡")
#print(xxx[u"Đ"])
#print [xxx[x] for x in u"ĐɔƩ"]