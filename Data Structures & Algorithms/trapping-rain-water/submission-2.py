class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        max_l=height[i]
        max_r=height[j]
        out = [0]*len(height)
        while i<=j:
            #print("i=",i,"j=",j,"max_left=",max_l,"max_right=",max_r)
            if(max_l<=max_r):   
                if(max_l-height[i] > 0):
                    out[i]=max_l-height[i]
                max_l = max(max_l, height[i])
                i=i+1
            else:    
                if(max_r-height[j]>0):
                    out[j]=max_r-height[j]
                max_r = max(max_r, height[j])
                j=j-1
            #print("out=",out)
        return sum(out)
