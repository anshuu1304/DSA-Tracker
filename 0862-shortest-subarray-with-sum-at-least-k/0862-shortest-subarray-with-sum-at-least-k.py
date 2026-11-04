class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:

        pSum = [0]

        for num in nums:
            pSum.append(pSum[-1]+num)

        dq = deque()    
        ans = float('inf')
        
        for i in range(len(pSum)):

            while dq and pSum[i] - pSum[dq[0]] >= k:
                ans = min(ans , i-dq.popleft())

            while dq and pSum[i] < pSum[dq[-1]]:
                dq.pop()

            dq.append(i)

        return ans if ans!=float('inf') else -1        