#!/bin/python3

import os
import sys
import time
from collections import deque

# Complete the solve function below.
def solve1(h, v, junctions, edges):
    possiblePaths = (n*n - n) / 2
    visitedCounter = 0
    start = time.time()
    for i,j in enumerate(junctions) :
        s = set();
        walkPath1(h, v, junctions, edges, i, s)
        visitedCounter += len(s)
        print ("from " + str(i) + " found "+ str(len(s)))
    print ("pp " + str(possiblePaths) + " visited "+ str(visitedCounter) + " total time " + str(time.time() - start))
    return possiblePaths - (visitedCounter - n)/2

# Complete the solve function below.
def solve2(h, v, junctions, edges):
    possiblePaths = (n*n - n) / 2
    visitedCounter = 0
    start = time.time()
    q = deque()
    visitSet = set()
    for i,j in enumerate(junctions) :
        visitH = {}
        visitV = {}
        visitH[str(i)] = 0
        visitV[str(i)] = 0
        q.append(i)
        while (len(q) > 0) :
            lastJ = q.popleft()
            visitSet.add(lastJ)
            for e in edges :
                if lastJ+1 in e :
                    nextJ = -1
                    if (e[0]-1 == lastJ) :
                        nextJ = e[1]-1
                    elif (e[1]-1 == lastJ ) :
                        nextJ = e[0]-1
                    if (not nextJ in visitSet) :
                        #print ("2  lastH " + str(visitH[str(lastJ)]))
                        visitH[str(nextJ)] = visitH[str(lastJ)] + abs(junctions[lastJ][0] - junctions[nextJ][0])
                        visitV[str(nextJ)] = visitV[str(lastJ)] + abs(junctions[lastJ][1] - junctions[nextJ][1])
                        if (visitH[str(nextJ)] <= h and visitV[str(nextJ)] <= v) :
                            #print ("2  Walking From " + str(lastJ) + " to " + str(nextJ) + " with h " + str(visitH[str(nextJ)]) + " v " + str(visitV[str(nextJ)]))
                            q.append(nextJ)
        print ("2 from " + str(i) + " found "+ str(len(visitSet)))
        visitedCounter += len(visitSet)
        visitSet.clear()
    print ("2 pp " + str(possiblePaths) + " visited "+ str(visitedCounter) + " total time " + str(time.time() - start))
    return possiblePaths - (visitedCounter - n)/2

def walkPath1 (h, v, junctions, edges, lastJ, visitSet) :
    visitSet.add(lastJ)
    for e in edges :
        if (lastJ+1 in e) :
            nextJ = -1
            if (e[0]-1 == lastJ) :
                nextJ = e[1]-1
            elif (e[1]-1 == lastJ ) :
                nextJ = e[0]-1
            if (not nextJ in visitSet) :
                nextH = h - abs(junctions[lastJ][0] - junctions[nextJ][0])
                nextV = v - abs(junctions[lastJ][1] - junctions[nextJ][1])             
                if (nextH >= 0 and nextV >= 0) :
                    #print ("  Walking From " + str(lastJ) + " to " + str(nextJ) + " with h " + str(nextH) + " v " + str(nextV))
                    walkPath1(nextH, nextV, junctions, edges, nextJ, visitSet)
            
    


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nhv = input().split()

    n = int(nhv[0])

    h = int(nhv[1])

    v = int(nhv[2])

    junctions = []

    for _ in range(n):
        junctions.append(list(map(int, input().rstrip().split())))

    edges = []

    for _ in range(n-1):
        edges.append(list(map(int, input().rstrip().split())))

    result = solve2(h, v, junctions, edges)
    
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
