class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        verbose = True
        output = []
        hashmap = {}
        for i in range(0,len(strs)):
            word = strs[i]
            sorted_word = ''.join(sorted(word))
            if hashmap.get(sorted_word) == None:
                hashmap[sorted_word] = [word]
            else:
                hashmap[sorted_word].append(word)
        return list(hashmap.values())