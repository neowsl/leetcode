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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid_bst(root: Optional[TreeNode], min_val: int, max_val: int):
            if not root:
                return True

            if root.val <= min_val or root.val >= max_val:
                return False

            return is_valid_bst(root.left, min_val, root.val) and is_valid_bst(
                root.right, root.val, max_val
            )

        return is_valid_bst(root, -(1 << 32), 1 << 32)


# @leet end

