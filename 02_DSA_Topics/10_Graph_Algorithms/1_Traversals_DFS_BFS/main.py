from collections import deque
def dfs(adj, s):
    n=len(adj); seen=[False]*n; out=[]
    def go(u):
        seen[u]=True; out.append(u)
        for v in adj[u]:
            if not seen[v]: go(v)
    go(s); return out
def bfs(adj, s):
    n=len(adj); seen=[False]*n; out=[]; dq=deque([s]); seen[s]=True
    while dq:
        u=dq.popleft(); out.append(u)
        for v in adj[u]:
            if not seen[v]: seen[v]=True; dq.append(v)
    return out
if __name__=="__main__":
    g=[[1,2],[0,3],[0,3],[1,2]]
    print("DFS:", dfs(g,0))
    print("BFS:", bfs(g,0))
