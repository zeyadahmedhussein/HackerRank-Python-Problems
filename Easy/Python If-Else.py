#!/bin/python3

import math
import os
import random
import re
import sys


user_input = int(input())
if(user_input%2==0):
    if(user_input>=2 and user_input<=5):
        print("Not Weird")
    elif user_input>=6 and user_input<=20 :
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")
