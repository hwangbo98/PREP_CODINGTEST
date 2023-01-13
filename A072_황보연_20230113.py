class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int,date.split("-"))
        # month = int(month)
        year_tf = False
        full_m = [1,3,5,7,8,10,12]
        else_m = [4,6,9,11]
        if ((year%4 == 0 and year%100 != 0) or year % 400 == 0) :
            year_tf = True
        else :
            year_tf = False
        result = 0
        if year_tf :
            for k in range(1,month) :
                if k in full_m :
                    result+=31
                elif k in else_m :
                    result+=30
                else :
                    result+=29
            
            result+=day
        else :
            for k in range(1,month) :
                if k in full_m :
                    result+=31
                elif k in else_m :
                    result+=30
                else :
                    result+=28

            result+=day
        