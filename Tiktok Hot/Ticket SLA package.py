import datetime

# point1: need to figure out the number of days between start and end
# point2: if ambiguous, need to figure out the number of weekends from 0000-01-01 to start_date and to end_date


class SlaCalculator: # is it allowed to use datetime package? if yes

    def is_within(self, start_date: str, end_date: str or None) -> bool:
        start_year, start_month, start_day = map(int, start_date.split('-'))
        start = datetime.date(start_year, start_month, start_day)

        if not end_date:
            end = datetime.datetime.now().date()  # '2023-08-09'
        else:
            end_year, end_month, end_day = map(int, end_date.split('-'))
            end = datetime.date(end_year, end_month, end_day)
        print(start, end)

        days_gap = end - start
        print(days_gap)
        days_difference = days_gap.days + 1
        print(days_difference)

        if days_difference > 11:
            return False
        if days_difference <= 9:
            return True

        # if we need to calculate the weekends
        weekend_count = 0
        current_day = start
        while current_day <= end:
            if current_day.weekday() in (5, 6):
                weekend_count += 1
            current_day += datetime.timedelta(days=1)
        print(weekend_count)

        if days_difference - weekend_count <= 7:
            return True
        return False


s = SlaCalculator()
start_date = '2023-8-1'
end_date = '2023-8-10'
test = s.is_within(start_date, end_date)
print(test)