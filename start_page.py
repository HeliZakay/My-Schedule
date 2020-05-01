from tkinter import DISABLED, NORMAL
from PIL import Image, ImageTk
from constraint import Problem
from my_check_button import *
import my_constraints as mc
import tkinter.font as font
from scrollable_frame import ScrollableFrame


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.canvas = tk.Canvas(self, width=1500, height=900)
        self.canvas.pack()
        pil_img = Image.open(r"pictures\landscape1.jpg")
        self.img = ImageTk.PhotoImage(pil_img.resize((1500, 900), Image.ANTIALIAS))
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
        self._data_base = self.controller.get_data_base()
        self._dct_of_names = self._data_base.get_names_of_courses_dct()
        self._list_of_all_courses = self._data_base.get_all_courses_lst()
        self._checkbox_buttons = {}
        new_frame = ScrollableFrame(self)
        row_to_pack_checkbutton = 1
        for course_num in self._list_of_all_courses:
            course = MyCheckButton(self, self._dct_of_names, new_frame.scrollable_frame, course_num)
            self._checkbox_buttons[course_num] = course
            course.grid(row=row_to_pack_checkbutton, column=0)
            row_to_pack_checkbutton += 1
        text_label = tk.Label(self, text="!היי, כאן תבחרו קורסי חובה")
        text_label.config(font=("Ariel", 20))
        self.canvas.create_window(520, 20, anchor=tk.NW, window=text_label)
        self.canvas.create_window(450, 160, anchor=tk.NW, window=new_frame)
        button = tk.Button(self, text="!הבא", fg='blue', command=lambda: self.controller.switch_to_frame_two(self, self._checkbox_buttons))
        my_font = font.Font(size=20)
        button['font'] = my_font
        self.canvas.create_window(650, 810, anchor=tk.NW, window=button)
        self._exception_label = tk.Label(self, text="")
        self._exception_label.pack(side=tk.BOTTOM)

    def on_check(self, button_checked):
        if button_checked.get_bool_var():
            button_checked['fg'] = 'green'
            dct_of_times = self._data_base.get_times_of_courses_dct()
            course_times = dct_of_times[button_checked.get_course_num()]
            for number_of_course, button in self._checkbox_buttons.items():
                if button != button_checked:
                    time_of_other_course = dct_of_times[number_of_course]
                    p = Problem()
                    p.addVariable(button_checked.get_course_num(), course_times)
                    p.addVariable(number_of_course, time_of_other_course)
                    my_constraints = mc.MyConstraints(self._data_base)
                    p.addConstraint(my_constraints.overlap_constraint, [button_checked.get_course_num(), number_of_course])
                    if not p.getSolutions():
                        button_checked.add_to_list_of_disabled(button)
                        button.increment_how_many_disable_me()
                        button.config(state=DISABLED)
        else:
            button_checked['fg'] = 'white'
            for disabled_button in button_checked.get_list_of_disabled():
                disabled_button.decrement_how_many_disable_me()
                if disabled_button.get_how_many_disable_me() == 0:
                    disabled_button.config(state=NORMAL)
            button_checked.clear_list_of_disabled()

    def set_exception_label(self, new_text):
        self._exception_label.pack_forget()
        self._exception_label = tk.Label(self, text=new_text)
        self._exception_label.config(font=("Ariel", 14), pady=25)
        self.canvas.create_window(410, 700, anchor=tk.NW, window=self._exception_label)

























