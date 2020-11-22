"""
    Author: Mahir Dhall
    Name: Homework11
    Description: This class creates a data repository of courses, students,
    and instructors. The system will be used to help students track their
    required courses, the courses they have successfully completed,
    their grades, GPA, etc. The system will also be used by faculty advisors
    to help students to create study plans.
"""


from collections import defaultdict
import sqlite3
from typing import DefaultDict, IO, Iterator, List, Tuple
from prettytable import PrettyTable
from os import path
import sqlite3


class FileReader:
    """ This class contains file reader function to parse data from the input
        files
        Function - print_pretty_table() to print the three pretty tables
    """

    def valid_string(self, string: str) -> bool:
        """ This helper function validates an input string """
        if not isinstance(string, str) or len(string) == 0:
            raise TypeError(
                "Error: input should be of type string and non empty")
        return True

    def file_reader(self, path: str, fields: int, sep: str = ',',
                    header: bool = False) -> Iterator[List[str]]:
        """ Reads text files with a fixed number of fields,
            separated by a specific character seperator and returns an iterator
            object with list of fields as string
        """
        self.valid_string(path)
        self.valid_string(sep)

        try:
            my_file: IO = open(path, "r")
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: File not found at path - {path}")
        else:
            with my_file:
                line_number: int = 1
                while True:
                    try:
                        if header and line_number == 1:
                            next(my_file)
                        curr_line: str = next(my_file).rstrip('\n')
                    except StopIteration:
                        break
                    curr_list: List[str] = [word.strip()
                                            for word in curr_line.split(sep)]
                    curr_len: int = len(curr_list)
                    if curr_len != fields:
                        raise ValueError(
                            f"Error: {my_file.name} has {curr_len}\
                                 fields which is less than the required\
                                number of fields - {fields}\
                                     on line number {line_number}")
                    yield curr_list
                    line_number += 1
            my_file.close()


class University:
    """ This class stores list of students and instructors and has functions\
        to print the pretty table for both
    """

    def __init__(self, directory_path: str) -> None:
        """ This constructor calls all the necessary helper fuctions to\
            parse the data and create two new lists of students and instructors
        """
        self.fr: "FileReader" = FileReader()
        self.directory_path = directory_path
        self.fr.valid_string(self.directory_path)

        if not path.exists(self.directory_path):
            # It raises an exception if the path is not a valid directory
            raise FileNotFoundError(
                "Error: Path given is not a valid directory ")

        self.student_list: dict(str, "Student") = {}
        self.instructor_list: dict(str, "Instructor") = {}
        self.grade_dict: dict('str', float) = {
            'A': 4.0, 'A-': 3.75, 'B+': 3.25, 'B': 3.0, 'B-': 2.75, 'C+': 2.25,
            'C': 2.0, 'C-': 0, 'D+': 0, 'D': 0, 'D-': 0, 'F': 0
        }
        self.majors_list: dict(str, "Majors") = {}
        self.course_list: List[str] = []
        self.get_student_data()
        self.get_instructor_data()
        self.parse_grade_data()
        self.calculate_gpa()
        self.parse_majors_data()
        self.oragnize_student_courses()
        # self.print_pretty_table()

    def get_instructor_data(self) -> None:
        """ Parses the instructors.txt file in the directory """
        for instructor in self.fr.file_reader(
            f'{self.directory_path}/instructors.txt', 3, '\t',
                True):
            new_instructor: "Instructor" = Instructor(
                instructor[0], instructor[1], instructor[2])
            self.instructor_list[instructor[0]] = new_instructor

    def get_student_data(self) -> None:
        """ Parses the students.txt file in the directory """
        for student in self.fr.file_reader(
                f'{self.directory_path}/students.txt', 3, '\t', True):
            new_student: "Student" = Student(
                student[0], student[1], student[2])
            self.student_list[student[0]] = new_student

    def parse_grade_data(self) -> None:
        """ Parses the grade.txt file in the directory """
        for courses in self.fr.file_reader(
                f'{self.directory_path}/grades.txt', 4, '\t', True):
            if courses[0] not in self.student_list:
                raise ValueError(
                    f"Error: Student not found with the given CWID\
                            {courses[0]}")
            course_name: str = courses[1]

            student_obj: "Student" = self.student_list[courses[0]]
            student_obj.course_list.append((course_name, courses[2]))

            if courses[3] not in self.instructor_list:
                raise ValueError(
                    f"Error: Instructor not found with given CWID {courses[3]}"
                )
            instructor_obj: "Instructor" = self.instructor_list[courses[3]]
            instructor_obj.course_dict[courses[1]] += 1

    def parse_majors_data(self) -> None:
        """ This function parses the major.txt file """
        for major in self.fr.file_reader(f'{self.directory_path}/majors.txt',
                                         3, '\t', True):

            if major[0] not in self.majors_list:
                new_major_obj: "Majors" = Majors(major[0])
                self.majors_list[major[0]] = new_major_obj
                if major[1] == 'R':
                    new_major_obj.required_courses.append(major[2])
                else:
                    new_major_obj.electives_courses.append(major[2])
            else:
                major_obj: "Majors" = self.majors_list[major[0]]
                if major[1] == 'R':
                    major_obj.required_courses.append(major[2])
                else:
                    major_obj.electives_courses.append(major[2])

    def calculate_gpa(self) -> None:
        """ This function calculates GPA for all students """
        for student in self.student_list:
            student_obj: "Student" = self.student_list[student]
            sum_grade: float = 0.0
            for course in student_obj.course_list:
                sum_grade += self.grade_dict[course[1]]

            student_obj.gpa = round(sum_grade/len(student_obj.course_list), 2)

    def oragnize_student_courses(self) -> None:
        """ This function calculates the remaingin courses for all students """
        for student in self.student_list:
            student_obj: "Student" = self.student_list[student]
            for course in student_obj.course_list:
                if course[1] in ('A', 'A-', 'B+', 'B', 'B-', 'C+', 'C'):
                    student_obj.completed_courses.append(course[0])
            majors_obj: "Majors" = self.majors_list[student_obj.Major]
            student_obj.remaining_required =\
                list(set(majors_obj.required_courses) -
                     set(student_obj.completed_courses))
            student_obj.remaining_electives =\
                list(set(majors_obj.electives_courses) -
                     set(student_obj.completed_courses))

    def student_grades_table_db(self, db_path: str) -> None:
        """ Prints the pretty table from the student grade summary table """
        fr: "FileReader" = FileReader()
        fr.valid_string(db_path)
        try:
            db: sqlite3.Connection = sqlite3.connect(db_path)
        except Exception as e:
            print(e)
        else:
            query: str = """select s.Name, s.CWID, g.Grade, g.Course, i.Name
                            from students as s join grades as g on\
                                s.CWID = g.StudentCWID join instructors\
                                    i on g.InstructorCWID = i.CWID
                                    order by s.Name """
            pt: "PrettyTable" =\
                PrettyTable(field_names=['Name', 'CWID',
                                         'Course',
                                         'Grade', 'Instructor'])
            try:
                result_list: List[List[Tuple]] = []
                for row in db.execute(query):
                    result_list.append(row)
                    pt.add_row([row[0], row[1], row[2], row[3], row[4]])

                db.close()
                print('Student Grade Summary')
                print(pt)
            except sqlite3.OperationalError as e:
                print(e)

    def print_pretty_table(self) -> None:
        """ Prints the three pretty tables """
        student_pt: PrettyTable = PrettyTable(
            field_names=['CWID', 'Name', 'Major',
                         'Completed Courses', 'Remaining Required',
                         'Remaining Electives', 'GPA'])
        for cwid in self.student_list:
            student_obj: "Student" = self.student_list[cwid]
            student_pt.add_row([student_obj.CWID, student_obj.Name,
                                student_obj.Major,
                                sorted(student_obj.completed_courses),
                                sorted(student_obj.remaining_required),
                                sorted(student_obj.remaining_electives),
                                student_obj.gpa])
        print('Student Summary')
        print(student_pt)

        instructor_pt: PrettyTable = PrettyTable(field_names=['CWID', 'Name',
                                                              'Dep', 'Course',
                                                              'Students'])
        for instructor in self.instructor_list:
            instructor_obj = self.instructor_list[instructor]
            for course in instructor_obj.course_dict:
                instructor_pt.add_row([instructor_obj.CWID,
                                       instructor_obj.Name,
                                       instructor_obj.Department, course,
                                       instructor_obj.course_dict[course]])
        print('Instructor Summary')
        print(instructor_pt)

        majors_pt: PrettyTable = PrettyTable(
            field_names=['Major', 'Required Courses', 'Electives']
        )

        for major in self.majors_list:
            curr_major_obj: "Majors" = self.majors_list[major]
            majors_pt.add_row([curr_major_obj.Name, sorted(
                curr_major_obj.required_courses),
                sorted(curr_major_obj.electives_courses)])
        print('Major Summary')
        print(majors_pt)


class Majors:
    """ This class stores all information related to a Majors courses """

    def __init__(self, Name: str) -> None:
        self.Name: str = Name
        self.required_courses: List[str] = []
        self.electives_courses: List[str] = []


class Student:
    """ This class stores all information related to a student """

    def __init__(self, CWID: str, Name: str, Major: str) -> None:
        """ This is a constructor to store information related to a student """
        self.CWID: str = CWID
        self.Name: str = Name
        self.Major: str = Major
        self.course_list: List[Tuple(str, str)] = []
        self.completed_courses: List[str] = []
        self.remaining_required: List[str] = []
        self.remaining_electives: List[str] = []
        self.gpa: float = 0.0


class Instructor:
    """ This class stores all information related to an instructor """

    def __init__(self, CWID: str, Name: str, Department: str) -> None:
        """ This is a constructor to store information related to an instructor
        """
        self.CWID = CWID
        self.Name = Name
        self.Department = Department
        self.course_dict: DefaultDict[str:int] = defaultdict(int)
