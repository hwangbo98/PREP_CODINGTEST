class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        result = []
        for alpha in s :
            if (96< ord(alpha) < 123) or (47 < ord(alpha) <58) :
                result.append(alpha)
        

        print(result)
        new_s = ''.join(result)
        reverse_s = ""
        for k in reversed(result) :
            reverse_s+=k
        print(reverse_s)
        if new_s == reverse_s :
            return True

        else :
            return False