# -*- coding: utf-8 -*-
from __future__ import print_function
from colorama import *
import time
import subprocess
import sys
import os

init() #colorama
#---PLATFORM
flagplatform=0
if os.name=="nt":
    flagplatform=1
else:import readline
#---/PLATFORM

EPS=1e-5

#---VERSION
try:
    pythonv=2
    type(raw_input)
except:
    pythonv=3
#---/VERSION

"""
#---DATA
if len(sys.argv)<=1:
    print("Need to specify executable!")
    sys.exit()
try:
    with open(sys.argv[1],"r") as f:
        pass
except:
    print("There is no file named \""+sys.argv[1]+"\"")
    sys.exit()
#---/DATA
"""
#---STYLING
def res():
    return Style.RESET_ALL
def y(st):
    return Fore.YELLOW+Style.BRIGHT+st+res()
def g(st):
    return Fore.GREEN+Style.BRIGHT+st+res()
def r(st):
    return Fore.RED+Style.BRIGHT+st+res()
def br(st):
    return Style.BRIGHT+'\033[4m'+st+res()

def box(st):
    print ( "-"*4+"-"*len(st),"\n|",st,"|\n"+"-"*len(st)+"-"*4 )
#---/STYLING

def getinp(st):
    if pythonv==2:
        inp=raw_input(st)
    else:
        inp=input(st)
    return inp

##INTRO
count=1
corcount=0
wrocount=0

print("a tester by")
time.sleep(0.2)
print(br(g("#username")))
time.sleep(1.2)
print(".")
print("\ngood luck!")
print()
time.sleep(1)

##MAIN

print(Style.BRIGHT+"!Press Ctrl+C to finish.!"+res())
try:
    while True:
        """
        process = subprocess.Popen([("" if flagplatform else "./") + sys.argv[1]], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        process.stdin.write(str(getinp("message:")).encode('utf-8'))
        fromuser = process.communicate()[0].strip().decode('utf-8')
        process.stdin.close()
        """
        break;
## WIN+LINUX CTRL+C HANDLE
except EOFError:
    try:
        print ("\t")
    except KeyboardInterrupt:
        try:
            print ("\t")
        except:
            pass
except KeyboardInterrupt:
    try:
        print ("\t")
    except:
        pass

##END
print()
if corcount>=wrocount:
    print(g("{} correct out of: {}").format(corcount,count-1))
else:
    print(r("{} correct out of: {}").format(corcount,count-1))
print(y("---"))
box("Hello world!")
