class Solution:
    def sqrOfDigits(self,n:int)->int:

        sum = 0
        while n>0:

            d = n%10
            n = n//10
            sum += d*d

        return sum

    def isHappy(self, n: int) -> bool:

        slow = n
        fast = n

        while fast != 1:

            slow = self.sqrOfDigits(slow)
            fast = self.sqrOfDigits(fast)
            fast = self.sqrOfDigits(fast)

            if slow == fast and slow != 1:

                return False
            
        return True        


        