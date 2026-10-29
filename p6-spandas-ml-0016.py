import pandas as pd
import numpy as np

serie_amigos = ["Pedro","Morgan","Farfan","EL Adrian","Jesse","ELiseo","Mario"]
print ("---Serie listado de amigos NC 0016---")
amigos=pd.Series(serie_amigos)
print(amigos)

serie_billetes = [20,50,100,200,500,1000]
print ("---Serie listado de billetes MX NC 0016---")
amigos=pd.Series(serie_billetes)
print(amigos)

serie_billetes = [20,50,100,200,500,1000]
serie_bletras = ["veinte","cincuenta","cien","docientos","quinientos","mil"]
print ("---Serie listado nombre y valor de MX NC 0016---")
tablabilletes=pd.Series(serie_billetes, serie_bletras)
print(tablabilletes)
## diccionario dataframe
# diccionario de valor de moneadas
print("datos de diccionario a DataFrame en pandas")
dic_monedas ={
    "serie_billetes":[20,50,100,200,500,1000],
    "serie_bletras":["veinte","cincuenta","cien","docientos","quinientos","mil"]
}

tablabilletes=pd.DataFrame(dic_monedas,index=["A","B","C","D","E","F"])
print(tablabilletes)

print("Casa de cambio de Johan Paulo Aros NC 0016")