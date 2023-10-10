class Solution:
    def capitalizeTitle(self, title: str) -> str:

        title_2_lower = title.lower()

        list_title = title_2_lower.split(" ")
        result = []

        for value in list_title :
            new_str =""
            for k in range(len(value)) :
                if len(value) > 2 :
                    if k == 0 :
                        new_str=chr(ord(value[0]) - 32 ) 
                    else :
                        new_str += value[k]
                else :
                    new_str += value[k]
        
            result.append(new_str)

        return ' '.join(result)