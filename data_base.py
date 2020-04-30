from datetime import time
from my_time import MyTime
from itertools import *


def str_into_time(st_of_time):
    day, my_time = st_of_time.strip().rstrip().split()
    start_time, end_time = my_time.split('-')
    start_time_hours, start_time_minutes = start_time.split(':')
    end_time_hours, end_time_minutes = end_time.split(':')
    result = MyTime(day, [time(int(start_time_hours), int(start_time_minutes)),
                          time(int(end_time_hours), int(end_time_minutes))])
    return result


def create_names_of_courses_dict(file_path):
    names_of_courses_dict = {}
    file_object = open(file_path, 'r')
    file_content = file_object.read()
    list_of_courses = file_content.split(',')
    for course in list_of_courses:
        course = course.strip()
        if not course:
            continue
        course_num = course.split(':')[0].strip().rstrip()
        course_name = course.split(':')[1].strip()
        names_of_courses_dict[int(course_num)] = course_name
    return names_of_courses_dict


def create_times_of_courses_dict(f):
    dct = {}
    file_object = open(f, "r")
    file_content = file_object.read()
    lst_of_courses = file_content.split("*")
    for course in lst_of_courses:
        course_number = int(course.split("@")[0].strip())
        if course_number not in dct.keys():
            dct[course_number] = []
        lst_of_times_of_current_course = []
        course_times = course.split("@")[1].strip().rstrip()
        if "," in course_times:
            lst_of_times_of_current_course_str = course_times.split(",")
        else:
            lst_of_times_of_current_course_str = [course_times.strip()]
        for time_of_course_str in lst_of_times_of_current_course_str:
            time_of_course = str_into_time(time_of_course_str.strip().rstrip())
            lst_of_times_of_current_course.append(time_of_course)
        dct[course_number].append(lst_of_times_of_current_course)
    return dct


def get_all_courses_lst(file_path):
    result = []
    file_object = open(file_path, 'r')
    file_content = file_object.read()
    list_of_courses = file_content.split(',')
    for course in list_of_courses:
        course = course.strip()
        if not course:
            continue
        course_num = course.split(':')[0].strip().rstrip()
        result.append(int(course_num))
    return result


class DataBase:
    def __init__(self, names_file, times_file):
        self._names_of_courses_dct = create_names_of_courses_dict(names_file)
        self._all_courses_lst = get_all_courses_lst(names_file)
        self._times_of_courses_dct = create_times_of_courses_dict(times_file)

    def get_all_courses_lst(self):
        return self._all_courses_lst

    def get_names_of_courses_dct(self):
        return self._names_of_courses_dct

    def get_times_of_courses_dct(self):
        return self._times_of_courses_dct






