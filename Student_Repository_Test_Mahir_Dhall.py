"""
Test File for Student Repository
Author: Mahir Dhall
This file contains all test functions for homework09
"""
from os import chdir
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

        grades_file.writelines(
            ['10103\tSSW 567\tA\t98765\n', '10103\tSSW 564\tA-\t98764\n',
                '10103\tSSW 687\tB\t98764\n', '10103\tCS 501\tB\t98764\n',
             '10115\tSSW 567\tA\t98765\n',
             '10115\tSSW 564\tB+\t98764\n', '10115\tSSW 687\tA\t98764\n',
             '10115\tCS 545\tA\t98764\n', '10172\tSSW 555\tA\t98763\n',
             '10172\tSSW 567\tA-\t98765\n', '10175\tSSW 567\tA\t98765\n',
             '10175\tSSW 564\tA\t98764\n', '10175\tSSW 687\tB-\t98764\n',
             '10183\tSSW 689\tA\t98763\n', '11399\tSSW 540\tB\t98765\n',
             '11461\tSYS 800\tA\t98760\n', '11461\tSYS 750\tA-\t98760\n',
             '11461\tSYS 611\tA\t98760\n', '11658\tSSW 540\tF\t98765\n',
             '11714\tSYS 611\tA\t98760\n', '11714\tSYS 645\tC\t98760\n',
             '11788\tSSW 540\tA\t98765\n'])
        students_file.writelines(
            ['10103\tBaldwin, C\tSFEN\n', '10115\tWyatt, X\tSFEN\n',
                '10172\tForbes, I\tSFEN\n', '10175\tErickson, D\tSFEN\n',
             '10183\tChapman, O\tSFEN\n', '11399\tCordova, I\tSYEN\n',
             '11461\tWright, U\tSYEN\n', '11658\tKelly, P\tSYEN\n',
             '11714\tMorton, A\tSYEN\n', '11788\tFuller, E\tSYEN\n'])
        instructors_file.writelines(
            ['98765\tEinstein, A\tSFEN\n', '98764\tFeynman, R\tSFEN\n',
                '98763\tNewton, I\tSFEN\n',
             '98762\tHawking, S\tSYEN\n', '98761\tEdison, A\tSYEN\n',
             '98760\tDarwin, C\tSYEN\n'])
        grades_file.close()
        students_file.close()
        instructors_file.close()

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

        grades_file.writelines(
            ['10103\tSSW 567\tA\t98765\n', '10103\tSSW 564\tA-\t98764\n',
                '10103\tSSW 687\tB\t98764\n', '10103\tCS 501\tB\t98764\n',
             '10115\tSSW 567\tA\t98765\n',
             '10115\tSSW 564\t98764\n', '10115\tSSW 687\tA\t98764\n',
             '10115\tCS 545\tA\t98764\n', '10172\tSSW 555\tA\t98763\n',
             '10172\tA-\t98765\n', '10175\tSSW 567\tA\t98765\n',
             '10175\tSSW 564\tA\t98764\n', '10175\tSSW 687\tB-\t98764\n',
             '10183\tSSW 689\tA\t98763\n', '11399\tSSW 540\tB\t98765\n',
             '11461\tSYS 800\tA\t98760\n', '11461\tSYS 750\tA-\t98760\n',
             '11461\tSYS 611\tA\t98760\n', '11658\tSSW 540\tF\t98765\n',
             '11714\tSYS 611\tA\t98760\n', '11714\tSYS 645\tC\t98760\n',
             '11788\tSSW 540\tA\t98765\n']
        )
        students_file.writelines(
            ['10103\tBaldwin, C\tSFEN\n', '10115\tWyatt, X\tSFEN\n',
                '10172\tSFEN\n', '10175\tErickson, D\tSFEN\n',
             '10183\tChapman, O\tSFEN\n', '11399\tCordova, I\tSYEN\n',
             '11461\tWright, U\tSYEN\n', '11658\tKelly, P\tSYEN\n',
             '11714\tMorton, A\tSYEN\n', '11788\tFuller, E\tSYEN\n']
        )
        instructors_file.writelines(
            ['98765\tEinstein, A\tSFEN\n', '98764\tFeynman, R\tSFEN\n',
                '98763\tNewton, I\tSFEN\n',
             '98762\tHawking, S\tSYEN\n', '98761\tEdison, A\tSYEN\n',
             '98760\tDarwin, C\tSYEN\n'])
        grades_file.close()
        students_file.close()
        instructors_file.close()

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
            ['10103\tSSW 567\tA\t98765\n', '10103\tSSW 564\tA-\t98764\n',
                '10103\tSSW 687\tB\t98764\n', '10103\tCS 501\tB\t98764\n',
             '10115\tSSW 567\tA\t98765\n',
             '10115\tSSW 564\tB+\t98764\n', '10115\tSSW 687\tA\t98764\n',
             '10115\tCS 545\tA\t98764\n', '10172\tSSW 555\tA\t98763\n',
             '10172\tSSW 567\tA-\t98765\n', '10175\tSSW 567\tA\t98765\n',
             '10175\tSSW 564\tA\t98764\n', '10175\tSSW 687\tB-\t98764\n',
             '10183\tSSW 689\tA\t98763\n', '11399\tSSW 540\tB\t98765\n',
             '11461\tSYS 800\tA\t98760\n', '11461\tSYS 750\tA-\t98760\n',
             '11461\tSYS 611\tA\t98760\n', '11658\tSSW 540\tF\t98765\n',
             '11714\tSYS 611\tA\t98760\n', '11714\tSYS 645\tC\t98760\n',
             '11788\tSSW 540\tA\t98765\n']
        )
        students_file.writelines(
            ['10103\tBaldwin, C\tSFEN\n', '10115\tWyatt, X\tSFEN\n',
                '10172\tForbes, I\tSFEN\n', '10175\tErickson, D\tSFEN\n',
             '10183\tChapman, O\tSFEN\n', '11399\tCordova, I\tSYEN\n',
             '11461\tWright, U\tSYEN\n', '11658\tKelly, P\tSYEN\n',
             '11714\tMorton, A\tSYEN\n', '11788\tFuller, E\tSYEN\n']
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

        grades_file.writelines(
            ['10103\tSSW 567\tA\t98765\n', '10103\tSSW 564\tA-\t98764\n',
                '10103\tSSW 687\tB\t98764\n', '10103\tCS 501\tB\t98764\n',
             '10115\tSSW 567\tA\t98765\n',
             '10115\tSSW 564\tB+\t98764\n', '10115\tSSW 687\tA\t98764\n',
             '10115\tCS 545\tA\t98764\n', '10172\tSSW 555\tA\t98763\n',
             '10172\tSSW 567\tA-\t98765\n', '10175\tSSW 567\tA\t98765\n',
             '10175\tSSW 564\tA\t98764\n', '10175\tSSW 687\tB-\t98764\n',
             '10183\tSSW 689\tA\t98763\n', '11399\tSSW 540\tB\t98765\n',
             '11461\tSYS 800\tA\t98760\n', '11461\tSYS 750\tA-\t98760\n',
             '11461\tSYS 611\tA\t98760\n', '11658\tSSW 540\tF\t98765\n',
             '11714\tSYS 611\tA\t98760\n', '11714\tSYS 645\tC\t98760\n',
             '11788\tSSW 540\tA\t98765\n']
        )
        students_file.writelines(
            ['10103\tBaldwin, C\tSFEN\n', '10115\tWyatt, X\tSFEN\n',
                '10172\tForbes, I\tSFEN\n', '10175\tErickson, D\tSFEN\n',
             '10183\tChapman, O\tSFEN\n', '11399\tCordova, I\tSYEN\n',
             '11461\tWright, U\tSYEN\n', '11658\tKelly, P\tSYEN\n',
             '11714\tMorton, A\tSYEN\n', '11788\tFuller, E\tSYEN\n']
        )
        instructors_file.writelines(
            ['98765\tEinstein, A\tSFEN\n', '98764\tFeynman, R\tSFEN\n',
                '98763\tNewton, I\tSFEN\n',
             '98762\tHawking, S\tSYEN\n'])
        grades_file.close()
        students_file.close()
        instructors_file.close()

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

        grades_file.writelines(
            ['10103\tSSW 567\tA\t98765\n', '10103\tSSW 564\tA-\t98764\n',
                '10103\tSSW 687\tB\t98764\n', '10103\tCS 501\tB\t98764\n',
             '10115\tSSW 567\tA\t98765\n',
             '10115\tSSW 564\tB+\t98764\n', '10115\tSSW 687\tA\t98764\n',
             '10115\tCS 545\tA\t98764\n', '10172\tSSW 555\tA\t98763\n',
             '10172\tSSW 567\tA-\t98765\n', '10175\tSSW 567\tA\t98765\n',
             '10175\tSSW 564\tA\t98764\n', '10175\tSSW 687\tB-\t98764\n',
             '10183\tSSW 689\tA\t98763\n', '11399\tSSW 540\tB\t98765\n',
             '11461\tSYS 800\tA\t98760\n', '11461\tSYS 750\tA-\t98760\n',
             '11461\tSYS 611\tA\t98760\n', '11658\tSSW 540\tF\t98765\n',
             '11714\tSYS 611\tA\t98760\n', '11714\tSYS 645\tC\t98760\n',
             '11788\tSSW 540\tA\t98765\n']
        )
        students_file.writelines(
            ['10103\tBaldwin, C\tSFEN\n',
                '10172\tForbes, I\tSFEN\n', '10175\tErickson, D\tSFEN\n',
             '10183\tChapman, O\tSFEN\n', '11399\tCordova, I\tSYEN\n',
             '11461\tWright, U\tSYEN\n', '11658\tKelly, P\tSYEN\n',
             '11714\tMorton, A\tSYEN\n', '11788\tFuller, E\tSYEN\n']
        )
        instructors_file.writelines(
            ['98765\tEinstein, A\tSFEN\n', '98764\tFeynman, R\tSFEN\n',
                '98763\tNewton, I\tSFEN\n',
             '98762\tHawking, S\tSYEN\n', '98761\tEdison, A\tSYEN\n',
             '98760\tDarwin, C\tSYEN\n'])
        grades_file.close()
        students_file.close()
        instructors_file.close()

    def test_valid_directory(self) -> None:
        """ Tests valid directory and its information
            Verifies information of random student and instructor objects
        """
        valid_university: "University" = University('valid_directory')

        self.assertEqual(len(valid_university.student_list), 10)
        self.assertEqual(len(valid_university.instructor_list), 6)
        student_obj: "Student" = valid_university.student_list['10103']
        self.assertEqual(
            sorted(student_obj.course_list), [
                'CS 501', 'SSW 564', 'SSW 567', 'SSW 687']
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
