#For printing a whole year calendar.
import calendar

year = 2025
print(calendar.TextCalendar().formatyear(year))

#For printing a specific month of a specific year

month = 2
print(calendar.month(year, month))