select s.Name, s.CWID, count(g.Course) as total_courses
from students as s join grades as g on s.CWID = g.StudentCWID
group by s.Name, s.CWID
order by s.Name