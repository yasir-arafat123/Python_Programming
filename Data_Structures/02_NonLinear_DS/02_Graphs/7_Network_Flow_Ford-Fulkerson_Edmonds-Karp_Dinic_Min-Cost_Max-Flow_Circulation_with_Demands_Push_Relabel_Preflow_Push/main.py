from collections import deque
def edmonds_karp(n, cap, s, t):
    flow=0
    while True:
        parent=[-1]*n; parent[s]=s; q=deque([s])
        while q and parent[t]==-1:
            u=q.popleft()
            for v in range(n):
                if parent[v]==-1 and cap[u][v]>0:
                    parent[v]=u; q.append(v)
        if parent[t]==-1: break
        v=t; aug=float('inf')
        while v!=s:
            u=parent[v]; aug=min(aug, cap[u][v]); v=u
        v=t
        while v!=s:
            u=parent[v]; cap[u][v]-=aug; cap[v][u]+=aug; v=u
        flow+=aug
    return flow
if __name__=="__main__":
    n=4; s,t=0,3
    cap=[[0,3,2,0],[0,0,2,2],[0,0,0,3],[0,0,0,0]]
    print("max flow:", edmonds_karp(n, cap, s, t))
