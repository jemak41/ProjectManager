from app import app, db
from flask import render_template, flash, url_for, redirect, request
from app.forms import Menu, New, EditEmpty, Edit, Delete
from app.models import Project, Status, Task, Technology
from datetime import datetime
import pygal
from sqlalchemy import extract

def getDate(dateText):
    return datetime(int(dateText[:4]),int(dateText.split('-')[1]),int(dateText[-2:]))

def getTechCount(technology_id):
    lis = []
    x = 1
    while x <= 12:
        lis.append(len(Project.query.filter_by(technology_id=technology_id).filter(extract('month', Project.actual_start_date)==x).all()))
        x += 1
    return lis


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    active_projects = len(Project.query.filter(~Project.status_id.in_([4])).all())
    onhold_projects = len(Project.query.filter_by(status_id=5).all())
    completed_projects = len(Project.query.filter_by(status_id=4).all())

    line_chart = pygal.Line()
    line_chart.title = 'Projects Started for each Programming Language per month'
    line_chart.x_labels = map(str, range(1, 12))
    for x in Technology.query.all():
        line_chart.add(x.technology, getTechCount(x.id))
    line_chart_data = line_chart.render_data_uri()

    return render_template('index.html', line_chart_data=line_chart_data, active_projects=active_projects,
                           onhold_projects=onhold_projects, completed_projects=completed_projects)


@app.route('/new', methods=['GET', 'POST'])
def new():
    form = New()
    form.technology.choices = [(x.id, x.technology) for x in Technology.query.all()]

    if request.method == 'POST':
        project = Project(project_name=form.project_name.data,
                          technology_id = form.technology.data,
                          description = form.description.data,
                          status_id=1,
                          task_id=1,
                          target_start_date=datetime.combine(form.target_start_date.data, datetime.min.time()),
                          target_end_date=datetime.combine(form.target_end_date.data, datetime.min.time()),
                          remarks=form.remarks.data
                          )
        db.session.add(project)
        db.session.commit()
        flash(form.project_name.data + ' have been created.')
        return redirect(url_for('index'))
    return render_template('new.html', form=form)


@app.route('/editempty', methods=['GET', 'POST'])
def editempty():
    form = EditEmpty()
    form.project_name.choices = [(x.id, x) for x in Project.query.all()]

    if request.method == 'POST':
        return redirect(url_for('edit', id=form.project_name.data))
    return render_template('editempty.html', form=form)


@app.route('/edit', methods=['GET', 'POST'])
def edit():

    id = request.args.get('id')
    project = Project.query.filter_by(id=id).first()
    form = Edit()
    form.id.data = str(id)
    form.project_name.data = project.project_name
    form.technology.data = project.technology_id
    form.description.data = project.description
    form.status.data = project.status_id
    form.task.data = project.task_id
    form.target_start_date.data = project.target_start_date
    form.target_end_date.data = project.target_end_date
    form.actual_start_date.data = project.actual_start_date
    form.actual_end_date.data = project.actual_end_date
    form.remarks.data = project.remarks

    if request.method == 'POST':
        if form.submit.data:
            project.project_name = form.project_name.raw_data[0]
            project.technology_id = form.technology.raw_data[0]
            project.description = form.description.raw_data[0]
            project.status_id = form.status.raw_data[0]
            project.task_id = form.task.raw_data[0]
            project.target_start_date = getDate(form.target_start_date.raw_data[0])
            project.target_end_date = getDate(form.target_end_date.raw_data[0])
            project.actual_start_date = getDate(form.actual_start_date.raw_data[0])
            project.actual_end_date = getDate(form.actual_end_date.raw_data[0])
            project.remarks = form.remarks.raw_data[0]
            db.session.commit()
            flash('Your changes have been saved.')
            return redirect(url_for('index'))
        elif form.delete.data:
            return redirect(url_for('delete', id=id))
    return render_template('edit.html', id=request.args.get('id'), form=form)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    id = request.args.get('id')
    project = Project.query.filter_by(id=id).first()
    form = Delete()

    if form.yes.data:
        db.session.delete(project)
        db.session.commit()
        flash('Project has been deleted')
        return redirect(url_for('index'))
    elif form.no.data:
        return redirect(url_for('edit', id=id))

    return render_template('delete.html', form=form, project=project)
