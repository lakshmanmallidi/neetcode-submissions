from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = 0
        total_bananas = 0
        for i in range(0, len(piles)):
            if piles[i] > max_pile:
                max_pile = piles[i]
            total_bananas = total_bananas + piles[i]
        abs_minimum_rate = ceil(total_bananas/h)
        #rates = [rate for rate in range(abs_minimum_rate, max_pile+1)]
        i=1
        j=max_pile
        minimum_rate = max_pile
        while i<=j:
            m=(i+j)//2
            hours = 0
            for pile in piles:
                hours = hours+ceil(pile/m)
            #print("m=",m,"i=",i,"j=",j,"hours=",hours)
            if hours > h:
                i=m+1
            else:
                if m < minimum_rate:
                    minimum_rate = m
                j=m-1
        return minimum_rate