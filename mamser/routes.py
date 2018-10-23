from flask import render_template, url_for, flash, redirect, jsonify
from mamser import app
from mamser.forms import AddRegistryForm, SearchRegistryForm
from mamser import models
from mamser.models import *

@app.route("/")
@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/mamser", methods=["get", "post"])
def mamser():
    addRegistryForm = AddRegistryForm()
    searchRegistryForm = SearchRegistryForm()
    
    addRegistryForm.add_course.choices = [(course.course_db_id, course.course_name) for course in Course.query.filter_by(college_id=addRegistryForm.add_college.data).all()]
    searchRegistryForm.search_course.choices = [(course.course_db_id, course.course_name) for course in Course.query.filter_by(college_id=searchRegistryForm.search_college.data).all()]

    if addRegistryForm.validate_on_submit():
        course = Course.query.filter_by(course_db_id=addRegistryForm.add_course.data).first()
        student = Student(student_idNo=addRegistryForm.add_idNo.data, student_name=addRegistryForm.add_name.data, student_gender=addRegistryForm.add_gender.data, course_id=course.course_db_id)

        db.session.add(student)
        db.session.commit()

        addRegistryForm.add_idNo.data = ""
        addRegistryForm.add_name.data = ""
        addRegistryForm.add_gender.data = ""
        addRegistryForm.add_college.data = 0
        addRegistryForm.add_course.choices = []
        return redirect(url_for("mamser"))

    if searchRegistryForm.validate_on_submit():
        return redirect(url_for("mamser")) 

    content = "student_list"
    return render_template("mamser.html", addRegistryForm=addRegistryForm, searchRegistryForm=searchRegistryForm, content=content)

@app.route("/coursesoptionlib/<college_id>")
def course(college_id):
    courseList = []

    courses = Course.query.filter_by(college_id=college_id).all()

    for course in courses:
        courseObj = {}

        courseObj["db_id"] = course.course_db_id
        courseObj["name"] = course.course_name
        
        courseList.append(courseObj)
    
    return jsonify({"courses" : courseList})

@app.route("/studentsearchidnolib/<student_idNo>")
def searchStudentIdNo(student_idNo):
    studentObj = {}

    student = Student.query.filter_by(student_idNo=student_idNo).first()

    if student:
        course = Course.query.filter_by(course_db_id=student.course_id).first()
        college = College.query.filter_by(college_db_id=course.college_id).first()

        studentObj["idNo"] = student.student_idNo
        studentObj["name"] = student.student_name
        studentObj["gender"] = student.student_gender
        studentObj["course"] = course.course_name
        studentObj["college"] = college.college_name

    return jsonify({"student" : studentObj})

@app.route("/studentsearchnamelib/<student_name>")
def searchStudentName(student_name):
    studentObj = {}

    student = Student.query.filter_by(student_name=student_name).first()

    if student:
        course = Course.query.filter_by(course_db_id=student.course_id).first()

        studentObj["idNo"] = student.student_idNo
        studentObj["name"] = student.student_name
        studentObj["gender"] = student.student_gender
        studentObj["course"] = course.course_name

    return jsonify({"students" : studentObj})

@app.route("/studentsearchgenderlib/<student_gender>")
def searchStudentGender(student_gender):
    studentList = []

    students = Student.query.filter_by(student_gender=student_gender).all()

    for student in students:
        studentObj = {}

        course = Course.query.filter_by(course_db_id=student.course_id).first()

        studentObj["idNo"] = student.student_idNo
        studentObj["name"] = student.student_name
        studentObj["gender"] = student.student_gender
        studentObj["course_id"] = course.course_name
        
        studentList.append(studentObj)

    return jsonify({"students" : studentList})

@app.route("/studentsearchcourselib/<course_id>")
def searchStudentCourse(course_id):
    studentList = []

    students = Student.query.filter_by(course_id=course_id).all()

    for student in students:
        studentObj = {}

        course = Course.query.filter_by(course_db_id=student.course_id).first()

        studentObj["idNo"] = student.student_idNo
        studentObj["name"] = student.student_name
        studentObj["gender"] = student.student_gender
        studentObj["course_id"] = course.course_name
        
        studentList.append(studentObj)

    return jsonify({"students" : studentList})
