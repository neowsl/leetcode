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
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)

        left_bound = [0] * N
        right_bound = [N - 1] * N

        stack = [0]
        for i in range(1, N):
            height = heights[i]

            while stack and heights[stack[-1]] >= height:
                stack.pop()

            left_bound[i] = stack[-1] + 1 if stack else 0
            stack.append(i)

        stack = [N - 1]
        for i in reversed(range(0, N - 1)):
            height = heights[i]

            while stack and heights[stack[-1]] >= height:
                stack.pop()

            right_bound[i] = stack[-1] - 1 if stack else N - 1
            stack.append(i)

        ans = 0
        for i in range(N):
            height = heights[i]
            width = right_bound[i] - left_bound[i] + 1
            ans = max(ans, height * width)

        return ans


# @leet end
