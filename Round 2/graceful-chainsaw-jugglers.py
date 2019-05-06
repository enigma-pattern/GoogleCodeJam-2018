# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 2 - Problem B. Graceful Chainsaw Jugglers
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000007706/00000000000459f3
#
# Time:  O(R^(4/3)*B^(4/3)), pass in PyPy2 but Python2
# Space: O(R^(4/3)*B^(4/3))
#

import collections
import sys

MAX_R, MAX_B = 500, 500

def graceful_chainsaw_jugglers(dp):
    R, B = map(int, raw_input().strip().split())
    return dp[R][B]

V = []
for i in xrange(MAX_R+1):
    for j in xrange(MAX_B+1):
        if (i, j) == (0, 0):
            continue
        if (j+1)*i*(i+1)//2 <= MAX_R and (i+1)*j*(j+1)//2 <= MAX_B:
            V.append((i, j))
dp = [[0 for _ in xrange(MAX_B+1)] for _ in xrange(MAX_R+1)]
for i in xrange(len(V)):
   for r in reversed(xrange(MAX_R+1)):
       if r-V[i][0] < 0:
           break
       for b in reversed(xrange(MAX_B+1)):
           if b-V[i][1] < 0:
               break
           dp[r][b] = max(dp[r][b], 1+dp[r-V[i][0]][b-V[i][1]])
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, graceful_chainsaw_jugglers(dp))
