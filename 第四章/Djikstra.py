# 按路径长度的递增顺序，逐步产生最短路径
# 输入变成改写用fn+ins
# 未开启Numlock时，直接按0进入改写模式，此时用fn+ins退出
import torch


# edge是图的邻接矩阵
# s存放已找到最短路径的点
# path[i]表示 v0 到 vi 的最短路径上顶点 vi 的前一个顶点序号
# dist[i]表示当前找到的从源点 v0 到终点 vi 的最短路径的长度
def djikstra(v0, numberofv, edge):
    # 初始化三个矩阵的值
    s = torch.zeros(numberofv)
    path0 = torch.full((numberofv, 1), -1)  # 都是-1的张量
    dist = torch.full((numberofv, 1), float("inf"))  # 都是inf的张量
    s[v0] = 1     # 表示v0作为源节点
    dist[v0] = 0  # 将v0加入已找到路径的点
    # 修改与v0相邻的点的dist和path0的值
    for i in range(numberofv):
        dist[i] = edge[v0][i]
        if i != v0 and dist[i] < float("inf"):
            # 有向图v0不能到vi用inf表示
            path0[i] = v0  # vi上一个顶点是v0
#     从v0确定n-1条最短路径
    for i in range(numberofv-1):
        minpath, u = float("inf"), v0  # 把赋值放在外面避免没添加s新元素进入第二个循环
        # 选择当前集合中具有最短路径的点u
        for j in range(numberofv):
            if s[j] == 0 and dist[j] < minpath:
                u, minpath = j, dist[j]
        s[u] = 1  # 将最短路径u加入s集合中，表示最短路径已求得
#         新增u后修改dist和path0的元素值
        for k in range(numberofv):
            if s[k] == 0 and edge[u][k] is not float('inf') and edge[u][k] + dist[u] < dist[k]:
                dist[k], path0[k] = edge[u][k] + dist[u], u
    return s, dist, path0


edge1 = torch.tensor(
    [0, float('inf'), 5, 30, float('inf'), float('inf'), 2, 0, float('inf'), float('inf'), 8, float('inf'),
     float('inf'), 15, 0, float('inf'), float('inf'), 7, float('inf'), float('inf'), float('inf'), 0, float('inf'), float('inf'),
    float('inf'), float('inf'), float('inf'), 4, 0, float('inf'),
    float('inf'), float('inf'), float('inf'), 10, 18, 0]
).reshape(6, 6)
print(djikstra(0, 6, edge1))
