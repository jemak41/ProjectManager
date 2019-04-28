from app import db
from datetime import datetime
from time import time


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(128), index=True, unique=True)
    project = db.relationship('Project', backref='status', lazy='dynamic')

    def __repr__(self):
        return self.status

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(128), index=True, unique=True)
    project = db.relationship('Project', backref='task', lazy='dynamic')

    def __repr__(self):
        return self.task

class Technology(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    technology = db.Column(db.String(64), index=True, unique=True)
    project = db.relationship('Project', backref='technology', lazy='dynamic')

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(1000), index=True, unique=True)
    technology_id = db.Column(db.Integer, db.ForeignKey('technology.id'))
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
    target_start_date = db.Column(db.DateTime, default=datetime(1900, 1, 1))
    target_end_date = db.Column(db.DateTime, default=datetime(1900, 1, 1))
    actual_start_date = db.Column(db.DateTime, default=datetime(1900, 1, 1))
    actual_end_date = db.Column(db.DateTime, default=datetime(1900, 1, 1))
    remarks = db.Column(db.String(5000), index=True)

    def __repr__(self):
        return self.project_name
