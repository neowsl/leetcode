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
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycle_len = n + 1

        # stores count of labels
        queue: list[int] = []

        label_freq = Counter(tasks)
        for label in label_freq:
            queue.append(-label_freq[label])

        heapq.heapify(queue)

        ans = 0

        while queue:
            rem = []
            for _ in range(cycle_len):
                if not queue and not rem:
                    break

                ans += 1
                if not queue:
                    continue

                # take most frequent label and use it
                x = heapq.heappop(queue)
                x += 1
                if x < 0:
                    rem.append(x)

            queue += rem
            heapq.heapify(queue)

        return ans


# @leet end
