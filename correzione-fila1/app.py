#Realizzare un sito web cyhe permetta di visualizzare tutti i dipendenti che lavorano in un certo store.
#Il maneger inserisce il nome dello store e clicca su un bottone che invia i dati al server. Quest'ultimo
#accede al database e restituisce i nomi e i cognomi dei dipendenti di quello store. Se il nome dello store non è presente,
#deve essere restituito un opportuno messaggio di errore. Tutta la parte grafica deve essere gestita con Bootstrap.



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

@app.route('/', methods=['GET'])
def homepage():
  return render_template("homepage.html")


@app.route('/inputval', methods=['GET'])
def serv():
  nomestore = request.args["nomestore"]
  query = f"select sales.staffs.first_name, sales.staffs.last_name from sales.stores inner join sales.staffs on sales.stores.store_id = sales.staffs.store_id where sales.stores.store_name = '{nomestore}'" 
  df1 = pd.read_sql(query, connection)
  # controllo se un df è vuoto, semplice semplice
  if list(df1.values.tolist()) == []: # se dati è una lista vuota
    return render_template("error.html")
  else:
    return render_template("risultati1.html", nomicolonne = df1.columns.values, dati = list(df1.values.tolist()))






if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3225, debug=True)