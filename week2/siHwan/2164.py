# 카드 2

from collections import deque
import sys


ls = deque()

num = int(input())

for i in range(num):
    ls.append(i+1)

while(len(ls) > 1):
    ls.popleft()
    data = ls.popleft()
    ls.append(data)

print(ls[0])