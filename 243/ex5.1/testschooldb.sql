use schooldb;

select * from students;
select * from courses;
select * from course_enrollments;
select * from course_schedule;

SELECT sid, CONCAT(first_name, ' ', last_name) AS student_name
	FROM course_enrollments JOIN students USING (sid)
	WHERE course_id = 1;

SELECT DISTINCT course_id, course_name, course_time
	FROM course_enrollments JOIN courses USING (course_id)
	WHERE sid = 1
	ORDER BY course_time;