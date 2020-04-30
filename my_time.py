from datetime import *
START_TIME = 8


class MyTime:
    def __init__(self, day_of_week, time_span):
        self.day_of_week = day_of_week
        self.start_time = time_span[0]
        self.end_time = time_span[1]

    def is_overlap(self, another_time):
        if self.day_of_week != another_time.day_of_week:
            return False
        latest_start = max(self.start_time, another_time.start_time)
        earliest_end = min(self.end_time, another_time.end_time)
        if datetime.combine(date.today(), earliest_end) <= datetime.combine(date.today(), latest_start):
            return False
        return True

    def time_to_table_index(self):
        days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
        column = days_of_week.index(self.day_of_week)
        times_in_day = []
        for i in range(13):
            times_in_day.append(time(START_TIME+i))
        row = [times_in_day.index(self.start_time), times_in_day.index(self.end_time) - 1]
        return row, column

    def __str__(self):
        start_time_without_seconds = self.start_time.strftime("%H:%M")
        end_time_without_seconds = self.end_time.strftime("%H:%M")
        return f"{self.day_of_week} {start_time_without_seconds}-{end_time_without_seconds}"