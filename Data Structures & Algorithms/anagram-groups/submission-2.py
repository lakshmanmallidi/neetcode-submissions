class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = {}
        for strg in strs:
            freqs = [0] * 26
            for char in strg:
                freqs[ord(char) - ord('a')] += 1 
            if tuple(freqs) in freq_map:
                freq_map[tuple(freqs)].append(strg)
            else:
                freq_map[tuple(freqs)] = [strg]
        return list(freq_map.values())