import pandas as pd

# Datos iniciales para Antas en 2024
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre", "Año 2023"]
horas = [306, 300, 368, 392, 437, 440, 448, 422, 375, 350, 307, 299, 4450]
minutos = [36, 53, 14, 22, 28, 6, 47, 38, 7, 42, 33, 35, 1]

# Convertir horas y minutos en minutos totales
minutos_totales = [(h * 60) + m for h, m in zip(horas, minutos)]

# Crear un DataFrame con la información para Antas en 2024
df_antas_2024 = pd.DataFrame({
    'Mes': meses,
    'Horas de Sol en Antas': horas,
    'Minutos de Sol en Antas': minutos,
    'Minutos Totales de Sol en Antas': minutos_totales
})

# Guardar el DataFrame como un archivo CSV
df_antas_2024.to_csv('horas_de_sol_antas_2024.csv', index=False)

print(df_antas_2024)
