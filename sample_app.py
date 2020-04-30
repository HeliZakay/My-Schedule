from page_two import PageTwo, create_list_of_courses_checked
from schedule_problem import ScheduleProblem
from schedule_manager import ScheduleManager
from start_page import *
import data_base as db
import time
import my_constraints as mc


class SampleApp(tk.Tk):
    NAMES_FILE = r"courses\fake_names.txt"
    TIMES_FILE = r"courses\courses.txt"

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1500x900")
        self._data_base = db.DataBase(SampleApp.NAMES_FILE, SampleApp.TIMES_FILE)
        self._my_constraints = mc.MyConstraints(self._data_base)
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.start_page = StartPage(parent=self.container, controller=self)
        self.switch_to_frame_one()

    def switch_to_frame_one(self):
        new_frame = self.start_page
        new_frame.grid(row=0, column=0, sticky="nsew")
        new_frame.tkraise()

    def get_data_base(self):
        return self._data_base

    def switch_to_frame_two(self, frame, checkbox_buttons):
        if not self.problem_can_be_solved(checkbox_buttons):
            frame.set_exception_label("אוופססס :)))... אתם יודעים מה, הקורסים מתנגשים בשעות, סורי")
        else:
            self.start_page = frame
            list_of_courses_checked = create_list_of_courses_checked(checkbox_buttons)
            new_frame = PageTwo(list_of_courses_checked, parent=self.container, controller=self)
            new_frame.grid(row=0, column=0, sticky="nsew")
            new_frame.tkraise()

    def switch_to_page_three(self, frame2, dct_of_checkbox, combo, list_of_courses_checked):
        num_of_optional = combo.get()
        try:
            number_of_optional_courses = int(num_of_optional)
        except (ValueError, TypeError):
            frame2.set_exception_label("...חמודים, אתם חייבים להכניס כמה קורסי בחירה תרצו")
        else:
            lst_of_optional_courses_allowed = create_list_of_courses_checked(dct_of_checkbox)
            if number_of_optional_courses > len(dct_of_checkbox.keys()):
                frame2.set_exception_label("...לא ניתן לבחור יותר קורסים ממה שמוצע במאגר")
            elif number_of_optional_courses > len(lst_of_optional_courses_allowed):
                frame2.set_exception_label("? :)סמנו יותר קורסים... סבבה")
            else:
                problem = ScheduleProblem(self._my_constraints, list_of_courses_checked, lst_of_optional_courses_allowed,
                                          number_of_optional_courses, self._data_base)
                problem_solutions = problem.get_problem_solutions()
                if not problem_solutions and number_of_optional_courses != 0:
                    frame2.set_exception_label("""אתם אנשים עם דרישות גבוהות :) מצטערים, אבל לא הצלחנו לבנות לכם מערכת.
                        בבקשה בחרו קורסים אחרים :) """)
                else:
                    frame2.set_exception_label("")
                    ScheduleManager(problem_solutions, self._data_base.get_names_of_courses_dct())

    def problem_can_be_solved(self, checkbox_buttons):
        lst_of_optional_courses_allowed = create_list_of_courses_checked(checkbox_buttons)
        if not lst_of_optional_courses_allowed:
            return True
        times_of_courses_dct = self._data_base.get_times_of_courses_dct()
        p = Problem()
        for course_number in lst_of_optional_courses_allowed:
            p.addVariable(course_number, times_of_courses_dct[course_number])
        my_constraints = mc.MyConstraints(self._data_base)
        p.addConstraint(my_constraints.overlap_constraint, lst_of_optional_courses_allowed)
        if p.getSolutions():
            return True
        return False
