import itertools as it
import time


def are_courses_overlap(time1, time2):
    return len([1 for item1 in time1 for item2 in time2 if item1.is_overlap(item2)]) != 0


class MyConstraints:
    def __init__(self, data_base):
        self._data_base = data_base
        self._num_of_choice_classes = 0
        self._sum_due_to_overlap = 0
        self._sum_due_to_exact_choice = 0
        self._count_overlap_constraint_calls = 0
        self._overlap_matrix = {}

    def overlap_constraint(self, *args):
        start_time = time.time()
        for comb in it.combinations(list(args), 2):
            if (comb[0] and comb[1]) and (are_courses_overlap(comb[0], comb[1])):
                if time.time() - start_time != 0:
                    self._count_overlap_constraint_calls += 1
                    self.increase_sum_due_to_overlap(time.time() - start_time)
                return False
        if time.time() - start_time != 0:
            self._count_overlap_constraint_calls += 1
            print(f"call took {time.time() - start_time}")
            self.increase_sum_due_to_overlap(time.time() - start_time)
        return True

    def increase_sum_due_to_overlap(self, amount):
        self._sum_due_to_overlap += amount

    def increase_sum_due_to_exact_choice(self, amount):
        self._sum_due_to_exact_choice += amount

    def get_sum_due_to_overlap(self):
        return self._sum_due_to_overlap

    def get_sum_due_to_exact_choice(self):
        return self._sum_due_to_exact_choice

    def get_count_overlap_constraint_calls(self):
        return self._count_overlap_constraint_calls

    def set_number_of_choice_classes(self, number):
        self._num_of_choice_classes = number

    def constraint_exact_number_of_optional_courses(self, *args):
        start_time = time.time()
        my_sum = len([value for value in list(args) if value])
        if int(self._num_of_choice_classes) == my_sum:
            self.increase_sum_due_to_exact_choice(time.time() - start_time)
            return True
        else:
            self.increase_sum_due_to_exact_choice(time.time() - start_time)
            return False
