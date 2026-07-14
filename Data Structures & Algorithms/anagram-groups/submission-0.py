class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for strg in strs:
            counter = [0]*26
            for letter in strg:
                counter[ord(letter)-ord('a')] = counter[ord(letter)-ord('a')] + 1
            if tuple(counter) in hash_map:
                hash_map[tuple(counter)].append(strg)
            else:
                hash_map[tuple(counter)] = [strg]
        return list(hash_map.values())