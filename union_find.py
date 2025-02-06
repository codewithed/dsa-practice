class UnionFind:
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def Find(self,n):
        if n != self.par(n):
            self.par[n] = self.Find([self.par[n])
            n = self.par[n]
        return n

    def Union(self,x,y):
        p1,p2 = self.Find(x),self.Find(y)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += p1
        return True
