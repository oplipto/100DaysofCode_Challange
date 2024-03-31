#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def transformSentence(sentence):
    # Write your code here\
    result = sentence[0]  # Keep the first character unchanged
    for i in range(1, len(sentence)):
        if sentence[i].lower() < sentence[i - 1].lower():
            result += sentence[i].upper()
        else:
            result += sentence[i].lower()
    return result

def main():
    sentence = input().strip()
    transformed_sentence = transformSentence(sentence)
    print(transformed_sentence)

if __name__ == "__main__":
    main()