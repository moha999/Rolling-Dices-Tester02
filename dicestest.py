#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 20:00:02 2021
Tester code.
@author: Mohammed H
"""

from dices_0_1 import Dices

class DicesTest:
        
    @staticmethod
    def testBigPairs():
        dices= Dices(2,100)
        ipot = dices.pot
        dices.bet=1
        lst=[[1,1],[6,6]]
        for i in lst:
            dices._Dices__faces=i
            dices.check()
        fpot = dices.pot
        print(ipot, fpot, ipot-fpot)
        return fpot-ipot == 2*10 
      
    @staticmethod
    def testSmallPairs():
        dices= Dices(2,100)
        ipot = dices.pot
        dices.bet=1
        lst=[[2,2],[3,3],[4,4],[5,5]]
        for i in lst:
            dices._Dices__faces=i
            dices.check()
        fpot = dices.pot
        print(ipot, fpot, ipot-fpot)
        return fpot-ipot == 2*4 
    @staticmethod
    def testSum():
        dices= Dices(2,100)
        ipot = dices.pot
        dices.bet=1
        lst=[[1,5],[4,2],[5,1],[2,4]]
        for i in lst:
            dices._Dices__faces=i
            dices.check()
        fpot = dices.pot
        return ipot-fpot == 0 # always will be zero.
    @staticmethod   
    def testBigLosses():  
        dices= Dices(2,100)
        ipot = dices.pot
        dices.bet=1
        for i in range(1, 7):
            for j in range(1, 7):
                if i != j and i + j != 6:
                    dices._Dices__faces[0] = i
                    dices._Dices__faces[1] = j
                    dices.check()
        fpot = dices.pot
        return ipot - fpot == 4*4*2 + 2*5*2
        
       
if __name__ == '__main__' :
    print(f'Big pairs (1,1 ja 6,6) test is passed: {DicesTest.testBigPairs()}')
    print(f'Small pairs (2,2 3,3 4,4 5,5) test passed: {DicesTest.testSmallPairs()}')
    print(f'Small losses test is passed: {DicesTest.testSum()}')
    print(f'Big losses test is passed: {DicesTest.testBigLosses()}')