# -*- coding: utf-8 -*-
__author__ = ''

from aap_election.model.election import State, District, AC, Station
from aap_election import ma
from aap_election.schemas import safe_execute

class StateSchema(ma.ModelSchema):
    districts=ma.Nested('DistrictSchema',many=True)
    class Meta:
	model=State
    exclude=('created_at','updated_at')

class DistrictSchema(ma.ModelSchema):
    acs=ma.Nested('ACSchema',many=True)
    class Meta:
        model=District
        exclude=('created_at','updated_at')

class ACSchema(ma.ModelSchema):
    stations=ma.Nested('StationSchema',many=True)
    class Meta:
        model=AC
        exclude=('created_at','updated_at')

class StationSchema(ma.ModelSchema):
    class Meta:
        model=Station
        exclude=('created_at','updated_at')