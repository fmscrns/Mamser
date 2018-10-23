from mamser import db

class College(db.Model):
    college_db_id = db.Column(db.Integer, primary_key=True)
    college_name = db.Column(db.String(100), nullable=False)
    comprised_by = db.relationship("Course", backref="college", lazy=True)

def __repr__(self):
    return "College({})".format(self.college_name)

class Course(db.Model):
    course_db_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    college_id = db.Column(db.Integer, db.ForeignKey("college.college_db_id"), nullable=False)
    attended_by = db.relationship("Student", backref="course", lazy=True)

def __repr__(self):
    return "Course({}, {})".format(self.course_name, self.college_id)

class Student(db.Model):
    student_db_id = db.Column(db.Integer, primary_key=True)
    student_idNo = db.Column(db.String(9), nullable=False)
    student_name = db.Column(db.String(100), nullable=False)
    student_gender = db.Column(db.String(6), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("course.course_db_id"), nullable=False)

def __repr__(self):
    return "Student({}, {}, {})".format(self.student_idNo, self.student_name, self.student_gender, self.course_id)