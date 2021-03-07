
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    print(len(max(re.split("0+",bin(n)[2:])))) # 0+ is to get away with the condition of multiple zeros 
