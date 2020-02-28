# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 18:39:47 2020

@author: MARAT
"""










a = int( input() )
sum = 0
for i in range( 1, a ):

    sum = sum +  i * (i+1)
    b=str(i)
    k=str(i+1)
    t=str(sum)
    if ( i == a - 1 ):
        print(b+"*"+k,end="")
    else:
        print(b+"*"+k+"+",end="")
            
print('='+t )