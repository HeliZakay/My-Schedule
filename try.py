from data_base import *

db = DataBase(r'C:\Users\User\Desktop\fake_names.txt', r'C:\Users\User\Desktop\courses.txt')
reversed_dct = db.get_reversed_dct()
d = db.get_times_of_courses_dct()
t = d[455350501]
print(reversed_dct[tuple(t)])

