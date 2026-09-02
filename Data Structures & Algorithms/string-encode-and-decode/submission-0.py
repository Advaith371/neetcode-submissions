class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "?" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 #counts the characters of entire string
        while i < len(s):
            j = i #counter j iterates throguh individual strings
            while s[j] != "?": #loop until you reach special character
                j += 1
            length =  int(s[i:j]) #when special character is reached lenght is between i and j but not including j
            res.append(s[j+1: j +1 + length]) #append al the character from end of ? to s[length]
            i = j + 1 + length
        return res