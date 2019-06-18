# -*- coding: utf-8 -*-
from aap_election import db
from aap_election.model.base import Base


class State(Base):
    __tablename__ = 'state'
    state_name=db.Column(db.String(25), unique=True)
    districts = db.relationship("District")
	

class District(Base):
    __tablename__ = 'district'
    state_id=db.Column(db.Integer, db.ForeignKey('state.id'))
    district_name=db.Column(db.String(50), unique=True)
    acs = db.relationship("AC")

class AC(Base):
    __tablename__ = 'ac'
    district_id=db.Column(db.Integer, db.ForeignKey('district.id'))
    ac_name=db.Column(db.String(50), unique=True)
    stations = db.relationship("Station")

class Station(Base):
    __tablename__ = 'station'
    ac_id=db.Column(db.Integer, db.ForeignKey('ac.id'))
    station_name=db.Column(db.String(100))