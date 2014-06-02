"""

 hello world

   """

"""
   EQuilo is simply a name i gave to the programe jus for fun.I like naming thigs i make. I tried a lot of strategies to code this particular program
   but this worked for me the best.

"""

import time
"""
print " "
print " " 
print " "

print "-----------------------------------EQUILO v.1.0.0-----------------------------"
print " "
print " "
print "EQUILO is a programme written in python,which can calculate the value of any equation given with  '+' ,'-' , '*' or division in any arbittary order."
print "Developed by Jishnu Menon for PerleyBrook Labs"
print " "
print " "
print " "
print " "
print " "
"""
// hey
        
# Input of the program
#print "$ python EQuilo.py"
theString = raw_input("")


# <string>.split() is a method in python to split the string into a list of smaller strings on the basis of a separator. if the parameter is left empty,it splits every <space>.
theList=theString.split()

"""
    Now the string is split into smaller bits of strings., comfortably in the format <operent>,<operator>,<operent>...
    To get the correct order of performing the mathematiicl operstions.,we must follow the BODMAS procedure
    Since there are no brackets.,DMAS. Our string is theString.theString is first searched for '/' sign.and the the 2 elements on either side of the sign are
    POPed out  separately to to variables.These are then divided separately and replaced in place of the '/' sign.This process is looped till the number of '/ '
    signs are decremented to 0.When the list passes the division section all the division operations will be over.

    The same process repeat for for all the operations . By the end of the program the list will shrink to just 1 element.which is our answer.
"""


# DIVISION CODE



divCount = theString.count("/")
while divCount>0:
        div=theList.index("/")
        div1 = float (theList.pop(div-1))
        div2 = float (theList.pop(div))
        if div2 == 0:
                print " "
                print " "
                print "Division with 0 is not possible"
                print "Exiting program "
                time.sleep(3)
                break
        now  = div1/div2
        theList.pop(div-1)
        theList.insert(div-1,now)
        divCount=divCount-1


# MULTIPLICATION CODE


mulCount = theString.count("*")
while mulCount>0:
        mul=theList.index("*")
        mul1 = float (theList.pop(mul-1))
        mul2 = float (theList.pop(mul))
        now  = mul1*mul2
        theList.pop(mul-1)
        theList.insert(mul-1,now)
        mulCount=mulCount-1

# arithemetics

minusList=[]
plusList=[]

minusCount=theString.count("-")

while minusCount > 0:
    minusPos=theList.index("-")
    theList.pop(minusPos)
    minusNo=theList.pop(minusPos)
    minusList.append(minusNo)
    minusCount=theList.count("-")


plusCount=theString.count("+")

while plusCount > 0:
    plusPos=theList.index("+")
    theList.pop(plusPos)
    plusList=theList
    plusCount=theList.count("+")


plusListLen=len(theList)
plusTot=0
plusNow=0

while plusListLen>0:
    plusNow=float(theList.pop(plusListLen-1))
    plusTot=plusNow+plusTot
    plusListLen=len(theList)




minusListLen=len(minusList)
minusTot=0
minusNow=0

while minusListLen>0:
    minusNow=float(minusList.pop(minusListLen-1))
    minusTot=minusNow+minusTot
    minusListLen=len(minusList)






###############################################
finalAnswer=plusTot-minusTot








print int(finalAnswer)
#raw_input()

