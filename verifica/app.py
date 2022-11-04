from flask import Flask, render_template, request, redirect, url_for, Response, redirect
app = Flask(__name__)

import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import pymssql


connection = pymssql.connect(server="213.140.22.237\SQLEXPRESS", user="basco.luke",password="xxx123##",database="basco.luke")

@app.route('/', methods=['GET'])
def search():
  return render_template("homepage.html")


@app.route('/inputvar', methods=['GET'])
def inputvar():
    nome = request.args["nome"]
    cognome = request.args["cognome"]
    query = f"select * from sales.customers where first_name ='{nome}' and last_name ='{cognome}'"
    df1 = pd.read_sql(query, connection)
    return render_template("servizio.html",
    id = df1.columns[0], first_name = df1.columns[1], last_name = df1.columns[2], phone = df1.columns[3], email = df1.columns[4], street = df1.columns[5], city = df1.columns[6], state = df1.columns[7], zipcode = df1.columns[8],
    val0 = df1["customer_id"].values[0], val1 = df1["first_name"].values[0], val2 = df1["last_name"].values[0], val3 = df1["phone"].values[0], val4 = df1["email"].values[0], val5 = df1["street"].values[0], val6 = df1["city"].values[0], val7 = df1["state"].values[0], val8 = df1["zip_code"].values[0]
    )




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3225, debug=True)