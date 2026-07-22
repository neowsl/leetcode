# @leet imports start
import bisect
import collections
import copy
import datetime
import functools
import heapq
import io
import itertools
import json
import math
import operator
import random
import re
import statistics
import string
import sys
from bisect import *
from builtins import *
from collections import *
from copy import *
from datetime import *
from functools import *
from heapq import *
from io import *
from itertools import *
from json import *
from math import *
from operator import *
from random import *
from re import *
from statistics import *
from string import *
from sys import *
from typing import *

# @leet imports end


# @leet start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        N = len(digits)

        carry = 1
        ans: list[int] = [0] * N

        for i in reversed(range(N)):
            new_digit = digits[i] + carry

            if new_digit > 9:
                ans[i] = new_digit % 10
                carry = 1
            else:
                ans[i] = new_digit
                carry = 0

        if carry == 1:
            ans.insert(0, 1)

        return ans


# @leet end
