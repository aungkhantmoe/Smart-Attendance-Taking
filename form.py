from flask_wtf import FlaskForm 
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class register_form(FlaskForm):
    userid = StringField('userid', 
                            validators=[DataRequired(), Length(min=9)])
                
    name = StringField('name',validators=[DataRequired()])

    email = StringField('email', validators = [DataRequired(),Email()])

    picture = FileField('picture', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])

    submit = SubmitField('signup')
