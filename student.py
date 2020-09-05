"""
 simple example for basic undersatnding of why we need sqlalchemy
 just because of that we get rid of writting long query
 it is time saving
 risk of syntax error is very less
"""


from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///college.db', echo = True)

meta = MetaData()
# create table student

students = Table('students', meta,Column('id', Integer, primary_key = True),
	                              Column('name', String),
	                              Column('lastname', String),)

meta.create_all(engine)
#for inserting the data

ins = students.insert()
ins = students.insert().values(name = 'Rashmi', lastname = 'sahu')
ins1 = students.insert().values(name = 'Ravi', lastname = 'kapoor')

s = students.select()

conn = engine.connect()

result1 = conn.execute(ins)
result1 = conn.execute(ins1)
result = conn.execute(s)
# it shows all entries that is in  database

for row in result:
   print (row)