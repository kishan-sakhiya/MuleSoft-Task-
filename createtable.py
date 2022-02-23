# import connection file
from connection import *

try:  # handle the exception
    # create a table query with replace
    con.execute(
        "create table if not exists movies (id integer primary key autoincrement, name text, actor_name text, actress_name text, year_of_release int,  director_name text)")

    print("Table is Created")  # message show

except:
    print("Table is Not Created")  # Error message show

con.commit()  # commit the table
