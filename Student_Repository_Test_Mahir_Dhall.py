"""
Test File for Student Repository
Author: Mahir Dhall
This file contains all test functions for homework10

Un-comment line 302 to print the three pretty tables
"""
from typing import IO, List, Tuple
import unittest
import sqlite3

from Student_Repository_Mahir_Dhall import Instructor, University, Student


class TestHomework7(unittest.TestCase):

    def test_valid_directory(self) -> None:
        """ Tests valid directory and its information
            Verifies information of random student and instructor objects
        """
        valid_university: "University" = University(
            'hw11Direc/valid_directory')

        self.assertEqual(len(valid_university.student_list), 4)
        self.assertEqual(len(valid_university.instructor_list), 3)
        student_obj: "Student" = valid_university.student_list['10103']
        self.assertEqual(
            sorted(student_obj.completed_courses), ['CS 501', 'SSW 810']
        )
        self.assertEqual(
            sorted(student_obj.remaining_required), [
                'SSW 540', 'SSW 555']
        )
        instrucor_obj: "Instructor" = valid_university.instructor_list['98764']
        self.assertEqual(instrucor_obj.course_dict['CS 546'], 1)

        # valid_university.print_pretty_table()

    def test_invalid_directory(self) -> None:
        """ This tests all invalid directories with erroneous inputs to check
            for correct exception handling
        """
        with self.assertRaises(FileNotFoundError):
            University(
                'hw11Direc/missing_files_directory')
        with self.assertRaises(ValueError):
            University('hw11Direc/invalid_directory')
        with self.assertRaises(ValueError):
            University('hw11Direc/missing_instructor')
        with self.assertRaises(TypeError):
            University(123)
        with self.assertRaises(ValueError):
            University('hw11Direc/missing_student')

    def test_student_grades_table_db(self) -> None:
        """ This tests the student_grades_table_db function for it correct
            implementation
        """
        try:
            path: str = f"hw11Direc/810_startup.db"
            db: sqlite3.Connection = sqlite3.connect(path)
        except (FileNotFoundError, ValueError) as e:
            print(e)
        else:
            query: str = """select s.Name, s.CWID, g.Grade, g.Course, i.Name
                            from students as s join grades as g on\
                                s.CWID = g.StudentCWID join instructors\
                                    i on g.InstructorCWID = i.CWID
                                    order by s.Name """
            try:
                result_list: List[List[Tuple]] = []
                for row in db.execute(query):
                    result_list.append(row)
            except sqlite3.OperationalError as e:
                print(e)
            else:
                db.close()
                self.assertEqual(result_list,
                                 [('Bezos, J', '10115', 'A', 'SSW 810',
                                   'Rowland, J'),
                                  ('Bezos, J', '10115', 'F', 'CS 546',
                                   'Hawking, S'), ('Gates, B', '11714', 'A',
                                                   'CS 546', 'Cohen, R'),
                                  ('Gates, B', '11714', 'B-', 'SSW 810',
                                   'Rowland, J'), ('Gates, B', '11714', 'A-',
                                                   'CS 570', 'Hawking, S'),
                                  ('Jobs, S', '10103', 'A-', 'SSW 810',
                                   'Rowland, J'), ('Jobs, S', '10103', 'B',
                                                   'CS 501', 'Hawking, S'),
                                  ('Musk, E', '10183', 'A', 'SSW 555',
                                   'Rowland, J'), ('Musk, E', '10183', 'A',
                                                   'SSW 810', 'Rowland, J')])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
