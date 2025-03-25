class UnionFind:
    def __init__(self,size):
        self.par = [i for i in range(size)]
        self.rank = [1] * size
    
    def Find(self,x):
        if x != self.par[x]:
            self.par[x] = self.Find([self.par[x])
        return self.par[x]

    def Union(self,x,y):
        rootX, rootY = self.Find(x), self.Find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] > self.rank[rootY]:
            self.par[rootY] = rootX
        elif self.rank[rootY] > self.rank[rootX]:
            self.par[rootX] = rootY
        else:
            self.par[rootY] = rootX
            self.rank[rootX] += 1
        return True
