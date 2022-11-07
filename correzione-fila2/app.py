#   Realizzare un sito web ch epermetta di visualizzare le informazioni riguardanti i clienti.
#   Un componente dello staff richiama la rotta /infoUser dove sono presenti due text per l'inserimento del nome
#   e del cognome del cliente ed un bottone per inviare le informazioni, Una volta inviate, il sito risponde con tutte
#   le informazioni relative a quel cliente, una sotto l'altra. Se il cliente non esiste, deve essere 
#   visualizzato un opportuno messaggio di errore. Utilizzare Bootstrap per l'interfaccia grafica di tutte le pagine.




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

@app.route('/infoUser', methods=['GET'])
def homepage():
  return render_template("homepage.html")


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