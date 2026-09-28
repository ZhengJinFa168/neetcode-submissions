class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap)>1:
            heaviest = -heapq.heappop(maxHeap)
            second = -heapq.heappop(maxHeap)
            diff = heaviest - second
            if diff != 0:
                heapq.heappush(maxHeap,-diff)
        if not maxHeap:
            return 0
        return -heapq.heappop(maxHeap)
