class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_pos = []
        occ = {}
        for l in wall:
            temp = []
            prev = 0
            for b in l:
                temp.append(b+prev)
                prev = b + prev        
            edge_pos.append(temp)
        for s in edge_pos:
            for edge in s:
                occ[edge] = occ.get(edge,0) + 1
        max_occ = 0
        i = 0
        for k,v in occ.items():
            if k != edge_pos[0][-1]:
                max_occ = max(v,max_occ)
        return len(wall)-max_occ
        
        
        