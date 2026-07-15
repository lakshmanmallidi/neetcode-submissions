class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_od = sorted(nums)
        result = []
        #print("******************")
        #print(nums_od)
        #print("******************")
        #[-4,-1,-1,0,1,2]
        #  0  1  2 3 4 5
        prev_i = None
        for i in range(0,len(nums_od)-2):
            if nums_od[i] == prev_i:
                continue
            else:
                prev_i = nums_od[i]
            j = i+1
            k = len(nums_od)-1
            while j<k:
                #print(nums_od[i],nums_od[j],nums_od[k])
                s = nums_od[i]+nums_od[j]+nums_od[k]
                if(s>0):
                    k = k-1
                elif(s<0):
                    j = j+1
                else:
                    #print("matched", nums_od[i], nums_od[j], nums_od[k],i,j,k)
                    result.append([nums_od[i], nums_od[j], nums_od[k]])
                    j=j+1
                    k=k-1
                    while j<k and nums_od[j]==nums_od[j-1] and nums_od[k]==nums_od[k+1]:
                        j=j+1
                        k=k-1
            #print("----------------------------")
        return result

