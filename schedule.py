from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView


class Schedule(QTableWidget):
    DAYS_OF_WEEK = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
    START_HOUR = 8
    NUM_OF_DAYS = 5
    NUM_OF_HOURS = 12
    num_of_schedule = -1

    def __init__(self, problem_solutions, dct, schedule_manager):
        QTableWidget.__init__(self)
        Schedule.num_of_schedule += 1
        self.setColumnCount(Schedule.NUM_OF_DAYS)
        self.setRowCount(Schedule.NUM_OF_HOURS)
        for i in range(Schedule.NUM_OF_DAYS):
            self.setHorizontalHeaderItem(i, QTableWidgetItem(str(Schedule.DAYS_OF_WEEK[i])))
        for i in range(Schedule.NUM_OF_HOURS):
            self.setVerticalHeaderItem(i, QTableWidgetItem(
                str(Schedule.START_HOUR + i) + ":00 - " + str(Schedule.START_HOUR + i + 1) + ":00"))
        # headers font
        font = self.horizontalHeader().font()
        font.setPointSize(16)
        self.horizontalHeader().setFont(font)
        font = self.verticalHeader().font()
        font.setPointSize(14)
        self.verticalHeader().setFont(font)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # courses font
        course_fnt = QFont()
        course_fnt.setPointSize(13)
        course_fnt.setFamily("Ariel")
        self.setFont(course_fnt)
        solution = problem_solutions[Schedule.num_of_schedule]
        for course_num in solution:
            if not solution[course_num]:
                continue
            course_color = schedule_manager.set_course_color(course_num)
            for course_time in (solution[course_num]):
                col = course_time.time_to_table_index()[1]
                start_row = course_time.time_to_table_index()[0][0]
                end_row = course_time.time_to_table_index()[0][1]
                self.setSpan(start_row, col, end_row - start_row + 1, 1)
                item = QTableWidgetItem(dct[course_num])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setBackground(course_color)
                self.setItem(start_row, col, item)





