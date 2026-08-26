class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        max_len = 0
        for num in nums:
            sub_seq = []
            #print("num:",num)
            if num-1 not in hashset:
                #print("num-1:", num-1)
                sub_seq.append(num)
                while True:
                    if num+1 in hashset:
                        sub_seq.append(num+1)
                        num = num+1
                    else:
                        break
                #print(sub_seq)
                curr_len = len(sub_seq)
                #print('curr_len:', curr_len," max len:", max_len)
                if curr_len > max_len:
                    max_len = curr_len
        return max_len

