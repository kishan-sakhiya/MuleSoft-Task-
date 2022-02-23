from connection import *

try:
    # select query in fetch all data
    data = con.execute("select * from movies")

    # use a for loop
    for row in data:
        # print all row
        print('id={0},movie name = {1},actor name = {2},actress name = {3},year of release = {4},director name = {5}'.format(
            row[0], row[1], row[2], row[3], row[4], row[5]))

    print("Information is show")

except:
    print("Data not fatched")

con.commit()  # commit the file
