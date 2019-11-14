import mysql.connector

### Open DB Connection
cnx = mysql.connector.connect(user='root', password='sesame80',
                              host='localhost',
                              database='schooldb')

display_prompt = ("Please enter one of the following commands:\n"
					"-r [register] (first_name) (last_name) to register new student\n"
					"-a [add] to add a course\n"
					"-e [enroll] (SID) (course_ID) to enroll a student in a course\n"
					"r [roster] (course_ID) to see a course roster\n"
					"s [schedule] (SID) to see a student's schedule\n"
					"d [day-schedule] (SID) (day) to see a student's day schedule\n"
					"Or type exit to quit.\n")
# Process input
def process_input(input):
	input_elements = input.split()
	# TODO: Sanitize inputs

	# Choose action
	action = input_elements[0]
	if action == "-r" or action == "register":
		register_new_student(input_elements)
	elif action == "-a" or action == 'add':
		add_course()
	elif action == "-e" or action == "enroll":
		enroll_in_course(input_elements)
	elif action == "r" or action == "roster":
		get_course_roster(input_elements)
	elif action == "s" or action == "schedule":
		get_student_schedule(input_elements)
	elif action == "d" or action == "day-schedule":
		get_student_schedule_by_day(input_elements)
	elif action == "h" or action == "help" or action == "-h":
		print(display_prompt)
	elif action == "exit":
		pass
	else:
		print("Unrecognized command: " + input)

# Add a new student to the program
def register_new_student(input_elements):
	if len(input_elements) != 3:
		print("Please enter both a first name and a last name in your command.\ne.g. -r Jane Done")
	else:
		cursor = cnx.cursor()
		add_student = (	"INSERT INTO students "
						"(first_name, last_name)"
						"VALUES (%s, %s)")
		data_student = (input_elements[1], input_elements[2])
		cursor.execute(add_student, data_student)
		cnx.commit()
		cursor.close()
		print 'Added student %s %s' %(input_elements[1], input_elements[2])

# Add a new course to the program
# Then follow prompts.
def add_course():
	course_name = raw_input("Please enter the course name: ") #TODO make course name unique
	course_days = []
	course_hours = [0]

	while len(course_days) != len(course_hours):
		course_days = []
		course_hours = []
		course_times_entered = raw_input("Please enter a comma-separated list of days and times (i.e. Tu 12:00, W 14:00): ") #TODO support multiple days
		course_times = course_times_entered.split(",")
		for course in course_times:
			course_days.append(course.split()[0]) #change to regex match
			course_hours.append(course.split()[1]) #change to regex match
		if len(course_days) != len(course_hours):
			print 'Number of weekdays and times entered do not match'

	add_course = ("INSERT INTO courses VALUES (default, %s)")
	get_course_id = ("SELECT course_id FROM courses WHERE course_name = %s")
	add_times = ("INSERT INTO course_schedule VALUES (%s, %s, %s)")

	cursor = cnx.cursor()
	cursor.execute(add_course, (course_name,))
	cnx.commit()

	# get course_id
	cursor.execute(get_course_id, (course_name,))
	course_id = cursor.fetchone()
	print course_id
	if course_id is None:
		print 'Error adding class. Please check your connection and try again.'
		return

	# add times
	i = 0
	while i < len(course_days):
		cursor.execute(add_times, (course_id[0], course_days[i], course_hours[i]))
		cnx.commit()
		i += 1

	cursor.close()
	print '''Added course "%s"''' %(course_name)

# Enroll a student in a course
def enroll_in_course(input_elements):
	if len(input_elements) != 3:
		print("Please enter the student's SID and the course ID in your command.\ne.g. -e 1 3")

	enroll_student = (	"INSERT INTO course_enrollments "
						"VALUES (%s, %s)")
	enroll_data = (input_elements[1], input_elements[2])

	cursor = cnx.cursor()
	cursor.execute(enroll_student, enroll_data)
	cnx.commit()
	cursor.close()
	print "Added student %s to course %s" %(input_elements[1], input_elements[2])

# See which students are in given course
def get_course_roster(input_elements):
	if len(input_elements) != 2:
		print("Please include a course ID in your command.\ne.g. r 3")
	
	query_roster = (	"SELECT sid, CONCAT(first_name, ' ', last_name) AS student_name "
						"FROM course_enrollments JOIN students USING (sid) "
						"WHERE course_id = %s"
						"ORDER BY last_name, first_name")
	cursor = cnx.cursor()
	cursor.execute(query_roster, (input_elements[1],))

	for (sid, student_name) in cursor:
		print "%s (SID: %s)" %(student_name, sid)

# See which courses the given student is in
def get_student_schedule(input_elements):
	if len(input_elements) != 2:
		print("Please include a SID in your command.\ne.g. s 1")
	query_schedule = (	"SELECT DISTINCT course_id, course_name "
						"FROM course_enrollments JOIN courses USING (course_id) "
						"WHERE sid = %s "
						"ORDER BY course_name")
	cursor = cnx.cursor()
	cursor.execute(query_schedule, (input_elements[1],))

	for (course_id, course_name) in cursor:
		print "%s: %s" %(course_id, course_name)

# See the courses and times of each course for
#	the given student on the given day
def get_student_schedule_by_day(input_elements):
	if len(input_elements) != 3:
		print("Please include a SID and day in your command.\ne.g. d 1 M")

	query_day = (	"SELECT DISTINCT course_id, course_name, time AS course_time "
					"FROM course_enrollments JOIN courses USING (course_id) JOIN course_schedule USING (course_id) "
					"WHERE sid = %s AND day_of_week = %s "
					"ORDER BY course_time")
	cursor = cnx.cursor()
	cursor.execute(query_day, (input_elements[1], input_elements[2]))

	for (course_id, course_name, course_time) in cursor:
		print "%s: (%s) %s" %(course_time, course_id, course_name)

#### Main

response = ""
while response != "exit":
	response = raw_input("Please enter a command: ")
	process_input(response)

cnx.close()