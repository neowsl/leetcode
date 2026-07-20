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
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        value = list(map(lambda x, y: x - y, gas, cost))
        # impossible if sum(gas) < sum(cost), always possible otherwise
        if sum(value) < 0:
            return -1

        running_value = 0
        global_min = (0, 0)
        for i, v in enumerate(value):
            if running_value < global_min[1]:
                # we want to start at global min, because everything will be
                # above it
                global_min = i, running_value

            running_value += v

        return global_min[0]


# @leet end

