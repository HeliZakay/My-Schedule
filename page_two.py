from PIL import ImageTk, Image
from my_check_button import MyCheckButton
import tkinter as tk
from tkinter import ttk, font
from scrollable_frame import ScrollableFrame


def create_list_of_courses_checked(check_buttons):
    lst = []
    for course_num, checkButton in check_buttons.items():
        if checkButton.get_bool_var():
            lst.append(int(course_num))
    return lst


def on_check(button):
    if button.get_bool_var():
        button['fg'] = 'green'
    else:
        button['fg'] = 'white'


class PageTwo(tk.Frame):
    def __init__(self, list_of_courses_checked, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.canvas = tk.Canvas(self, width=1500, height=900)
        self.canvas.pack()
        pil_img = Image.open(r"pictures\beach-hd-background.jpg")
        self.img = ImageTk.PhotoImage(pil_img.resize((1500, 900), Image.ANTIALIAS))
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
        self._data_base = self.controller.get_data_base()
        self._text_label = tk.Label(self, text="")
        self._text_label.config(font=("Courier", 20))
        dct_of_course_names = self._data_base.get_names_of_courses_dct()
        list_of_all_courses = self._data_base.get_all_courses_lst()
        entry_label = tk.Label(self, text="?כמה קורסי בחירה תרצו")
        entry_label.config(font=("Ariel", 20))
        self.canvas.create_window(670, 20, anchor=tk.NW, window=entry_label)
        number_of_courses_to_choose_from = len(list_of_all_courses) - len(list_of_courses_checked)
        combo = ttk.Combobox(self, width=13, values=[str(num) for num in range(number_of_courses_to_choose_from + 1)],
                             font=("Ariel", 14))
        self.canvas.create_window(450, 20, anchor=tk.NW, window=combo, height=45)
        text_label = tk.Label(self, text="בבקשה סמנו לנו קורסי בחירה שנבחר לכם מתוכם ")
        text_label.config(font=("Ariel", 16))
        self.canvas.create_window(450, 150, anchor=tk.NW, window=text_label)
        new_frame = ScrollableFrame(self)
        self.canvas.create_window(450, 200, anchor=tk.NW, window=new_frame)
        self._checkbox_buttons = {}
        for course_num in list_of_all_courses:
            if course_num not in list_of_courses_checked:
                course = MyCheckButton(self, dct_of_course_names, new_frame.scrollable_frame, course_num)
                self._checkbox_buttons[course_num] = course
                course.pack()
        button = tk.Button(self, text="!הבא- תראו לי מערכת", fg='blue',
                           command=lambda: self.controller.switch_to_page_three(self, self._checkbox_buttons, combo,
                                                                       list_of_courses_checked))
        my_font = font.Font(size=16)
        button['font'] = my_font
        self.canvas.create_window(450, 700, anchor=tk.NW, window=button)
        button2 = tk.Button(self, text="חזור אחורה", command=lambda: self.controller.switch_to_frame_one())
        button2['font'] = my_font
        self.canvas.create_window(830, 700, anchor=tk.NW, window=button2)

    def set_exception_label(self, new_text):
        self._text_label.pack_forget()
        self._text_label = tk.Label(self, text=new_text, width=60)
        self._text_label.config(font=("Ariel", 16))
        self.canvas.create_window(280, 800, anchor=tk.NW, window=self._text_label)

    def on_check(self, button):
        on_check(button)
