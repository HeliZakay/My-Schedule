import tkinter as tk
from tkinter import font as tk_font


class MyCheckButton(tk.Checkbutton):
    def __init__(self, frame, dct_of_names, inner_frame_scrollable, course_num):
        self._course_num = course_num
        self._c_var = tk.BooleanVar()
        self._how_many_disable_me = 0
        self._list_of_disabled = []
        checkbox_font = tk_font.Font(family='Helvetica', size=15, weight='bold')
        super().__init__(inner_frame_scrollable, disabledforeground='grey', command=lambda: frame.on_check(self), pady=25, text=dct_of_names[int(course_num)], font=checkbox_font, variable=self._c_var)

    def get_bool_var(self):
        return self._c_var.get()

    def get_course_num(self):
        return int(self._course_num)

    def increment_how_many_disable_me(self):
        self._how_many_disable_me += 1

    def decrement_how_many_disable_me(self):
        self._how_many_disable_me -= 1

    def get_how_many_disable_me(self):
        return self._how_many_disable_me

    def get_list_of_disabled(self):
        return self._list_of_disabled

    def clear_list_of_disabled(self):
        self._list_of_disabled.clear()

    def add_to_list_of_disabled(self, button):
        self._list_of_disabled.append(button)











