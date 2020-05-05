# from flask_wtf import FlaskForm
# from wtforms import StringField, TextAreaField, SubmitField, RadioField
# from wtforms.validators import DataRequired
# class Pitch_Form(FlaskForm):
#     title = StringField('Title', validators=[DataRequired()])
#     author = StringField('Author', validators=[DataRequired()])
#     content = TextAreaField('Write Pitch', validators=[DataRequired()])
#     category = RadioField('Pick Category', choices=[('Pickup Lines', 'Pickup Lines'), ('Interview Pitch', 'Interview Pitch'), ('Product Pitch', 'Product Pitch'), ('Promotion Pitch', 'Promotion Pitch')], validators=[DataRequired()])
#     submit = SubmitField('Submit')
# class Update_Profile(FlaskForm):
#     bio = TextAreaField('Add something more about Yourself...', validators = [DataRequired()])
#     submit = SubmitField('Submit')
# class CommentsForm(FlaskForm):
#     comment = TextAreaField('comment on the post',validators=[DataRequired()])
#     submit = SubmitField('Add Comment')

from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField, RadioField
from wtforms.validators import Required

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    vote=RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])
    submit = SubmitField('SUBMIT')  

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit') 

class PitchForm(FlaskForm):
    category_id = SelectField('Select Category', choices=[('1', 'Interview'), ('2', 'Pick Up Lines'), ('3', 'Promotion'),('4','Product')])
    content = TextAreaField('YOUR PITCH')
    submit = SubmitField('Create Pitch')

class UpvoteForm(FlaskForm):
    '''
    Class to create a wtf form for upvoting a pitch
    '''
    submit = SubmitField('Upvote')
    