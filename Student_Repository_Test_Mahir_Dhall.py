"""
Test File for Student Repository
Author: Mahir Dhall
This file contains all test functions for homework10

Un-comment line 300 to print the three pretty tables
"""
from typing import IO
import unittest
import os as os

from Student_Repository_Mahir_Dhall import Instructor, University, Student


class TestHomework7(unittest.TestCase):
    """ This class contains test cases to test class University of
    """
    @classmethod
    def setUpClass(cls) -> None:
        """ This class is called before running the test case
            valid and invalid directories are being created wth valid and
            invalid inputs respectively
        """

        # Creates a valid directory with valid input files
        try:
            os.mkdir('valid_directory')
        except FileExistsError:
            pass
        grades_file: IO = open(
            f"{os.getcwd()}/valid_directory/grades.txt", "w")
        students_file: IO = open(
            f"{os.getcwd()}/valid_directory/students.txt", "w")
        instructors_file: IO = open(
            f"{os.getcwd()}/valid_directory/instructors.txt", "w")
        majors_file: IO = open(
            f"{os.getcwd()}/valid_directory/majors.txt", "w")

        grades_file.writelines(
            ['StudentCWID|Course|Grade|InstructorCWID\n',
             '10103|SSW 567|A|98765\n', '10103|SSW 564|A-|98764\n',
             '10103|SSW 687|B|98764\n', '10103|CS 501|B|98764\n',
             '10115|SSW 567|A|98765\n', '10115|SSW 564|B+|98764\n',
             '10115|SSW 687|A|98764\n', '10115|CS 545|A|98764\n',
             '10172|SSW 555|A|98763\n', '10172|SSW 567|A-|98765\n',
                '10175|SSW 567|A|98765\n', '10175|SSW 564|A|98764\n',
                '10175|SSW 687|B-|98764\n', '10183|SSW 689|A|98763\n',
                '11399|SSW 540|B|98765\n', '11461|SYS 800|A|98760\n',
                '11461|SYS 750|A-|98760\n', '11461|SYS 611|A|98760\n',
                '11658|SSW 540|F|98765\n', '11714|SYS 611|A|98760\n',
                '11714|SYS 645|C|98760\n', '11788|SSW 540|A|98765\n']
        )
        students_file.writelines(
            ['CWID;Name;Major\n', '10103;Baldwin, C;SFEN\n',
             '10115;Wyatt, X;SFEN\n', '10172;Forbes, I;SFEN\n',
             '10175;Erickson, D;SFEN\n', '10183;Chapman, O;SFEN\n',
             '11399;Cordova, I;SYEN\n', '11461;Wright, U;SYEN\n',
             '11658;Kelly, P;SYEN\n', '11714;Morton, A;SYEN\n',
             '11788;Fuller, E;SYEN\n'])
        instructors_file.writelines(
            ['CWID|Instructor|Dept\n', '98765|Einstein, A|SFEN\n',
             '98764|Feynman, R|SFEN\n', '98763|Newton, I|SFEN\n',
             '98762|Hawking, S|SYEN\n', '98761|Edison, A|SYEN\n',
             '98760|Darwin, C|SYEN\n'])
        majors_file.writelines(
            ['Major\tRequired/Elective\tCourse\n', 'SFEN\tR\tSSW 540\n',
             'SFEN\tR\tSSW 564\n', 'SFEN\tR\tSSW 555\n', 'SFEN\tR\tSSW 567\n',
             'SFEN\tE\tCS 501\n', 'SFEN\tE\tCS 513\n',
                'SFEN\tE\tCS 545\n', 'SYEN\tR\tSYS 671\n',
                'SYEN\tR\tSYS 612\n', 'SYEN\tR\tSYS 800\n',
                'SYEN\tE\tSSW 810\n', 'SYEN\tE\tSSW 565\n',
                'SYEN\tE\tSSW 540\n']
        )
        grades_file.close()
        students_file.close()
        instructors_file.close()
        majors_file.close()
        # Creates an invalid directory with invalid numbers of fields in input
        try:
            os.mkdir('invalid_directory')
        except FileExistsError:
            pass

        grades_file: IO = open(
            f"{os.getcwd()}/invalid_directory/grades.txt", "w")
        students_file: IO = open(
            f"{os.getcwd()}/invalid_directory/students.txt", "w")
        instructors_file: IO = open(
            f"{os.getcwd()}/invalid_directory/instructors.txt", "w")
        majors_file: IO = open(
            f"{os.getcwd()}/invalid_directory/majors.txt", "w")

        grades_file.writelines(
            ['StudentCWID|Course|Grade|InstructorCWID\n',
             '10103|SSW 567|A|98765\n', '10103|SSW 564|A-|98764\n',
             '10103|SSW 687|B|98764\n', '10103|CS 501|B|98764\n',
             '10115|SSW 567|A|98765\n', '10115|SSW 564|B+|98764\n',
             '10115|SSW 687|98764\n', '10115|CS 545|A|98764\n',
             '10172|SSW 555|A|98763\n', '10172|SSW 567|A-|98765\n',
             '10175|SSW 567|A|98765\n', '10175|SSW 564|A|98764\n',
                '10175|SSW 687|B-|98764\n', '10183|SSW 689|A|98763\n',
                '11399|SSW 540|B|98765\n', '11461|SYS 800|A|98760\n',
                '11461|SYS 750|A-|98760\n', '11461|SYS 611|A|98760\n',
                '11658|SSW 540|F|98765\n', '11714|SYS 611|A|98760\n',
                '11714|SYS 645|C|98760\n', '11788|SSW 540|A|98765\n']
        )
        students_file.writelines(
            ['CWID;Name;Major\n', '10103;Baldwin, C;SFEN\n',
             '10115;SFEN\n', '10172;Forbes, I;SFEN\n',
             '10175;Erickson, D;SFEN\n', '10183;Chapman, O;SFEN\n',
             '11399;Cordova, I;SYEN\n', '11461;Wright, U;SYEN\n',
             '11658;Kelly, P;SYEN\n', '11714;Morton, A;SYEN\n',
             '11788;Fuller, E;SYEN\n']
        )
        instructors_file.writelines(
            ['CWID|Instructor|Dept\n', '98765|Einstein, A|SFEN\n',
             '98764|Feynman, R|SFEN\n', '98763|Newton, I|SFEN\n',
             '98762|Hawking, S|SYEN\n', '98761|Edison, A|SYEN\n',
             '98760|Darwin, C|SYEN\n'])
        majors_file.writelines(
            ['Major\tRequired/Elective\tCourse\n', 'SFEN\tR\tSSW 540\n',
             'SFEN\tR\tSSW 564\n', 'SFEN\tR\tSSW 555\n', 'SFEN\tR\tSSW 567\n',
             'SFEN\tE\tCS 501\n', 'SFEN\tE\tCS 513\n',
             'SFEN\tE\tCS 545\n', 'SYEN\tR\tSYS 671\n',
                'SYEN\tR\tSYS 612\n', 'SYEN\tR\tSYS 800\n',
                'SYEN\tE\tSSW 810\n', 'SYEN\tE\tSSW 565\n',
                'SYEN\tE\tSSW 540\n']
        )
        grades_file.close()
        students_file.close()
        instructors_file.close()
        majors_file.close()

        # invalid directory with one missing input file instructors.txt
        try:
            os.mkdir('missing_files_directory')
        except FileExistsError:
            pass

        grades_file: IO = open(
            f"{os.getcwd()}/missing_files_directory/grades.txt", "w")
        students_file: IO = open(
            f"{os.getcwd()}/missing_files_directory/students.txt", "w")

        grades_file.writelines(
            ['StudentCWID|Course|Grade|InstructorCWID\n',
             '10103|SSW 567|A|98765\n', '10103|SSW 564|A-|98764\n',
             '10103|SSW 687|B|98764\n', '10103|CS 501|B|98764\n',
             '10115|SSW 567|A|98765\n', '10115|SSW 564|B+|98764\n',
             '10115|SSW 687|A|98764\n', '10115|CS 545|A|98764\n',
             '10172|SSW 555|A|98763\n', '10172|SSW 567|A-|98765\n',
             '10175|SSW 567|A|98765\n', '10175|SSW 564|A|98764\n',
                '10175|SSW 687|B-|98764\n', '10183|SSW 689|A|98763\n',
                '11399|SSW 540|B|98765\n', '11461|SYS 800|A|98760\n',
                '11461|SYS 750|A-|98760\n', '11461|SYS 611|A|98760\n',
                '11658|SSW 540|F|98765\n', '11714|SYS 611|A|98760\n',
                '11714|SYS 645|C|98760\n', '11788|SSW 540|A|98765\n']
        )
        students_file.writelines(
            ['CWID;Name;Major\n', '10103;Baldwin, C;SFEN\n',
             '10115;Wyatt, X;SFEN\n', '10172;Forbes, I;SFEN\n',
             '10175;Erickson, D;SFEN\n', '10183;Chapman, O;SFEN\n',
             '11399;Cordova, I;SYEN\n', '11461;Wright, U;SYEN\n',
             '11658;Kelly, P;SYEN\n', '11714;Morton, A;SYEN\n',
             '11788;Fuller, E;SYEN\n']
        )
        grades_file.close()
        students_file.close()

        # Creates an invalid directory with a missing instructor
        try:
            os.mkdir('missing_instructor')
        except FileExistsError:
            pass
        grades_file: IO = open(
            f"{os.getcwd()}/missing_instructor/grades.txt", "w")
        students_file: IO = open(
            f"{os.getcwd()}/missing_instructor/students.txt", "w")
        instructors_file: IO = open(
            f"{os.getcwd()}/missing_instructor/instructors.txt", "w")
        majors_file: IO = open(
            f"{os.getcwd()}/missing_instructor/majors.txt", "w")

        grades_file.writelines(
            ['StudentCWID|Course|Grade|InstructorCWID\n',
             '10103|SSW 567|A|98765\n', '10103|SSW 564|A-|98764\n',
             '10103|SSW 687|B|98764\n', '10103|CS 501|B|98764\n',
             '10115|SSW 567|A|98765\n', '10115|SSW 564|B+|98764\n',
             '10115|SSW 687|A|98764\n', '10115|CS 545|A|98764\n',
             '10172|SSW 555|A|98763\n', '10172|SSW 567|A-|98765\n',
             '10175|SSW 567|A|98765\n', '10175|SSW 564|A|98764\n',
                '10175|SSW 687|B-|98764\n', '10183|SSW 689|A|98763\n',
                '11399|SSW 540|B|98765\n', '11461|SYS 800|A|98760\n',
                '11461|SYS 750|A-|98760\n', '11461|SYS 611|A|98760\n',
                '11658|SSW 540|F|98765\n', '11714|SYS 611|A|98760\n',
                '11714|SYS 645|C|98760\n', '11788|SSW 540|A|98765\n']
        )
        students_file.writelines(
            ['CWID;Name;Major\n', '10103;Baldwin, C;SFEN\n',
             '10115;Wyatt, X;SFEN\n', '10172;Forbes, I;SFEN\n',
             '10175;Erickson, D;SFEN\n', '10183;Chapman, O;SFEN\n',
             '11399;Cordova, I;SYEN\n', '11461;Wright, U;SYEN\n',
             '11658;Kelly, P;SYEN\n', '11714;Morton, A;SYEN\n',
             '11788;Fuller, E;SYEN\n']
        )
        instructors_file.writelines(
            ['CWID|Instructor|Dept\n', '98765|Einstein, A|SFEN\n',
             '98763|Newton, I|SFEN\n',
             '98762|Hawking, S|SYEN\n', '98761|Edison, A|SYEN\n',
             '98760|Darwin, C|SYEN\n'])
        majors_file.writelines(
            ['Major\tRequired/Elective\tCourse\n', 'SFEN\tR\tSSW 540\n',
             'SFEN\tR\tSSW 564\n', 'SFEN\tR\tSSW 555\n', 'SFEN\tR\tSSW 567\n',
             'SFEN\tE\tCS 501\n', 'SFEN\tE\tCS 513\n',
             'SFEN\tE\tCS 545\n', 'SYEN\tR\tSYS 671\n',
                'SYEN\tR\tSYS 612\n', 'SYEN\tR\tSYS 800\n',
                'SYEN\tE\tSSW 810\n', 'SYEN\tE\tSSW 565\n',
                'SYEN\tE\tSSW 540\n']
        )
        grades_file.close()
        students_file.close()
        instructors_file.close()
        majors_file.close()

        # Creates an invalid directory with missing student
        try:
            os.mkdir('missing_student')
        except FileExistsError:
            pass
        grades_file: IO = open(
            f"{os.getcwd()}/missing_student/grades.txt", "w")
        students_file: IO = open(
            f"{os.getcwd()}/missing_student/students.txt", "w")
        instructors_file: IO = open(
            f"{os.getcwd()}/missing_student/instructors.txt", "w")
        majors_file: IO = open(
            f"{os.getcwd()}/missing_student/majors.txt", "w")

        grades_file.writelines(
            ['StudentCWID|Course|Grade|InstructorCWID\n',
             '10103|SSW 567|A|98765\n', '10103|SSW 564|A-|98764\n',
             '10103|SSW 687|B|98764\n', '10103|CS 501|B|98764\n',
             '10115|SSW 567|A|98765\n', '10115|SSW 564|B+|98764\n',
             '10115|SSW 687|A|98764\n', '10115|CS 545|A|98764\n',
             '10172|SSW 555|A|98763\n', '10172|SSW 567|A-|98765\n',
             '10175|SSW 567|A|98765\n', '10175|SSW 564|A|98764\n',
                '10175|SSW 687|B-|98764\n', '10183|SSW 689|A|98763\n',
                '11399|SSW 540|B|98765\n', '11461|SYS 800|A|98760\n',
                '11461|SYS 750|A-|98760\n', '11461|SYS 611|A|98760\n',
                '11658|SSW 540|F|98765\n', '11714|SYS 611|A|98760\n',
                '11714|SYS 645|C|98760\n', '11788|SSW 540|A|98765\n']
        )
        students_file.writelines(
            ['CWID;Name;Major\n', '10103;Baldwin, C;SFEN\n',
             '10172;Forbes, I;SFEN\n',
             '10175;Erickson, D;SFEN\n', '10183;Chapman, O;SFEN\n',
             '11399;Cordova, I;SYEN\n', '11461;Wright, U;SYEN\n',
             '11658;Kelly, P;SYEN\n', '11714;Morton, A;SYEN\n',
             '11788;Fuller, E;SYEN\n']
        )
        instructors_file.writelines(
            ['98765\tEinstein, A\tSFEN\n', '98764\tFeynman, R\tSFEN\n',
                '98763\tNewton, I\tSFEN\n',
             '98762\tHawking, S\tSYEN\n', '98761\tEdison, A\tSYEN\n',
             '98760\tDarwin, C\tSYEN\n'])
        majors_file.writelines(
            ['Major\tRequired/Elective\tCourse\n', 'SFEN\tR\tSSW 540\n',
             'SFEN\tR\tSSW 564\n', 'SFEN\tR\tSSW 555\n', 'SFEN\tR\tSSW 567\n',
             'SFEN\tE\tCS 501\n', 'SFEN\tE\tCS 513\n',
             'SFEN\tE\tCS 545\n', 'SYEN\tR\tSYS 671\n',
                'SYEN\tR\tSYS 612\n', 'SYEN\tR\tSYS 800\n',
                'SYEN\tE\tSSW 810\n', 'SYEN\tE\tSSW 565\n',
                'SYEN\tE\tSSW 540\n']
        )
        grades_file.close()
        students_file.close()
        instructors_file.close()
        majors_file.close()

    def test_valid_directory(self) -> None:
        """ Tests valid directory and its information
            Verifies information of random student and instructor objects
        """
        valid_university: "University" = University('valid_directory')

        self.assertEqual(len(valid_university.student_list), 10)
        self.assertEqual(len(valid_university.instructor_list), 6)
        student_obj: "Student" = valid_university.student_list['10103']
        self.assertEqual(
            sorted(student_obj.completed_courses), [
                'CS 501', 'SSW 564', 'SSW 567', 'SSW 687']
        )
        self.assertEqual(
            sorted(student_obj.remaining_required), [
                'SSW 540', 'SSW 555']
        )
        instrucor_obj: "Instructor" = valid_university.instructor_list['98764']
        self.assertEqual(instrucor_obj.course_dict['SSW 687'], 3)

        # valid_university.print_pretty_table()

    def test_invalid_directory(self) -> None:
        """ This tests all invalid directories with erroneous inputs to check
            for correct exception handling
        """
        with self.assertRaises(FileNotFoundError):
            University(
                'missing_files_directory')
        with self.assertRaises(ValueError):
            University('invalid_directory')
        with self.assertRaises(ValueError):
            University('missing_instructor')
        with self.assertRaises(TypeError):
            University(123)
        with self.assertRaises(ValueError):
            University('missing_student')


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
