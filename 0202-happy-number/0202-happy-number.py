class Solution:

    def sqrSumDigits(self, n:int) -> int:
            
            sum = 0
            while n >0:
                digits = n%10
                sum += digits*digits
                n = n//10

            return sum

    def isHappy(self, n: int) -> bool:

        slow = n
        fast = n

        while fast !=1:

            slow = self.sqrSumDigits(slow)
            fast = self.sqrSumDigits(fast)
            fast = self.sqrSumDigits(fast)

            if slow == fast and slow!=1: 

                return False

        return True        


        