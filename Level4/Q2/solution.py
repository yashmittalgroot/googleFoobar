def updatePath(entrances, exits, path):
    V1=len(path)
    entrancesSet=set(entrances)
    exitsSet=set(exits)
    midSet = set(range(V1)) - entrancesSet - exitsSet
    V=V1-len(entrances)-len(exits)+2
    pathModified = [[0 for _ in range(V1)]for _ in range(V)]
    for i in entrancesSet:
        pathModified[0] = [pathModified[0][j]+path[i][j] for j in range(V1)]
    for i in exitsSet:
        pathModified[V-1] = [pathModified[V-1][j]+path[i][j] for j in range(V1)]
    for ind,i in enumerate(midSet):
        pathModified[ind+1]=[path[i][j] for j in range(V1)]
    pathModified1 = [[0 for _ in range(V)]for _ in range(V)]
    #if error check this
    for j in range(V):
        for i in entrancesSet:
            pathModified1[j][0] = pathModified1[j][0]+pathModified[j][i]
        for i in exitsSet:
            pathModified1[j][V-1] = pathModified1[j][V-1]+pathModified[j][i]
        for ind,i in enumerate(midSet):
            pathModified1[j][ind+1]=pathModified[j][i]
    return pathModified1

class Graph:
    def __init__(self,graph):
        self.graph=graph
        self.V=len(graph)
    
    def BFS(self,s,t,parent):
        #needed to check if there is a path or not
        #also need if path is possible from source to sink than
        #we need one complete path and  update all 
        queue=[]
        queue.append(s)
        visited=[False for _ in range(self.V)]
        visited[s]=True
        while(queue):
            u=queue.pop(0)
            for v,val in enumerate(self.graph[u]):
                if val>0 and not visited[v]:
                    queue.append(v)
                    visited[v]=True
                    parent[v]=u
        return visited[t]        
    
    def fulk(self):
        s=0
        t=self.V-1
        max_flow=0
        parent=[0 for _ in range(self.V)]
        flow = float("Inf")
        while self.BFS(s,t,parent):
            temp=t
            while(temp!=s):
                flow = min(flow,self.graph[parent[temp]][temp])
                temp=parent[temp]
            max_flow+=flow
            temp=t
            while(temp!=s):
                self.graph[parent[temp]][temp]-=flow
                self.graph[temp][parent[temp]]+=flow
                temp=parent[temp]
            
        
        return max_flow
def solution(entrances, exits, path):
    # Your code here
    matrix = updatePath(entrances, exits, path)
    g=Graph(matrix)
    return g.fulk()
    
