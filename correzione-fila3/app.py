#   Realizzare un sito web che permetta di visualizzare l'elenco dei primi 10 clienti che hanno speso di più.
#   Il maneger di BikeStore si collega alla rotta /bestCustomers e riceve l'elenco dei clienti. Cliccando poi sull'ID di uno dei clienti,
#   si deve poter visualizzare l'elenco degli ordini effettuati. Utilizzare Bootstrap per l'interfaccia grafica.


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

#collegamento al DB
connection = pymssql.connect(server="213.140.22.237\SQLEXPRESS", user="basco.luke",password="xxx123##",database="basco.luke")

@app.route('/bestCustomers', methods=['GET'])
def table():
    # query= select *
    # from sales.customers as C inner join sales.orders as O
    # on C.customer_id = O.customer_id
    # inner join sales.order_items as OI
    # on O.order_id = OI.order_id
    return render_template("table.html")


@app.route('/inputval', methods=['GET'])
def serv():
  nome = request.args["nome"]
  cognome = request.args["cognome"]
  query = f"select * from sales.customers where sales.customers.first_name = '{nome}' and sales.customers.last_name = '{cognome}'" 
  df1 = pd.read_sql(query, connection)
  # controllo se un df è vuoto, semplice semplice
  if list(df1.values.tolist()) == []: # se dati è una lista vuota
    return render_template("error.html")
  else:
    return render_template("risultati1.html", nomicolonne = df1.columns.values, dati = list(df1.values.tolist()))




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3235, debug=True)