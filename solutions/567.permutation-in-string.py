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
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        def hash(c: str) -> int:
            return ord(c) - ord("a")

        target_freq = [0] * 26
        for c in s1:
            target_freq[hash(c)] += 1

        curr_freq = [0] * 26
        for i in range(len(s1)):
            curr_freq[hash(s2[i])] += 1

        if curr_freq == target_freq:
            return True

        left = 0
        right = len(s1)

        while right < len(s2):
            curr_freq[hash(s2[right])] += 1
            curr_freq[hash(s2[left])] -= 1

            if curr_freq == target_freq:
                return True

            left += 1
            right += 1

        return False


# @leet end

