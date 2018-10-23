from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, SelectField
from wtforms.validators import ValidationError, DataRequired, InputRequired 
from mamser.models import Student

def nameFieldCheck(form, field):
    count = 0
    for x in field.data:
        try:
            int(x)
        except ValueError:
            count +=1
    if count<len(field.data):
        raise ValidationError("Field does not accept numbers.")
    if len(field.data) < 3:
        raise ValidationError("Field is too small.")
    elif len(field.data) > 60:
        raise ValidationError("Field is too long.")

def idNoFieldCheck(form, field):
    if len(field.data) != 9:
        raise ValidationError("Field requires you to follow the ID number format.")
    try:
        if field.data[4] != "-":
            raise ValidationError("Field requires you to follow the ID number format.")
    except IndexError:    
        raise ValidationError("Field requires you to follow the ID number format.")
    for x in field.data[0:4]:
        try:
            int(x)
        except ValueError:
            raise ValidationError("Field requires you to follow the ID number format.")
    for x in field.data[5:9]:
        try:
            int(x)
        except ValueError:
            raise ValidationError("Field requires you to follow the ID number format.")

def idNoExistenceCheck(form, field): 
    student = Student.query.filter_by(student_idNo=field.data).first()
    if student:
        raise ValidationError("Student already exists.")
     
class AddRegistryForm(FlaskForm):
    add_name = StringField("add_name", validators=[DataRequired(), nameFieldCheck])
    add_idNo = StringField("add_idNo", validators=[DataRequired(), idNoFieldCheck, idNoExistenceCheck])
    add_gender = RadioField("add_gender", choices=[("Male", "Male"), ("Female", "Female")], validators=[InputRequired()])
    add_college = SelectField("add_college", coerce=int, choices=[(0,"-----select college-----"), (1, "Engineering and Technology"), (2, "Science and Mathematics"), (3, "Education"), (4, "Arts and Social Sciences"), (5, "Business Administration and Accountancy"), (6, "Nursing"), (7, "Computer Studies")])
    add_course = SelectField("add_course", coerce=int, choices=[])
    add_submit = SubmitField("ADD")

class SearchRegistryForm(FlaskForm):
    search_field = StringField("search_field")
    search_name = StringField("search_name", validators=[nameFieldCheck])
    search_idNo = StringField("search_idNo", validators=[idNoFieldCheck])
    search_gender = RadioField("search_gender", choices=[("Male", "Male"), ("Female", "Female")])
    search_college = SelectField("search_college", coerce=int, choices=[(0,"-----select college-----"), (1, "Engineering and Technology"), (2, "Science and Mathematics"), (3, "Education"), (4, "Arts and Social Sciences"), (5, "Business Administration and Accountancy"), (6, "Nursing"), (7, "Computer Studies")])
    search_course = SelectField("search_course", coerce=int, choices=[])