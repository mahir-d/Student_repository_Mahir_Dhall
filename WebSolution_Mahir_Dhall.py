"""
    Author: Mahir Dhall
    Name: Homework12
    Description: This class creates a web server using Flask to display
                 the student summary table using data from sqlite3 database.                
"""
from typing import List, Tuple
import sqlite3
from flask import Flask, render_template
app: Flask = Flask(__name__, template_folder='templates')


def run_query() -> List[List[Tuple]]:
    """ This funcitons runs the query to fetch data from the database file
        to display the student summary table.
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
            return result_list


@app.route('/student_summary')
def template_demo() -> str:
    """ This function creates an html template to display student summary
        table at route /student_summary
    """
    return render_template('student_table.html',
                           my_header="Student Summary",
                           students=run_query())


app.run(debug=True)
