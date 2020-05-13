""""
Item 37: compose classes instead of nesting many levels of built-in types
"""

from collections import defaultdict
from collections import namedtuple


# Nested Dictionaries
class WeightedGradebook_NestedDicts:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = defaultdict(list)

    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject = self._grades[name]
        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                subject_avg += score * weight
                total_weight += weight
            score_sum += subject_avg / total_weight
            score_count += 1
        return score_sum / score_count


# Composition of classes

Grade = namedtuple('Grade', ('score', 'weight'))


class Subject:
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        score_sum, total_weight = 0, 0
        for score, weight in self._grades:
            score_sum += score * weight
            total_weight += weight
        return score_sum / total_weight


class Student:
    def __init__(self):
        self._subjects = defaultdict(Subject)

    def get_subject(self, subject):
        return self._subjects[subject]

    def average_grade(self):
        score_sum, subject_count = 0, 0
        for subject in self._subjects.values():
            score_sum += subject.average_grade()
            subject_count += 1
        return score_sum / subject_count


class GradeBook:
    def __init__(self):
        self._students = defaultdict(Student)

    def get_student(self, name):
        return self._students[name]


if __name__ == '__main__':
    # Nested Dictionaries
    book = WeightedGradebook_NestedDicts()
    book.add_student('Tom')
    book.report_grade('Tom', 'Math', 75, 0.05)
    book.report_grade('Tom', 'Math', 65, 0.15)
    book.report_grade('Tom', 'Math', 70, 0.80)
    book.report_grade('Tom', 'Gym', 100, 0.40)
    book.report_grade('Tom', 'Gym', 85, 0.60)
    print(book.average_grade('Tom'))

    # Composition of classes
    book = GradeBook()
    tom = book.get_student('Tom')
    math = tom.get_subject('Math')
    math.report_grade(75, 0.05)
    math.report_grade(65, 0.15)
    math.report_grade(70, 0.80)
    gym = tom.get_subject('Gym')
    gym.report_grade(100, 0.40)
    gym.report_grade(85, 0.60)
    print(tom.average_grade())