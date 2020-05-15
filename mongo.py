import pymysql
import json
from main import Flask
from pymongo import MongoClient
from bson.json_util import dumps
from bson import BSON
from bson import json_util
import time

def mongo_ext(str1):
    client = MongoClient('mongodb://localhost:27017/')
    db = client.geo
    t0=time.clock()
    rowss=db.geaodata.find({"GEO":str1})
    t1=time.clock()
    total=t1-t0
    print("mongo db Time:")
    print(total)
    ls=[]
    for row in rowss:
        ls.append(row)

    return dumps(ls)




def sql_ext():
    con = pymysql.connect('localhost', 'root',
                          'punu8866', 'geo')

    with con:

        cur1 = con.cursor()


        cur1.execute("SELECT DISTINCT GEO FROM cleaneddata")
        rows1=cur1.fetchall()

        print(json.dumps(rows1))
        return json.dumps(rows1)



def sql_data(str):
    con = pymysql.connect('localhost', 'root',
                          'punu8866', 'geo')
    #print(str)

    with con:
        cur = con.cursor()
        t2 = time.clock()
        cur.execute("SELECT * FROM cleaneddata where GEO='"+str+"' ")
        t3 = time.clock()

        total1=t3-t2
        print("mysql time")
        print(total1)
        rows=cur.fetchall()

        return json.dumps(rows)


#mongo_ext('Canada')
#sql_data("Canada")

#print(m)
#print(n)
#sql_ext()
