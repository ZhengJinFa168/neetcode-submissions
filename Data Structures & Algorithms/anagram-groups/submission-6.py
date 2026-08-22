class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        output = []
        for i in range(len(strs)):
            s = strs[i]
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1    
            len_output = len(output)
            if res.get(tuple(count)) == None:
                res[tuple(count)] = len_output
                output.append([s])
            else:
                output[res[tuple(count)]].append(s)
        return output