import openpyxl

# Abre el archivo Excel
workbook = openpyxl.load_workbook('Lista.xlsx')

# Selecciona la hoja en la que se aplicará el incremento porcentual
worksheet = workbook['Table 1']

# Define el incremento porcentual
incremento_porcentual = 0.10  # 10%

# Itera sobre las celdas de la columna y aplica el incremento porcentual
for cell in worksheet['B']:  # Cambia 'B' por la letra de la columna que deseas actualizar
    if isinstance(cell.value, (int, float)):
        cell.value *= (1 + incremento_porcentual)

# Guarda los cambios en el archivo Excel
workbook.save('Lista.xlsx')
