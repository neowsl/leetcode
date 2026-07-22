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
class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.next: Node | None = None
        self.prev: Node | None = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # head.next = least recently used node
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.nodes: dict[int, Node] = {}

    def __insert_at_tail(self, node: Node) -> None:
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

        self.nodes[node.key] = node
        self.capacity -= 1

    def __remove_node(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

        del self.nodes[node.key]
        self.capacity += 1

    def __access_node(self, key: int) -> Node:
        node = self.nodes[key]

        self.__remove_node(node)
        self.__insert_at_tail(node)

        return self.nodes[key]

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        return self.__access_node(key).value

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.__access_node(key).value = value
            return

        new_node = Node(key, value)
        self.__insert_at_tail(new_node)

        if self.capacity < 0:
            self.__remove_node(self.head.next)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @leet end

