class Solution:
    def minWindow(self, s: str, t: str) -> str:

        low = 0 
        res = ""
        min_len = float('inf')

        freq1 = {}
        freq2 = {}
        count = 0

        for char in t:
            freq2[char] = freq2.get(char , 0)+1

        for high in range(len(s)):

            freq1[s[high]] = freq1.get(s[high] , 0)+1

            if s[high] in freq2 and freq1[s[high]] <= freq2[s[high]]:

                count +=1

            while count == len(t):

                length = high-low+1

                if length < min_len:
                    min_len = length
                    res = s[low:high+1]

                if s[low] in freq2 and freq1[s[low]] <= freq2[s[low]]:

                    count-=1

                freq1[s[low]] -= 1
                
                if freq1[s[low]] == 0:
                    del  freq1[s[low]]   

                low+=1
                
        return res                
        