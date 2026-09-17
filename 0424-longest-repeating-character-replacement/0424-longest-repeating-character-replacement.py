class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low = 0
        res = 0 
        freq = {}

        for high in range(len(s)):

            freq[s[high]] = freq.get(s[high] , 0)+1

            max_cnt = max(freq.values()) # maximum freq count
            length =  high -low+1        # lenght of the freq 
            diff = length - max_cnt

            while diff > k :

                freq[s[low]] -=1
                low+=1
                max_cnt = max(freq.values()) # maximum freq count
                length =  high -low+1        # lenght of the freq 
                diff = length - max_cnt

            if diff <= k:

                length = high- low+1
                res = max(res , length)

        return res            
    


        