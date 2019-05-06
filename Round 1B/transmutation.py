# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 1B - Problem C. Transmutation
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000007764/000000000003675c
#
# Time:  O(M^3 * logS)
# Space: O(M^2)
#

def find_debt(G):
    debt = min(G)
    return len(G) if debt >= 0 else G.index(debt)

def multiply(R, k):
    return [g*k for g in R]

def add(R1, R2):
    for i in xrange(len(R2)):
        R1[i] += R2[i]

def impossible(L, R, G):
    R, G = [Ri[:] for Ri in R], G[:]
    G[0] -= L
    if G[0] >= 0:
        return False
    i = 0
    while i != len(G):
        Ri = R[i]
        if Ri[i] != 0 or \
           sum(G)-G[i] < -G[i]*sum(Ri):  # pruning
            return True
        add(G, multiply(Ri, G[i]))
        G[i] = 0
        for Rj in R:
            if Rj and Rj[i] != 0:
                add(Rj, multiply(Ri, Rj[i]))
                Rj[i] = 0
        Ri = None
        i = find_debt(G)
    return False

def transmutation():
    M = input()
    R = []
    for _ in xrange(M):
        R1, R2 = map(int, raw_input().strip().split())
        Ri = [0] * M
        Ri[R1-1] = Ri[R2-1] = 1
        R.append(Ri)
    G = map(int, raw_input().strip().split())

    left, right = G[0], sum(G)
    while left <= right:
        mid = left + (right-left)//2
        if impossible(mid, R, G):
            right = mid-1
        else:
            left = mid+1
    return left-1
    
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, transmutation())
