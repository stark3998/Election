# -*- coding: utf-8 -*-
import time
import json
from aap_election import db
from flask_script import Command
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from aap_election.model.election import State, District, AC, Station
from aap_election.api.user import create_state, create_district, create_ac, create_station
import os
import psycopg2

cwd = os.getcwd()


cur_state=None
cur_district=None
cur_ac=None


class Election(Command):

    def run(self):
        cur_state=str(State.query.order_by(State.created_at.desc()).first().state_name)
        cur_district=District.query.order_by(District.created_at.desc()).first()
        cur_ac=AC.query.order_by(AC.created_at.desc()).first()
        cur_station=Station.query.order_by(Station.created_at.desc()).first()
        print(cur_state)
        url="http://psleci.nic.in/"
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('--start-maximized')
            options.add_argument('--headless')
            driver = webdriver.Chrome(cwd + '/aap_election/driver/chromedriver', options=options)
            driver.get(url)
        except:
            print("ChromeDriver Error")

        x=Select(driver.find_element_by_id("ddlState"))

        print("Total Number of States : ",len(x.options))
        
        state=x.options
        st=[]
        for i in x.options:
            st.append(i.text)

        print("Available States : ",st)
        
        if(st.index(cur_state)>0):
            state_pos=st.index(cur_state)
        else:
            state_pos=1

        #for i in range(state_pos+1,len(x.options)):
        for i in range(1,len(x.options)):
            district=[]
            x=Select(driver.find_element_by_id("ddlState"))
            x.options[i].click()
            y=Select(driver.find_element_by_id("ddlDistrict"))

            for a in y.options:
                district.append(a.text)

            district=district[1:]
            print("\n Available Districts : ",district)

            try:
                new_state=create_state(str(st[i]))
                cur_state=new_state.id
            except Exception as error:
                print(error)

            for j in range(1,len(y.options)):
                y=Select(driver.find_element_by_id("ddlDistrict"))
                y.options[j].click()
                z=Select(driver.find_element_by_id("ddlAC"))
                ac=[]
                for a in z.options:
                    ac.append(a.text)
                ac=ac[1:]

                print("Loaded AC's : ",ac)


                try:
                    new_district=create_district(str(district[j]),cur_state)
                    print(new_district)
                    cur_district=new_district.id
                except Exception as y:
                    print(y)

                for k in range(1,len(z.options)):
                    z=Select(driver.find_element_by_id("ddlAC"))
                    z.options[k].click()
                    print("\n\n\n Loading AC \n\n\n")
                    l=Select(driver.find_element_by_id("ddlPS"))
                    pollst=[]

                    for a in l.options:
                        pollst.append(a.text)

                    pollst=pollst[1:]
                    
                    try:
                        new_ac=create_ac(str(ac[k]),cur_district)
                        print(new_ac)
                        cur_ac=new_ac.id
                    except Exception as error:
                        print(error)
                        
                    for m in pollst:
                        print(str(st[i]),str(district[j]),str(ac[k]),str(m))
                        try:
                            new_station=create_station(str(m),cur_ac)
                            print(new_station)
                        except Exception as error:
                            print(error)