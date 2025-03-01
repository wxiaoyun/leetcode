from typing import List


class UnionFind:
    parent = None
    size = None

    def __init__(self, size: int):
        self.parent = [i for i in range(size+1)]
        self.size = [1 for _ in range(size+1)]
    
    def find(self, n: int) -> int:
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
    
    def join(self, a: int, b: int) -> None:
        ap = self.find(a)
        bp = self.find(b)

        if ap == bp:
            return
        
        if self.size[ap] > self.size[bp]:
            self.parent[bp] = ap
            self.size[ap] += self.size[bp]
        else:
            self.parent[ap] = bp
            self.size[bp] += self.size[ap]
    
    def is_fully_connected(self) -> bool:
        p = self.parent[1]
        for q in self.parent[1:]:
            if self.find(p) != self.find(q):
                return False
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        auf = UnionFind(n)
        buf = UnionFind(n)

        def connect(t: int, u: int, v: int) -> None:
            if t == 1 or t == 3:
                auf.join(u, v)
            if t == 2 or t == 3:
                buf.join(u, v)

        _3 = []
        _12 = []
        for e in edges:
            if e[0] == 3:
                _3.append(e)
            else:
                _12.append(e)
        _3.extend(_12)

        drop_count = 0
        for t, u, v in _3:
            a_connected = auf.find(u) == auf.find(v)
            b_connected = buf.find(u) == buf.find(v)

            if a_connected and b_connected:
                drop_count += 1
                # print("drop",t,u,v)
                continue # Both graphs can be connected with this edge, so drop it

            if not (a_connected or b_connected):
                connect(t, u, v)
                continue
            
            # exactly a or b is not connected
            if t == 3:
                connect(t, u, v) # no choice
                continue

            if t == 1:
                if a_connected:
                    # print("drop",t,u,v)
                    drop_count += 1
                else:
                    connect(t, u, v)

            if t == 2:
                if b_connected:
                    # print("drop",t,u,v)
                    drop_count += 1
                else:
                    connect(t, u, v)
        # print(auf.parent)
        # print(buf.parent)

        return drop_count if (
            auf.is_fully_connected() and buf.is_fully_connected()
        ) else -1