"""
    Author: Mahir Dhall
    Name: Homework9
    Description: This class creates a data repository of courses, students,
    and instructors. The system will be used to help students track their
    required courses, the courses they have successfully completed,
    their grades, GPA, etc. The system will also be used by faculty advisors
    to help students to create study plans.
"""


from collections import defaultdict
from os.path import isfile
from typing import DefaultDict, IO, Iterator, List
from prettytable import PrettyTable
from os import path


class FileReader:
    """ This class contains file reader function to parse data from the input
        files
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
        self.course_list: List[str] = []
        self.get_student_data()
        self.get_instructor_data()
        self.parse_grade_data()
        # self.print_pretty_table()

    def get_instructor_data(self) -> None:
        """ Parses the instructors.txt file in the directory """
        for instructor in self.fr.file_reader(
            f'{self.directory_path}/instructors.txt', 3, '\t',
                False):
            new_instructor: "Instructor" = Instructor(
                instructor[0], instructor[1], instructor[2])
            self.instructor_list[instructor[0]] = new_instructor

    def get_student_data(self) -> None:
        """ Parses the students.txt file in the directory """
        for student in self.fr.file_reader(
                f'{self.directory_path}/students.txt', 3, '\t', False):
            new_student: "Student" = Student(
                student[0], student[1], student[2])
            self.student_list[student[0]] = new_student

    def parse_grade_data(self) -> None:
        """ Parses the grade.txt file in the directory """
        for courses in self.fr.file_reader(
                f'{self.directory_path}/grades.txt', 4, '\t', False):
            if courses[0] not in self.student_list:
                raise ValueError(
                    f"Error: Student not found with the given CWID\
                            {courses[0]}")
            course_name: str = courses[1]

            student_obj: "Student" = self.student_list[courses[0]]
            student_obj.course_list.append(course_name)

            if courses[3] not in self.instructor_list:
                raise ValueError(
                    f"Error: Instructor not found with given CWID {courses[3]}"
                )
            instructor_obj: "Instructor" = self.instructor_list[courses[3]]
            instructor_obj.course_dict[courses[1]] += 1

    def print_pretty_table(self) -> None:
        """ Prints the two pretty tables """
        student_pt: PrettyTable = PrettyTable(
            field_names=['CWID', 'Name',
                         'Major'])
        for cwid in self.student_list:
            student_obj: "Student" = self.student_list[cwid]
            student_pt.add_row([student_obj.CWID, student_obj.Name,
                                sorted(student_obj.course_list)])
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


class Student:
    """ This class stores all information related to a student """

    def __init__(self, CWID: str, Name: str, Major: str) -> None:
        """ This is a constructor to store information related to a student """
        self.CWID: str = CWID
        self.Name: str = Name
        self.Major: str = Major
        self.course_list: List[str] = []


class Instructor:
    """ This class stores all information related to an instructor """

    def __init__(self, CWID: str, Name: str, Department: str) -> None:
        """ This is a constructor to store information related to an instructor
        """
        self.CWID = CWID
        self.Name = Name
        self.Department = Department
        self.course_dict: DefaultDict[str:int] = defaultdict(int)
