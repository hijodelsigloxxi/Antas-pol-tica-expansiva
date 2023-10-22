import pandas as pd
presupuestos = pd.read_csv("dataset/presupuesto_antas_1985_2021.csv", sep=",", encoding="ISO-8859-1")
presupuestos.loc[0]=[2022,4453453.34, 0, 4345654.54, 0] 


#Porcentaje de aumento en relacion a la media con los 8 millones
media=presupuestos["Total Ingresos"].iloc[:10].mean()
desviacion_estandar=presupuestos["Total Ingresos"].iloc[:10].std()
recibido=7459762
print("")
print("ANALISIS DE DATOS")
print("")
print(f"La media de los ultimos 10 años es {media}, con una desviación estandar de {round(desviacion_estandar)}")
porcentaje_aumento= (recibido/media)*100
print("")
print(f"El porcentaje que supondra el cobro recibido de entrada el cual es {recibido} supondra un {round(porcentaje_aumento)} % del gasto de midia anual del ayuntamiento")

recibido2=985000
porcentaje_aumento_anual= (recibido2/media)*100
print("")
print(f"El porcentaje que supondra el cobro recibido de forma anual durante 32 años el cual es {recibido2} supondra un {round(porcentaje_aumento_anual)} % del gasto de media anual del ayuntamiento")
print("")
porcentaje_aumento_al_recibir= ((recibido+recibido2)/media)*100
print(f"El porcentaje que supondra el cobro recibido tras recibir la entrada y el primer anual si ponemos la media de los ultimos 10 años como base será {round(porcentaje_aumento_al_recibir)} % del gasto de media anual del ayuntamiento")
print("")
print(f"Si dividimos la entrada entre lo que dura una legislatura tenemos {recibido/4} por año, lo que supone un total de {round(((recibido/4)+recibido2))} lo que es igual {round((((recibido/4)+recibido2)/media),1)*100}% mas anualmente durante 4 años")
print("")

viviendas_comarca = pd.read_csv("dataset/solares_comarca_corregido.csv", sep=";", encoding="ISO-8859-1")
viviendas_principales_antas= 1176
print(f"Si dividimos el dinero de la entrada entre las viviendas activas, es decir la casa habitadas en antas, sale una media de {round(recibido/viviendas_principales_antas)} por unidad de vivienda habitada")
print("")
media_coste_fotovoltaica=5000
print(f"Si se planea pagar todas las instalaciones de todas las primeras viviendas de Antas y presuponemos un coste medio de 5000, supondría un coste total de {viviendas_principales_antas*media_coste_fotovoltaica} lo que supone un {((viviendas_principales_antas*media_coste_fotovoltaica)/recibido)*100} % del dinero cobrado de entrada")
media_gasto_electricidad=140
print("")
print(f"Si cada vivienda tiene un gasto de media de 140 la suma de todas las viviendas del pueblo gastan anualmente {media_gasto_electricidad*viviendas_principales_antas*12} lo que supone un coste total en 20 años de {media_gasto_electricidad*viviendas_principales_antas*12*20}")
print("")
print(F"Siguiendo esa media, cada casa gasta anualmente de media {media_gasto_electricidad*12} al año y {media_gasto_electricidad*12*20} al cabo de 20 años")
print("")

