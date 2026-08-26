import heapq 
class Solution:
    def lastStoneWeight(self, stones):
        pq = []

        for num in stones :
            heapq.heappush(pq, -num)


        while len(pq) > 1 :
            x = -heapq.heappop(pq)
            y = -heapq.heappop(pq)

            heapq.heappush(pq, y-x) 
        
        return -pq[0] if pq else 0 