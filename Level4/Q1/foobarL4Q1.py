import copy

class Graph():
    def __init__(self,matrix):
        self.graphMatrix = matrix
        self.inf = float("Inf")
        self.V = len(matrix)
        self.distances = [[self.inf for _ in range(self.V)] for _ in range(self.V)]

    def bellmenford(self):
        # return bool value 
        for source in range(self.V):
            self.distances[source][source]=0
            for _ in range(self.V-1):
                for u in range(self.V):
                    for v in range(self.V):
                        if (self.graphMatrix[u][v] + self.distances[source][u]) < self.distances[source][v] :
                            self.distances[source][v]=(self.graphMatrix[u][v] + self.distances[source][u])

            for u in range(self.V):
                for v in range(self.V):
                    if (self.graphMatrix[u][v] + self.distances[source][u]) < self.distances[source][v] :
                        #Negative cycle detected
                        return True 
        # No Negative cycle
        return False

    def allPossiblePaths(self,times_limit):
        end=self.V-1
        start=0
        stack =[(start, [start], times_limit,[[i] for i in range(self.V)])]
        # stack of (current vertex,path we travelled from start to this vertex, time left, matrix to not stuck in zero weight Loop)
        allVertex=set(range(self.V))
        while stack:
            (curr,path,time,curRemoveZeroLoop)=stack.pop()
            for nex in allVertex-set(curRemoveZeroLoop[curr]):
                timToNext = self.distances[curr][nex]
                timBack = self.distances[nex][curr]
                timToGoal =self.distances[nex][end]
                removeZeroLoop = copy.deepcopy(curRemoveZeroLoop)
                if timToNext + timBack == 0:
                    removeZeroLoop[curr].append(nex)
                    removeZeroLoop[nex].append(curr)

                if (0 <= time - timToNext -timToGoal):
                    nexPath = path +[nex]
                    nexTime = time - timToNext
                    stack.append((nex,nexPath,nexTime,removeZeroLoop))
                    if nex == end:
                        yield set(nexPath)
                        if len(set(nexPath)) ==self.V:
                            return

def solution(times, times_limit):
    # Your code here
    g1=Graph(times)
    V=len(times)
    if V<3:
        return []
    maxFreeBunnies=set([])
    if g1.bellmenford(): 
        # Negative cycle detected
        return range(V-2)
    else:
        # No negative cycle
        # Since there is no negative cycle Eventually The Door will close permanantly in finite time and we itrate to all possible path
        for freedBunnies in g1.allPossiblePaths(times_limit):
            if (len(maxFreeBunnies) < len(freedBunnies)) or ((len(maxFreeBunnies) == len(freedBunnies)) and (sum(maxFreeBunnies) > sum(freedBunnies)) ):
                maxFreeBunnies = freedBunnies

    return map(lambda x : x-1, sorted(maxFreeBunnies-set([0,V-1])))
