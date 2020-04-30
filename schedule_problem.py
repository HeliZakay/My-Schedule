from constraint import Problem


class ScheduleProblem:
    def __init__(self, my_constraints, lst_of_obligatory, lst_of_optional_courses_allowed, number_of_optional_courses, data_base):
        lst_of_all = lst_of_obligatory + lst_of_optional_courses_allowed
        times_of_courses_dct = data_base.get_times_of_courses_dct()
        self._my_constraints = my_constraints
        self._problem = Problem()
        self._my_constraints.set_number_of_choice_classes(number_of_optional_courses)
        for course_number in lst_of_all:
            times_for_course = list(times_of_courses_dct[int(course_number)])
            if course_number in lst_of_optional_courses_allowed:
                times_for_course.append(None)
            self._problem.addVariable(course_number, times_for_course)
        # dummy variable in case no variables in problem
        if not lst_of_all:
            self._problem.addVariable(1, [None])
        self._problem.addConstraint(self._my_constraints.overlap_constraint, lst_of_all)
        if number_of_optional_courses:
            self._problem.addConstraint(self._my_constraints.constraint_exact_number_of_optional_courses, lst_of_optional_courses_allowed)

    def get_problem_solutions(self):
        return self._problem.getSolutions()



