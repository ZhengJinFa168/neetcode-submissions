class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        verbose = True
        output = []
        hashmap = {}
        for i in range(0,len(strs)):
            word = strs[i]
            sorted_word = ''.join(sorted(word))
            len_output = len(output)
            if hashmap.get(sorted_word) == None:
                hashmap[sorted_word] = len_output
                output.append([word])
            else:
                pos = hashmap.get(sorted_word)
                output[pos].append(word)
        return output

                
                         
            
