class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_list = []
        t_list = []
        for s_alphabet in s :
            if s_alphabet == "#" :
                if not s_list :
                    pass
                else :
                    s_list.pop()
            else :
                s_list.append(s_alphabet)

        for t_alphabet in t : 
            if t_alphabet == "#" :
                if not t_list :
                    pass
                else :
                    t_list.pop()

            else :
                t_list.append(t_alphabet)

        count = 0 
        if len(t_list) != len(s_list) :
            return False
        else :
            for k in range(len(s_list)) :
                if s_list[k] == t_list[k] :
                    count+=1

            if count == len(s_list) :
                return True
            else :
                return False