select Grade, count(*) as grade_count
from grades
where Course = 'SSW 810'
group by Grade
order by grade_count DESC limit '1'