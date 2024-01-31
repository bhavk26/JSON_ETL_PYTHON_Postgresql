import configparser
import psycopg2 as psql
import logging
from logs import init_logger
from readjson import read
import json

#def connection_start():
cf = configparser.ConfigParser()
cf.read("C://Users//bhave//PycharmProjects//pythonProject1//venv//config.ini")
conn = psql.connect(
    host=cf.get('Postgresql', 'host'),
    database=cf.get('Postgresql', 'db_name'),
    user=cf.get('Postgresql', 'user'),
    password=cf.get('Postgresql', 'pass')

)
init_logger()
cur = conn.cursor()
cur.execute('Select version()')
v = cur.fetchone()
logging.info(f'successful connected to DB version:{v} ')
#    return conn

c_query="""
DROP TABLE IF EXISTS accidents_data;
CREATE TABLE accidents_data (
    state VARCHAR(100),
    year VARCHAR(100),
    accidents INTEGER
)
"""
#creating table in Database
cur.execute(c_query)


#ingesting to Database
read()
insert_query='''INSERT INTO accidents_data(state,year,accidents) VALUES (%s,%s,%s)'''
#list of years
l=['_2008','_2009','_2010','_2011','_2012','_2013','_2014','_2015','_2016']
with open('accident.json') as f:
    data = json.load(f)
for state in data['records']:
    for i in l:
        cur.execute(insert_query, (state['states_uts'], i, state[i]))
cur.close()
logging.info('Successfully ingested JSON data to Postgresql')
#commiting changes to database
conn.commit()











