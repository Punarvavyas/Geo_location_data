from flask import Flask,request
from flask_cors import CORS

import mongo as m
app = Flask(__name__)
CORS(app)
@app.route('/dbcall',methods=['POST'])
def dbcall():
    return m.sql_ext()

@app.route('/sqldbcall',methods=['GET','POST'])
def sqldbcall():
    pr_name = request.form.get('struser')

    return m.sql_data(pr_name)

@app.route('/mongodbcall',methods=['GET','POST'])
def mongodbcall():

    pr1_name = request.form.get('str1user')

    return m.mongo_ext(pr1_name)



if __name__ == '__main__':
    app.run()
