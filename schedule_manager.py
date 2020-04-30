from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from schedule import Schedule
import random


def clear_layout(layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                clear_layout(item.layout())


class ScheduleManager:
    COLORS = [QColor(238, 79, 249, 150),
              QColor(233, 171, 63, 150),
              QColor(74, 109, 225, 150),
              QColor(62, 175, 192, 150),
              QColor(49, 215, 171, 150),
              QColor(71, 132, 67, 150),
              QColor(237, 247, 88, 150),
              QColor(255, 107, 33, 150),
              QColor(255, 120, 110, 150),
              QColor(54, 26, 101, 150),
              QColor(246, 48, 114, 150),
              QColor(178, 96, 56, 150),
              ]

    def __init__(self, problem_solutions, names_of_course_dict):
        self.names_of_courses_dct = names_of_course_dict
        self._free_colors_lst = list(ScheduleManager.COLORS)
        self._colors_dct = {}
        app = QApplication([])
        q_widget = QWidget()
        q_widget.setWindowTitle("Schedule")
        q_widget.resize(1200, 700)
        layout = QVBoxLayout()
        q_widget.setLayout(layout)
        Schedule.num_of_schedule = -1
        self.put_table_on_app("next", layout, problem_solutions, names_of_course_dict)
        q_widget.show()
        app.exec_()

    def put_table_on_app(self, str_back_or_forward, layout, problem_solutions, names_of_course_dict):
        buttons_layout = QHBoxLayout()
        clear_layout(layout)
        if str_back_or_forward == "back":
            Schedule.num_of_schedule -= 2
        table = Schedule(problem_solutions, names_of_course_dict, self)
        layout.addWidget(table)
        if Schedule.num_of_schedule != 0:
            back = QPushButton("למערכת הקודמת")
            back.clicked.connect(lambda: self.put_table_on_app("back", layout, problem_solutions, names_of_course_dict))
            buttons_layout.addWidget(back)
        if Schedule.num_of_schedule < len(problem_solutions) - 1:
            next_page = QPushButton("למערכת האופציונאלית הבאה!")
            next_page.clicked.connect(lambda: self.put_table_on_app("next", layout, problem_solutions, names_of_course_dict))
            buttons_layout.addWidget(next_page)
        layout.addLayout(buttons_layout)

    def set_course_color(self, course_num):
        if course_num in self._colors_dct.keys():
            return self._colors_dct[course_num]
        if len(self._free_colors_lst) == 0:
            self._free_colors_lst = list(ScheduleManager.COLORS)
        random_index = random.randint(0, len(self._free_colors_lst) - 1)
        color_chosen = self._free_colors_lst[random_index]
        self._colors_dct[course_num] = color_chosen
        self._free_colors_lst.remove(color_chosen)
        return self._colors_dct[course_num]


