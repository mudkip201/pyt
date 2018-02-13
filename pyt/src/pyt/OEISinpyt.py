# -*- coding: utf-8 -*-

'''
    Created on Dec 22, 2017
    
    @author: matthewcowen-green
    '''

from interpreter4 import parse as pparse
from customlist import customlist
import numpy as np

def parse(line):
    return pparse(line,customlist())







#4      #parse(u"0")
#5      #parse(u"ðŁ")
#6      #parse(u"ᵽ√Ɩ")
#7      #parse(u"±¢")
#10     #parse(u"Ț")
#12     #parse(u"1")
#15     #parse(u"⁻0`ŕ⁺ĐḋŁ⁻ł")
#23     # - DOABLE
#26     #parse(u"ḋĐĐỤ⇹ɔΠ⇹ỤΠ*")
#27     #parse(u"←")
#30     #parse(u"ĐḶ⌊1ᴇ⇹^÷")
#32     #parse(u"Ŀ")
#34     #parse(u"2%⁺")
#35     #parse(u"2%")
#37     #parse(u"Đ√½+⌊+")
#38     #parse(u"0≤2*")
#40     #parse(u"ᵽ")
#41     #parse(u"ᵱ")
#42     #parse(u"žǰ")
#45     #parse(u"⁺Ḟ")
#51     #parse(u"2⇹^⁺")
#62     #parse(u"é⁻⁻/⌊")
#65     #parse(u"ᵱ⁻")
#70     #parse(u"řᵱƩ⁺")
#71     #parse(u"⁺Ḟ⁻")
#79     #parse(u"2⇹^")
#82     #parse(u"Đ²⇹ð⅟⁺Π*")
#93     #parse(u"³√⌊")
#94     #parse(u"Đᵱ-~")
#96     #parse(u"Đ3+*₂")
#108    #parse(u"Ć")
#120    #parse(u"Ħ")
#124    #parse(u"Đ⁺*₂⁺")
#125    #parse(u"Đ³⇹5*+6+₆")
#126    #parse(u"Đ5+Ḟ⇹⁺-")
#128    #parse(u"Đ5+Ḟ⇹Đ⁺*₂-3-")
#129    #parse(u"Đ12√+⇹^12√-⇹↔^-22√*÷")
#130    #parse(u"Đ!⇹řᒆ0↔0⇹`3Ș₋Å1⇹ɔ1=+⇹⁻łŕ₂ƥŕ")
#133    #parse(u"ĐĐĐ1⇹1⇹««⇹1⇹«⁻⇹3Ș⁻1⇹«⁺1⇹«*+⇹⁺1⇹«÷")
#139    #parse(u"2⇹ĐĐ3*!3Ș↔*↔2*⁺!⇹⁺!*÷")
#142    #parse(u"!")
#149    #parse(u"ǝ⌊")
#165    #parse(u"2*‼")
#166    #parse(u"!é/½+1↑⎶Ɩ")
#168    #parse(u"ĐĐĐ3⇹^⇹2*!*2*⇹!↔2+!⇹↔*÷")
#178    #parse(u"ř!Π")
#186    #parse(u"Đ000`ŕ4ȘĐ4ȘĐĐĐ5ȘĐĐ5Ș↔⇹5Ș6Ș8Ș3Ș6Ș4Ș⇹3Ș↔⁺3*~4Ș-+~ĐĐ1~⇹^4ȘÅĐ3Ș⇹+⁻ŘΠ⇹↔Đ↔9Ș↔!3Ș⇹3Ș*⇹!÷*3ȘĐ2⇹^⇹!3Ș4Ș⇹÷*⇹Đ0≥*!*+⇹Đ3Ș⇹⁻3Șłŕ⇹ŕ↔Đ↔⇹3Ș⇹3ȘĐ3Ș⇹⁻Đ5Ș4Ș-3Ș⇹łŕ3Ș↔ŕƥĉ")
#193    #parse(u"Ļ⎶")
#194    #parse(u"√⎶")
#195    #parse(u"Ļ⌊")
#196    #parse(u"√⌊")
#197    #parse(u"!!")
#201    #parse(u"φ*⌊")
#202    #parse(u"ðƩ")
#209    #parse(u"ť⎶")
#210    #parse(u"é⁻*⌊")
#212    #parse(u"²3÷")
#215    #parse(u"22←^^⁺")
#216    #parse(u"2⇹`⇹ą²Ʃ⇹⁻ł")
#217    #parse(u"△")
#218    #parse(u"3⇹`⇹ą²Ʃ⇹⁻ł")
#221    #parse(u"5⇹`⇹ą²Ʃ⇹⁻ł")
#225    #parse(u"2⇹^⁻")
#227    #parse(u"ǝ⎶")
#244    #parse(u"3⇹^")
#245    #parse(u"3⇹ĐĐ2*!3Ș⁺⁺!⇹⁻!*↔*↔÷")
#247    #parse(u"Đ2⇹^⇹-⁻⁻")
#265    #parse(u"ḋĐ2%*ž↑")
#267    #parse(u"4*+1√⌊")
#272    #parse(u"Đ2-^")
#277    #parse(u"Đ3*⇹4*5+√⌊~+5+")
#285    #parse(u"Đ2+ŘḞ↕Ʃ")
#290    #parse(u"²")
#292    #parse(u"Đ2+ŘΠ₆")
#295    #parse(u"Đ2⇹^⇹-⁻")
#297    #parse(u"ĐĐ⁺⇹3+↔8+Π6÷")
#302    #parse(u"4⇹^")
#312    #parse(u"Ṗ")
#325    #parse(u"Đ2⇹")
#326    #parse(u"⬠")
#330    #parse(u"ĐĐ⁺2*⇹⁺Π6÷")
#330    #parse(u"4ć")
#337    #parse(u"Đ⁻⇹2⇹^*⁺")
#344    #parse(u"5⇹ĐĐ2*⇹-2ć⇹3-↔*↔÷")
#346    #parse(u"22←Đ⁺Đ2*⇹ć↔3Ș*⁺^")
#351    #parse(u"5⇹^")
#356    #parse(u"Đ!²⇹Đ⁺!⇹Đ2+!⇹4Ș**⇹2*Đ⁺!⇹!*⇹÷")
#363    #parse(u"Đ5⇹^⇹Đ2*⁻⇹Đ3⇹^⇹Đ²2*⇹2*-2-3Ș*~++")
#371    # - DOABLE
#384    #parse(u"Đ2*⁻*")
#442    #parse(u"!³")
#447    #parse(u"½↑2*⁻ř²Ʃ")
#466    #parse(u"²4*⁻")
#484    #parse(u"č⎶")
#493    #parse(u"š⌊")
#503    #parse(u"ť⌊")
#538    #parse(u"ř⁴Ʃ")
#539    #parse(u"ř⁵Ʃ")
#540    #parse(u"ř⁶Ʃ")
#541    #parse(u"ř⁷Ʃ")
#542    #parse(u"ř⁸Ʃ")
#578    #parse(u"³")
#583    #parse(u"⁴")
#584    #parse(u"⁵")
#689    #parse(u"2⇹^4△%")
#778    #parse(u"ĐĆ⇹⁺Ć+⁻")
#782    #parse(u"ĐĆ2*⇹⁻Ć-")
#918    #parse(u"2⇹^2-")
#982    #parse(u"ᵮ₂⌈")
#parse(u"26*⇹^")                            #1021
#parse(u"Đḋ>⇹ḋ*Ʃ")                         #1065
#parse(u"5*₄")                            #1068
#parse(u"22←^^")                            #1146
#parse(u"2*⁻‼")                            #1147
#parse(u"ϼŁ")                              #1221
#parse(u"ḋŁ")                              #1222
#parse(u"Ć")                               #1246
#parse(u"")                                #1477
#parse(u"⁺~")                              #1478
#parse(u"~")                               #1489
#parse(u"3*ĐĐ⁺⇹2+*⇹3+*")                   #1509
#parse(u"2*ḋ2⇹ɔ")                          #1511
#parse(u"3*ĐĐĐ⁺⇹2+*⇹3+*⇹4+*")              #1512
#parse(u"6*Đ⁺⇹5+*")                        #1513
#parse(u"Đ!*")                             #1563
#parse(u"Đ⁴⇹4⇹^+")                         #1589
#parse(u"Ḟ⁺")                              #1611
#parse(u"ĐĐ3*⇹ć⇹2*⁺÷")                     #1764
#parse(u"Đ⁺*2*⁺")                          #1844
#parse(u"3+Ḟ2-")                           #1911
#parse(u"5*2+Ŀ")                           #1947
#parse(u"φ²*⌊")                            #1950
#1951   #parse(u"2√*⌊")
#1952   #parse(u"2√2+*⌊")
#1953   #parse(u"½+2√*⌊")
#1955   #parse(u"1₁√⁺*⌊")
#parse(u"67+√5+₂*⌊")                       #1956
#parse(u"34←⁻^*")                           #2001
#parse(u"64←^*")                            #2023
#parse(u"2√½+*⌊")                          #2024
#parse(u"Đ²-~⁺")                           #2061
#parse(u"ĐḞ+")                             #2062
#parse(u"4⇹^9*")                            #2063
#parse(u"₄⌊")                              #2265
#parse(u"Đ²*")                             #2378
#parse(u"²2»")                             #2620
#parse(u"8*⁺√⁻₂⌊")                         #3056
#parse(u"8*7-√⁺₂⌈")                        #3057
#parse(u"√⌈")                              #3059
#parse(u"2√1+*⌊")                          #3151
#3152   #parse(u"2√⅟1+*⌊")
#3153   #parse(u"2√1+*⎶")
#parse(u"Đ⁻*6*⁺")                          #3154
#3418   ##DOABLE
#parse(u"⁻3⇹^₂")                           #3462
#parse(u"2*⁺2⇹^")                           #4171
#parse(u"₂⌊")                              #4526
#parse(u"4*3+")                            #4767
#parse(u"4*₃")                            #4773
##4919-4935     replace '⎶' with '⌊' in #4939-4955
#4937   #parse(u"φ²*⎶")
#4938   #parse(u"φ³*⎶")
#4939   #parse(u"φ⁴*⎶")
#4940   #parse(u"φ⁵*⎶")
#4941   #parse(u"φ⁶*⎶")
#4942   #parse(u"φ⁷*⎶")
#4943   #parse(u"φ⁸*⎶")
#4944   #parse(u"φ⁹*⎶")
#4945   #parse(u"φ⁰*⎶")
#4946   #parse(u"φ¹*⎶")
#4947   #parse(u"φ²⁶*⎶")
#4948   #parse(u"φ67+^*⎶")
#4949   #parse(u"φ⁷²*⎶")
#4950   #parse(u"φ³⁵*⎶")
#4951   #parse(u"φ⁴⁴*⎶")
#4952   #parse(u"φ89+^*⎶")
#4953   #parse(u"φ³⁶*⎶")
#4954   #parse(u"φ³⁶φ**⎶")
#4955   #parse(u"φ⁴⁵*⎶")
##4957-4975     replace '⎶' with '⌈' in #4937-4955
#4976   #parse(u"φ³*⌊")
#parse(u"2*⁺")                             #5408
#parse(u"Đ2+*")                            #5563
#parse(u"2*")                              #5843
#parse(u"3+Ḟ3-")                           #6327
#parse(u"Đ2⇹⁻^⇹2⇹^⁻*")                     #6516
#parse(u"2*ḋ2⇹ɔ2⇹^")                       #6519
#parse(u"ϼ↑")                              #6530
#parse(u"3⇹^⁺₂")                           #7051
#parse(u"ƿ")                               #7088
#parse(u"3ṕ")                              #7089
#parse(u"4ṕ")                              #7090
#parse(u"5ṕ")                              #7091
#parse(u"6ṕ")                              #7092
#parse(u"7ṕ")                              #7093
#parse(u"8ṕ")                              #7094
#parse(u"9ṕ")                              #7095
#parse(u"2")                                #7395
#parse(u"ř⁹Ʃ")                             #7487
#parse(u"řƩ")                               #7489
#parse(u"ĐĐ⁻⇹2-**")                        #7531
#parse(u"Đ2⇹⁻^⇹2⇹^⁺*")                     #7582
#parse(u"ϼΠ")                              #7947
#parse(u"ḋ3⇹ɔ")                            #7949
#parse(u"3*")                              #8585
#parse(u"4*")                              #8586
#parse(u"45**")                            #8602
#parse(u"1~⇹ḋŁ^")                           #8836
#parse(u"²2*")
#parse(u"4△")                               #10692
#parse(u"3")                                #10701
#parse(u"4")                                #10709
#parse(u"5")                                #10716
#parse(u"6")                                #10722
#parse(u"7")                                #10727
#parse(u"8")                                #10731
#parse(u"9")                                #10734
#parse(u"56+")                              #10850
#parse(u"4²")                               #10855
#parse(u"54*")                              #10859
#parse(u"6△")                               #10860
#parse(u"6△⁺")                              #10861
#parse(u"6△2+")                             #10862
#parse(u"4!")                               #10863
#parse(u"5²")                               #10864
#parse(u"2⁵")                               #10871
#parse(u"32←^^")                            #11764
#parse(u"4%₃")                            #11765
#parse(u"Đ9*3-*")                          #13656
#parse(u"Đ2*⁺*")                           #14105
#parse(u"ĐḋĐ3Ș<*Đ1>↓1↑")                   #14673
##16742-16764     replace '26*' with '2' in #17522-17544
##16766-16800     replace '26*' with '3' in #17522-17556
##16802-16848     replace '26*' with '4' in #17522-17568
##16850-16908     replace '26*' with '5' in #17522-17580
##16910-16980     replace '26*' with '6' in #17522-17592
##16982-17064     replace '26*' with '7' in #17522-17604
##17066-17160     replace '26*' with '8' in #17522-17616
##17162-17268     replace '26*' with '9' in #17522-17628
##17270-17388     replace '26*' with '25*' in #17522-17640
##17390-17520     replace '26*' with '56+' in #17522-17652
#parse(u"26**²")                           #17522
#parse(u"26**3^")                          #17523
#parse(u"26**4^")                          #17524
#parse(u"26**5^")                          #17525
#parse(u"26**6^")                          #17526
#parse(u"26**7^")                          #17527
#parse(u"26**8^")                          #17528
#parse(u"26**9^")                          #17529
#parse(u"26**25*^")                        #17530
#parse(u"26**56+^")                        #17531
#parse(u"26**26*^")                        #17532
#parse(u"26**1+")                          #17533
#parse(u"26**1+²")                         #17534
#parse(u"26**1+³")                         #17535
#parse(u"26**1+⁴")                         #17536
#parse(u"26**1+⁵")                         #17537
#parse(u"26**1+⁶")                         #17538
#parse(u"26**1+⁷")                         #17539
#parse(u"26**1+⁸")                         #17540
#parse(u"26**1+⁹")                         #17541
#parse(u"26**1+⁰")                         #17542
#parse(u"26**1+¹")                         #17543
#parse(u"26**1+26*^")                      #17544
#parse(u"26**2+")                          #17545
#parse(u"26**2+²")                         #17546
#parse(u"26**2+³")                         #17547
#parse(u"26**2+⁴")                         #17548
#parse(u"26**2+⁵")                         #17549
#parse(u"26**2+⁶")                         #17550
#parse(u"26**2+⁷")                         #17551
#parse(u"26**2+⁸")                         #17552
#parse(u"26**2+⁹")                         #17553
#parse(u"26**2+⁰")                         #17554
#parse(u"26**2+¹")                         #17555
#parse(u"26**2+26*^")                      #17556
#parse(u"26**3+")                          #17557
#parse(u"26**3+²")                         #17558
#parse(u"26**3+³")                         #17559
#parse(u"26**3+⁴")                         #17560
#parse(u"26**3+⁵")                         #17561
#parse(u"26**3+⁶")                         #17562
#parse(u"26**3+⁷")                         #17563
#parse(u"26**3+⁸")                         #17564
#parse(u"26**3+⁹")                         #17565
#parse(u"26**3+⁰")                         #17566
#parse(u"26**3+¹")                         #17567
#parse(u"26**3+26*^")                      #17568
#parse(u"26**4+")                          #17569
#parse(u"26**4+²")                         #17570
#parse(u"26**4+³")                         #17571
#parse(u"26**4+⁴")                         #17572
#parse(u"26**4+⁵")                         #17573
#parse(u"26**4+⁶")                         #17574
#parse(u"26**4+⁷")                         #17575
#parse(u"26**4+⁸")                         #17576
#parse(u"26**4+⁹")                         #17577
#parse(u"26**4+⁰")                         #17578
#parse(u"26**4+¹")                         #17579
#parse(u"26**4+26*^")                      #17580
#parse(u"26**5+")                          #17581
#parse(u"26**5+²")                         #17582
#parse(u"26**5+³")                         #17583
#parse(u"26**5+⁴")                         #17584
#parse(u"26**5+⁵")                         #17585
#parse(u"26**5+⁶")                         #17586
#parse(u"26**5+⁷")                         #17587
#parse(u"26**5+⁸")                         #17588
#parse(u"26**5+⁹")                         #17589
#parse(u"26**5+⁰")                         #17590
#parse(u"26**5+¹")                         #17591
#parse(u"26**5+26*^")                      #17592
#parse(u"26**6+")                          #17593
#parse(u"26**6+²")                         #17594
#parse(u"26**6+³")                         #17595
#parse(u"26**6+⁴")                         #17596
#parse(u"26**6+⁵")                         #17597
#parse(u"26**6+⁶")                         #17598
#parse(u"26**6+⁷")                         #17599
#parse(u"26**6+⁸")                         #17600
#parse(u"26**6+⁹")                         #17601
#parse(u"26**6+⁰")                         #17602
#parse(u"26**6+¹")                         #17603
#parse(u"26**6+26*^")                      #17604
#parse(u"26**7+")                          #17605
#parse(u"26**7+²")                         #17606
#parse(u"26**7+³")                         #17607
#parse(u"26**7+⁴")                         #17608
#parse(u"26**7+⁵")                         #17609
#parse(u"26**7+⁶")                         #17610
#parse(u"26**7+⁷")                         #17611
#parse(u"26**7+⁸")                         #17612
#parse(u"26**7+⁹")                         #17613
#parse(u"26**7+⁰")                         #17614
#parse(u"26**7+¹")                         #17615
#parse(u"26**7+26*^")                      #17616
#parse(u"26**8+")                          #17617
#parse(u"26**8+²")                         #17618
#parse(u"26**8+³")                         #17619
#parse(u"26**8+⁴")                         #17620
#parse(u"26**8+⁵")                         #17621
#parse(u"26**8+⁶")                         #17622
#parse(u"26**8+⁷")                         #17623
#parse(u"26**8+⁸")                         #17624
#parse(u"26**8+⁹")                         #17625
#parse(u"26**8+⁰")                         #17626
#parse(u"26**8+¹")                         #17627
#parse(u"26**8+26*^")                      #17628
#parse(u"26**9+")                          #17629
#parse(u"26**9+²")                         #17630
#parse(u"26**9+³")                         #17631
#parse(u"26**9+⁴")                         #17632
#parse(u"26**9+⁵")                         #17633
#parse(u"26**9+⁶")                         #17634
#parse(u"26**9+⁷")                         #17635
#parse(u"26**9+⁸")                         #17636
#parse(u"26**9+⁹")                         #17637
#parse(u"26**9+⁰")                         #17638
#parse(u"26**9+¹")                         #17639
#parse(u"26**9+26*^")                      #17640
#parse(u"26**25*+")                        #17641
#parse(u"26**25*+²")                       #17642
#parse(u"26**25*+³")                       #17643
#parse(u"26**25*+⁴")                       #17644
#parse(u"26**25*+⁵")                       #17645
#parse(u"26**25*+⁶")                       #17646
#parse(u"26**25*+⁷")                       #17647
#parse(u"26**25*+⁸")                       #17648
#parse(u"26**25*+⁹")                       #17649
#parse(u"26**25*+⁰")                       #17650
#parse(u"26**25*+¹")                       #17651
#parse(u"26**25*+26*^")                    #17652
#parse(u"26**56++")                        #17653
#parse(u"26**56++²")                       #17654
#parse(u"26**56++³")                       #17655
#parse(u"26**56++⁴")                       #17656
#parse(u"26**56++⁵")                       #17657
#parse(u"26**56++⁶")                       #17658
#parse(u"26**56++⁷")                       #17659
#parse(u"26**56++⁸")                       #17660
#parse(u"26**56++⁹")                       #17661
#parse(u"26**56++⁰")                       #17662
#parse(u"26**56++¹")                       #17663
#parse(u"26**56++26*^")                    #17664
#parse(u"26**26*+")                        #17665
#parse(u"26**26*+²")                       #17666
#parse(u"26**26*+³")                       #17667
#parse(u"26**26*+⁴")                       #17668
#parse(u"26**26*+⁵")                       #17669
#parse(u"26**26*+⁶")                       #17670
#parse(u"26**26*+⁷")                       #17671
#parse(u"26**26*+⁸")                       #17672
#parse(u"26**26*+⁹")                       #17673
#parse(u"26**26*+⁰")                       #17674
#parse(u"26**26*+¹")                       #17675
#parse(u"26**26*+26*^")                    #17676
#parse(u"⁺")                               #20725
#parse(u"⁻!Đϼ⇹ḋ⇹ɔƩ")                        #22559
#parse(u"ĐĦ⇹ļ⌈-Å")                         #23416
#parse(u"⁻")                               #23443
#parse(u"¢")                              #24000
#parse(u"³¢")                             #24001
#parse(u"⁴¢")                             #24002
#parse(u"⁵¢")                             #24003
#parse(u"⁶¢")                             #24004
#parse(u"⁷¢")                             #24005
#parse(u"⁸¢")                             #24006
#parse(u"⁹¢")                             #24007
#parse(u"⁰¢")                             #24008
#parse(u"¹¢")                             #24009
#parse(u"26⇹^¢")                          #24010
#parse(u"2⇹Đ²~↔⇹^+")                        #24012
#parse(u"2⇹Đ³~↔⇹^+")                        #24013
#parse(u"2⇹Đ⁴~↔⇹^+")                        #24014
#parse(u"2⇹Đ⁵~↔⇹^+")                        #24015
#parse(u"2⇹Đ⁶~↔⇹^+")                        #24016
#parse(u"2⇹Đ⁷~↔⇹^+")                        #24017
#parse(u"2⇹Đ⁸~↔⇹^+")                        #24018
#parse(u"2⇹Đ⁹~↔⇹^+")                        #24019
#parse(u"2⇹Đ⁰~↔⇹^+")                        #24020
#parse(u"2⇹Đ¹~↔⇹^+")                        #24021
#parse(u"2⇹Đ26*^~↔⇹^+")                     #24022
#parse(u"3⇹^⁻")                             #24023
#parse(u"3⇹Đ~↔⇹^+")                         #24024
#parse(u"3⇹Đ²~↔⇹^+")                        #24025
#parse(u"3⇹Đ³~↔⇹^+")                        #24026
#parse(u"3⇹Đ⁴~↔⇹^+")                        #24027
#parse(u"3⇹Đ⁵~↔⇹^+")                        #24028
#parse(u"3⇹Đ⁶~↔⇹^+")                        #24029
#parse(u"3⇹Đ⁷~↔⇹^+")                        #24030
#parse(u"3⇹Đ⁸~↔⇹^+")                        #24031
#parse(u"3⇹Đ⁹~↔⇹^+")                        #24032
#parse(u"3⇹Đ⁰~↔⇹^+")                        #24033
#parse(u"3⇹Đ¹~↔⇹^+")                        #24034
#parse(u"3⇹Đ26*^~↔⇹^+")                     #24035
#parse(u"4⇹^⁻")                             #24036
#parse(u"4⇹Đ~↔⇹^+")                         #24037
#parse(u"4⇹Đ²~↔⇹^+")                        #24038
#parse(u"4⇹Đ³~↔⇹^+")                        #24039
#parse(u"4⇹Đ⁴~↔⇹^+")                        #24040
#parse(u"4⇹Đ⁵~↔⇹^+")                        #24041
#parse(u"4⇹Đ⁶~↔⇹^+")                        #24042
#parse(u"4⇹Đ⁷~↔⇹^+")                        #24043
#parse(u"4⇹Đ⁸~↔⇹^+")                        #24044
#parse(u"4⇹Đ⁹~↔⇹^+")                        #24045
#parse(u"4⇹Đ⁰~↔⇹^+")                        #24046
#parse(u"4⇹Đ¹~↔⇹^+")                        #24047
#parse(u"4⇹Đ26*^~↔⇹^+")                     #24048
#parse(u"5⇹^⁻")                             #24049
#parse(u"5⇹Đ~↔⇹^+")                         #24050
#parse(u"5⇹Đ²~↔⇹^+")                        #24051
#parse(u"5⇹Đ³~↔⇹^+")                        #24052
#parse(u"5⇹Đ⁴~↔⇹^+")                        #24053
#parse(u"5⇹Đ⁵~↔⇹^+")                        #24054
#parse(u"5⇹Đ⁶~↔⇹^+")                        #24055
#parse(u"5⇹Đ⁷~↔⇹^+")                        #24056
#parse(u"5⇹Đ⁸~↔⇹^+")                        #24057
#parse(u"5⇹Đ⁹~↔⇹^+")                        #24058
#parse(u"5⇹Đ⁰~↔⇹^+")                        #24059
#parse(u"5⇹Đ¹~↔⇹^+")                        #24060
#parse(u"5⇹Đ26*^~↔⇹^+")                     #24061
#parse(u"6⇹^⁻")                             #24062
#parse(u"6⇹Đ~↔⇹^+")                         #24063
#parse(u"6⇹Đ²~↔⇹^+")                        #24064
#parse(u"6⇹Đ³~↔⇹^+")                        #24065
#parse(u"6⇹Đ⁴~↔⇹^+")                        #24066
#parse(u"6⇹Đ⁵~↔⇹^+")                        #24067
#parse(u"6⇹Đ⁶~↔⇹^+")                        #24068
#parse(u"6⇹Đ⁷~↔⇹^+")                        #24069
#parse(u"6⇹Đ⁸~↔⇹^+")                        #24070
#parse(u"6⇹Đ⁹~↔⇹^+")                        #24071
#parse(u"6⇹Đ⁰~↔⇹^+")                        #24072
#parse(u"6⇹Đ¹~↔⇹^+")                        #24073
#parse(u"6⇹Đ26*^~↔⇹^+")                     #24074
#parse(u"7⇹^⁻")                             #24075
#parse(u"7⇹Đ~↔⇹^+")                         #24076
#parse(u"7⇹Đ²~↔⇹^+")                        #24077
#parse(u"7⇹Đ³~↔⇹^+")                        #24078
#parse(u"7⇹Đ⁴~↔⇹^+")                        #24079
#parse(u"7⇹Đ⁵~↔⇹^+")                        #24080
#parse(u"7⇹Đ⁶~↔⇹^+")                        #24081
#parse(u"7⇹Đ⁷~↔⇹^+")                        #24082
#parse(u"7⇹Đ⁸~↔⇹^+")                        #24083
#parse(u"7⇹Đ⁹~↔⇹^+")                        #24084
#parse(u"7⇹Đ⁰~↔⇹^+")                        #24085
#parse(u"7⇹Đ¹~↔⇹^+")                        #24086
#parse(u"7⇹Đ26*^~↔⇹^+")                     #24087
#parse(u"8⇹^⁻")                             #24088
#parse(u"8⇹Đ~↔⇹^+")                         #24089
#parse(u"8⇹Đ²~↔⇹^+")                        #24090
#parse(u"8⇹Đ³~↔⇹^+")                        #24091
#parse(u"8⇹Đ⁴~↔⇹^+")                        #24092
#parse(u"8⇹Đ⁵~↔⇹^+")                        #24093
#parse(u"8⇹Đ⁶~↔⇹^+")                        #24094
#parse(u"8⇹Đ⁷~↔⇹^+")                        #24095
#parse(u"8⇹Đ⁸~↔⇹^+")                        #24096
#parse(u"8⇹Đ⁹~↔⇹^+")                        #24097
#parse(u"8⇹Đ⁰~↔⇹^+")                        #24098
#parse(u"8⇹Đ¹~↔⇹^+")                        #24099
#parse(u"8⇹Đ26*^~↔⇹^+")                     #24100
#parse(u"9⇹^⁻")                             #24101
#parse(u"9⇹Đ~↔⇹^+")                         #24102
#parse(u"9⇹Đ²~↔⇹^+")                        #24103
#parse(u"9⇹Đ³~↔⇹^+")                        #24104
#parse(u"9⇹Đ⁴~↔⇹^+")                        #24105
#parse(u"9⇹Đ⁵~↔⇹^+")                        #24106
#parse(u"9⇹Đ⁶~↔⇹^+")                        #24107
#parse(u"9⇹Đ⁷~↔⇹^+")                        #24108
#parse(u"9⇹Đ⁸~↔⇹^+")                        #24109
#parse(u"9⇹Đ⁹~↔⇹^+")                        #24110
#parse(u"9⇹Đ⁰~↔⇹^+")                        #24111
#parse(u"9⇹Đ¹~↔⇹^+")                        #24112
#parse(u"9⇹Đ26*^~↔⇹^+")                     #24113
#parse(u"1ᴇ⇹^⁻")                           #24114
#parse(u"1ᴇ⇹Đ~↔⇹^+")                       #24115
#parse(u"1ᴇ⇹Đ²~↔⇹^+")                      #24116
#parse(u"1ᴇ⇹Đ³~↔⇹^+")                      #24117
#parse(u"1ᴇ⇹Đ⁴~↔⇹^+")                      #24118
#parse(u"1ᴇ⇹Đ⁵~↔⇹^+")                      #24119
#parse(u"1ᴇ⇹Đ⁶~↔⇹^+")                      #24120
#parse(u"1ᴇ⇹Đ⁷~↔⇹^+")                      #24121
#parse(u"1ᴇ⇹Đ⁸~↔⇹^+")                      #24122
#parse(u"1ᴇ⇹Đ⁹~↔⇹^+")                      #24123
#parse(u"1ᴇ⇹Đ⁰~↔⇹^+")                      #24124
#parse(u"1ᴇ⇹Đ¹~↔⇹^+")                      #24125
#parse(u"1ᴇ⇹Đ26*^~↔⇹^+")                   #24126
#parse(u"56+⇹^⁻")                           #24127
#parse(u"56+⇹Đ~↔⇹^+")                       #24128
#parse(u"56+⇹Đ²~↔⇹^+")                      #24129
#parse(u"56+⇹Đ³~↔⇹^+")                      #24130
#parse(u"56+⇹Đ⁴~↔⇹^+")                      #24131
#parse(u"56+⇹Đ⁵~↔⇹^+")                      #24132
#parse(u"56+⇹Đ⁶~↔⇹^+")                      #24133
#parse(u"56+⇹Đ⁷~↔⇹^+")                      #24134
#parse(u"56+⇹Đ⁸~↔⇹^+")                      #24135
#parse(u"56+⇹Đ⁹~↔⇹^+")                      #24136
#parse(u"56+⇹Đ⁰~↔⇹^+")                      #24137
#parse(u"56+⇹Đ¹~↔⇹^+")                      #24138
#parse(u"56+⇹Đ26*^~↔⇹^+")                   #24139
#parse(u"26*⇹^⁻")                           #24140
#parse(u"26*⇹Đ~↔⇹^+")                       #24141
#parse(u"26*⇹Đ²~↔⇹^+")                      #24142
#parse(u"26*⇹Đ³~↔⇹^+")                      #24143
#parse(u"26*⇹Đ⁴~↔⇹^+")                      #24144
#parse(u"26*⇹Đ⁵~↔⇹^+")                      #24145
#parse(u"26*⇹Đ⁶~↔⇹^+")                      #24146
#parse(u"26*⇹Đ⁷~↔⇹^+")                      #24147
#parse(u"26*⇹Đ⁸~↔⇹^+")                      #24148
#parse(u"26*⇹Đ⁹~↔⇹^+")                      #24149
#parse(u"26*⇹Đ⁰~↔⇹^+")                      #24150
#parse(u"26*⇹Đ¹~↔⇹^+")                      #24151
#parse(u"26*⇹Đ26*^~↔⇹^+")                   #24152
#parse(u"ĐḋĐ3Ș<*↑")                        #32742
#parse(u"²5*")                             #33429
#parse(u"Đ4*⁻*")
#parse(u"1~⇹^")                             #33999
#parse(u"2⇹⁻Å1»^⌊")                         #34008
#---- see 7091                              #37469
#---- see 7473                              #37473
#---- see 7476                              #37476
#parse(u"ḋ3⇹ɔ3⇹^")                         #38500
#parse(u"ḋĐ3≠*Π")                          #38502
#parse(u"1~⇹Đ↔⇹^*")                         #38608
#parse(u"Đ²6*+")                           #49453
#parse(u"22←^^⁻")                           #51179
#parse(u"ĐḋϺ⇹ɔ")                           #51903
#parse(u"Đϼ↑÷")                            #52126
#parse(u"4⇹^⁺")                             #52539
#parse(u"ĐḋĐ3Ș<*↑ĐḋĐ3Ș<*↑")                #54576
#parse(u"!⁺ḋŁ")                            #54990
#parse(u"!⁻ḋŁ")                            #54991
#parse(u"2⇹^⁺ḋŁ")                           #54992
#parse(u"⁺67+3*↓")                         #56064
#parse(u"0>")                              #57427
#parse(u"32←^^2+")                          #57727
#parse(u"1ᴇ⇹⁺^9²÷")                        #57932
#parse(u"1ᴇ⇹^9²⁻*9²÷")                     #57933
#parse(u"1ᴇ⇹^⁺ḋŁ")                         #57934
#parse(u"9⇹^⁺ḋŁ")                           #57935
#parse(u"8⇹^⁺ḋŁ")                           #57936
#parse(u"7⇹^⁺ḋŁ")                           #57937
#parse(u"6⇹^⁺ḋŁ")                           #57938
#parse(u"5⇹^⁺ḋŁ")                           #57939
#parse(u"4⇹^⁺ḋŁ")                           #52540
#parse(u"3⇹^⁺ḋŁ")                           #57941
#parse(u"1ᴇ⇹^⁻ḋŁ")                         #57951
#parse(u"9⇹^⁻ḋŁ")                           #57952
#parse(u"8⇹^⁻ḋŁ")                           #57953
#parse(u"7⇹^⁻ḋŁ")                           #57954
#parse(u"6⇹^⁻ḋŁ")                           #57955
#parse(u"5⇹^⁻ḋŁ")                           #57956
#parse(u"4⇹^⁻ḋŁ")                           #57957
#parse(u"3⇹^⁻ḋŁ")                           #57958
#parse(u"2%¢")                             #59841
#parse(u"32←^^⁺1»")                         #59917
#parse(u"32←^^⁻1»")                         #59918
#parse(u"32←^^⁺")                           #59919
#parse(u"2*⁻")                             #60747
#parse(u"Đ5Ǥ÷")                            #60791
#parse(u"1=")                              #63524
#parse(u"Đ₉⇹25*⇹⁻^⇹↔9²⁻*9²÷+")             #64617
#parse(u"ϼĐ1>*↕Π")                         #66048
#parse(u"ϼĐ1>*↕Ʃ")                         #74320
#parse(u"ąĐ²+Ʃ")                           #77523
#parse(u"3%0=")                            #79978
#parse(u"6%0=")                            #79979
#parse(u"5%0=")                            #79998
#parse(u"7%0=")                            #82784
#parse(u"Đ!⇹řᒆ0↔0⇹`3Ș₋Å1⇹ɔ1=+⇹⁻łŕƥŕ")      #86852
#parse(u"2*ƿ")                             #99820
#parse(u"2*⁺ƿ")                            #99821
#parse(u"5Ĺ")                              #109046
#parse(u"2~⇹^")                             #122803
#parse(u"33^^")                            #122968
#parse(u"Đϼ↕Π÷")                           #130065
#parse(u"ḋĐ5≠*Π")                          #132739
#parse(u"25*2←^^⁻9÷")                       #136308
#parse(u"²6*⁻")                            #140811
#parse(u"2*3+")                            #144396
#parse(u"²27**")                           #144555
#parse(u"Đ9*2+*")                          #147296
#parse(u"Đ7*5-*2*")                        #152760
#parse(u"Đ2*⁺⇹5*6+*")                      #153127
#parse(u"4*Đ⁺⇹2+*")                        #157870
#parse(u"²9*3-")                           #157872
#parse(u"2≥")                              #157928
#parse(u"Đ⁺2»⇹1»*")                        #159915
#parse(u"²Ħ")                              #159918
#parse(u"Đ⁺₫*")                            #160926
#parse(u"Đ⁻₫*")                            #160929
#parse(u"Đ⁺Ś*")                            #160938
#parse(u"Đ⁻Ś*")                            #160942
#parse(u"56*Ǥ1=")                          #162289
#parse(u"2*⁺")                             #176271
#parse(u"1~⇹Đ↔⇹^*~")                        #181983
#parse(u"2=")                              #185012
#parse(u"3=")                              #185013
#parse(u"4=")                              #185014
#parse(u"5=")                              #185015
#parse(u"6=")                              #185016
#parse(u"7=")                              #185017
#parse(u"Đ27**3-*")                        #185019
#parse(u"Đ25**3-*")                        #195018
#parse(u"Đ27**56+-*")                      #195021
#parse(u"Đ27**⁻*")                         #195023
#parse(u"Đ27**3+*")                        #195025
#parse(u"Đ2*⁺7**")                         #195026
#parse(u"Đ2*⁻*7*")                         #195320
#parse(u"Đ²31»+⇹½⇹1~⇹^*+")                 #248800
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#