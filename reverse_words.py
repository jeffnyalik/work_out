class Solution:
    def reverseWords(self, s:str)->str:
        if not s:
            return ''
        res = ' '
        i = 0

        while i < len(s):
            while i < len(s) and s[i] == ' ': i+=1
            if i >= len(s): break
            j = i + 1
            while j < len(s) and s[j] != ' ': j+=1
            subs = s[i:j]
            if len(res) == 0: res = subs
            else: res = subs + " " + res
            i = j + 1
        
        return res

cls = Solution()
s = " Good Morning "
print(cls.reverseWords(s))