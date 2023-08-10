import datetime

# point1: need to figure out the number of days between start and end
# point2: if ambiguous, need to figure out the number of weekends from 0000-01-01 to start_date and to end_date

# assumption1: the format of start_date and end_date is 'year-month-day', string
# assumption2: if the end_date is null, the end_date will be today
# assumption3: 0001-01-01 is Monday


class SlaCalculator: # is it allowed to use datetime package? if no
    def __init__(self):
        self.days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def is_within(self, start_date: str, end_date: str or None) -> bool:
        if not end_date:
            end_date = str(datetime.datetime.now().date())  # '2023-08-09'

        start_total_days = self.total_days(start_date)  # int
        end_total_days = self.total_days(end_date)  # int
        days_gap = end_total_days - start_total_days + 1
        # print(days_gap)

        if days_gap > 11:  # [6,7,1,2,3,4,5,6,7,1,2] maximum range
            return False
        if days_gap <= 9:  # [1,2,3,4,5,6,7,1,2]
            return True
        # if [10, 11] need to figure out the numbers of weekends
        start_total_weekends = start_total_days // 7 * 2
        start_total_weekends += max(0, start_total_days % 7 - 5)

        end_total_weekends = end_total_days // 7 * 2
        end_total_weekends += max(0, start_total_days % 7 - 5)

        if days_gap - (end_total_weekends - start_total_weekends) <= 7:
            return True
        else:
            return False

    def lunar_year(self, year: int):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return True
        return False

    def total_days(self, date: str):
        years, months, days = map(int, date.split('-'))
        day_count = 0

        # calculate years
        for year in range(1, years):  # [1, 2022] if years = 2023
            if self.lunar_year(year):
                day_count += 365 + 1
            else:
                day_count += 365

        # calculate months
        for month in range(1, months):  # [1, 2, 3] if months = 4
            if month == 2 and self.lunar_year(years):
                day_count += self.days_in_month[month] + 1
            else:
                day_count += self.days_in_month[month]

        # calculate days
        day_count += days

        return day_count


s = SlaCalculator()
start_date = '2020-02-19'
end_date = '2020-02-29'
print(s.is_within(start_date, end_date))







