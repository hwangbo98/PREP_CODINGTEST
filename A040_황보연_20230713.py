class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        mid = len(s) // 2
        front = s[:mid]
        back = s[mid:]
        count_front = 0
        count_back = 0
        for k in front :
            if k in vowel :
                count_front+=1

        for j in back :
            if j in vowel :
                count_back+=1
        
        if count_front == count_back :
            return True
        else :
            return False