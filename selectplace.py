import mysql.connector
mydb=mysql.connector.connect(host="localhost",user=" root",passwd="",database="disaster_management1")

import pandas as pd

df = pd.read_excel(r"F:\kavya\Place_Name_District.xlsx")


def getDistrict():
    return set(list(df["DISTRICT"]))

def getPlace(district):
    return list(df.query(f'DISTRICT=="{district}"')["SETNAME"])

def getlatLong(place):
	return list(df.query(f'SETNAME=="{place}"')["X"]),list(df.query(f'SETNAME=="{place}"')["Y"])