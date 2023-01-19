from datetime import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        which_day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
        date = str(year) +"-" + str(month) + "-" + str(day) 

        datetime_date = datetime.strptime(date, "%Y-%m-%d")

        yoil = datetime_date.weekday()

        return which_day[yoil]