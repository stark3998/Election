from aap_election.model.election import State, District, AC, Station


def create_state(name=""):
    if name or number:
	try:
		ob = State(state_name=name)
        	ob.save()
		return ob
	except Exception as e:
        	return e

def create_district(name="",s_id=None):
    if name or number:
	try:
	        ob = District(district_name=name,state_id=s_id)
	        ob.save()
	        return ob
	except Exception as e:
		return e

def create_ac(name="", d_id=None):
    if name or number:
        try:
		ob = AC(ac_name=name,district_id=d_id)
        	ob.save()
        	return ob
	except Exception as e:
		return e

def create_station(name="", a_id=None):
    if name or number:
        ob = Station(station_name=name, ac_id=a_id)
        ob.save()
        return ob
