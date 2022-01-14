# You are given a date. Your task is to find what the day is on that date.
# A single line of input containing the space separated month, day and year, respectively, in MM/DD/YYYY format.

import calendar

if __name__ == "__main__":
    month, day, year = input().split()
    Day = ""
    
    weekDay = calendar.weekday(int(year), int(month), int(day))
    
    if weekDay == 0:
        Day = "MONDAY"
    if weekDay == 1:
        Day = "TUESDAY"
    if weekDay == 2:
        Day = "WEDNESDAY"
    if weekDay == 3:
        Day = "THURSDAY"
    if weekDay == 4:
        Day = "FRIDAY"
    if weekDay == 5:
        Day = "SATURDAY"
    if weekDay == 6:
        Day = "SUNDAY"  
          
    print(Day)