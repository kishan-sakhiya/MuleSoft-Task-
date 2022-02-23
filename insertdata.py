# import connection file
from connection import *

try:

    # insert query with autoincrement id
    con.execute(
        "insert into movies (name, actor_name, actress_name,year_of_release, director_name) values('Chak De! India','Shah Rukh Khan','Vidya Malvade',2007,'Shimit Amin')")

    con.execute(
        "insert into movies (name, actor_name, actress_name,year_of_release, director_name) values('Lakshya','Hrithik Roshan','Preity Zinta',2004,'Farhan Akhtar')")

    print("Data inserted")

except:
    print("Data Not Inserted")

# commit the query
con.commit()
