select s.Name, s.CWID, g.Grade, g.Course, i.Name
from students as s join grades as g on s.CWID = g.StudentCWID join instructors i on g.InstructorCWID = i.CWID
order by s.Name
