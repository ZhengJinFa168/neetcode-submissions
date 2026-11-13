class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = []
        time = 0
        q = deque()
        for k,v in count.items():
            heapq.heappush(heap,-v)
        print(heap)
        while heap or q:
            time += 1
            if not heap:
                time = q[0][1]
            else:
                v = heapq.heappop(heap) + 1
                if v < 0:
                    q.append([v,time + n])
            if q and q[0][1] == time:
                heapq.heappush(heap,q.popleft()[0])
            
        return time