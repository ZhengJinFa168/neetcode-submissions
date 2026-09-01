class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        if len(word1)>len(word2):
            temp = 0
            for i in range(len(word2)):
                output = output + word1[i]
                output = output + word2[i]
                temp += 1
            output = output + word1[temp:]
        else:
            temp = 0
            for i in range(len(word1)):
                output = output + word1[i]
                output = output + word2[i]
                temp += 1
            output = output + word2[temp:]
        return output

        