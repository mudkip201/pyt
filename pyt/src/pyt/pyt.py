# -*- coding: utf-8 -*-

import interpreter3 as interp
import argparse
import io
from customlist import customlist

def parse(line):
    return interp.parse(line,customlist())

def main():
    parser=argparse.ArgumentParser(description="Executes a pyt file")
    parser.add_argument("--file","-f",type=str,required=True)
    parser.add_argument("--bytecode","-b",action="store_true")
    args=parser.parse_args()
    
    
    if(args.bytecode):
        codepage=u"⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉¼½¾⅐⅑⅒⅓⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞⅟Ƨ°|!÷↑↓←↕↔⇹¬^«»≤≥<>=≠√∛∜∞∈~˜%/+-*△⬠⬡∧∨⊼⊽⊻⊙⌊⌈⎶‰×ÅÁąáɓÇČƇĆçč¢ćĉɔĐðḋ₫éǝḞᵮǤĦĨƖǰḶĻĽĹŁĿļɬłɫṀϺɯɳṔƤǷҎᑭ₽Ṗ₱ᒆṕƥṗƿϼҏᵱŘɽɾɹʀřŕṛŞŠŜŚȘşŝšŤŦȚťŧỤʊŽžµΠπƩφ≡‼`⦋⁺⁻₊₋0123456789⑴·?:;"
        f=io.open(args.file,mode="rb")
        line=u""
        byte=f.read(1)
        while byte!="":
            line+=codepage[ord(byte)]
            byte=f.read(1)
        f.close()
        parse(line)
    else:
        f=io.open(args.file,mode="r",encoding="utf-8")
        parse(f.read())
        f.close()



if __name__ == "__main__":
    main()