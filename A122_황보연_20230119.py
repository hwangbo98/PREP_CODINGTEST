class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        list_s = list(s)
        dict_s = {}
        dict_t = {}
        list_t = list(t)
        print(list_s, list_t)

        if len(s) == 0 :
            return t
        else :
            for l_s in list_s :
                if l_s in dict_s :
                    dict_s[l_s] +=1
                else :
                    dict_s[l_s] = 1
            for l_t in list_t :
                if l_t in dict_t :
                    dict_t[l_t] +=1
                else :
                    dict_t[l_t] = 1
                
        for key, val in dict_t.items() :
            try :
                if dict_s[key] != dict_t[key] :
                    return key
            except KeyError :
                return key