class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:

        preSum = [0]

        for num in nums:
            preSum.append(preSum[-1]+num)

        dq = deque()
        ans = float('inf')

        for i in range(len(preSum)):

            while dq and preSum[i]-preSum[dq[0]] >= k:

                ans = min(ans,i-dq.popleft())

            while dq and preSum[i] <= preSum[dq[-1]]:

                dq.pop()

            dq.append(i)

        return ans if ans!=float('inf') else -1            

        