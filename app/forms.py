from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DateField, TextAreaField, SelectField
from wtforms.widgets import TextArea
from wtforms.fields.html5 import DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import Project, Task, Status

class Menu(FlaskForm):
    new_project = SubmitField('New Project')
    edit_project = SubmitField('Edit Project')
    graphs = SubmitField('Graphs')

class New(FlaskForm):
    project_name = StringField(('Project Name'), validators=[DataRequired()])
    technology = SelectField('Technology', choices=[])
    description = StringField('Description', widget=TextArea())
    target_start_date = DateField('Target Start Date', format='%Y-%m-%d', validators=[DataRequired()])
    target_end_date = DateField('Target End Date', format='%Y-%m-%d', validators=[DataRequired()])
    remarks = StringField('Remarks', widget=TextArea())
    submit = SubmitField('Create')

class EditEmpty(FlaskForm):
    #choices = [(x.id, x) for x in Project.query.all()]
    project_name = SelectField('Project Name', choices=[])
    submit = SubmitField('Modify')

class Edit(FlaskForm):
    id = StringField('ID', default='', render_kw={'readonly':True} )
    project_name = StringField('Project Name')
    technology = StringField('Technology')
    description = StringField('Description', default='', widget=TextArea())
    status = StringField('Status', default='')
    task = StringField('Task', default='')
    target_start_date = DateField('Target Start Date', default='', format='%Y-%m-%d', validators=[DataRequired()])
    target_end_date = DateField('Target End Date', default='', format='%Y-%m-%d', validators=[DataRequired()])
    actual_start_date = DateField('Actual Start Date', default='', format='%Y-%m-%d', validators=[DataRequired()])
    actual_end_date = DateField('Actual End Date', default='', format='%Y-%m-%d', validators=[DataRequired()])
    remarks = StringField('Remarks', default='', widget=TextArea())
    submit = SubmitField('Save Changes')
    delete = SubmitField('Delete')

class Delete(FlaskForm):
    yes = SubmitField('Yes')
    no = SubmitField('No')