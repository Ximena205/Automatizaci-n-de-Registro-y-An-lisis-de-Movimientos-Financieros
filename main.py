import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV
df = pd.read_csv('movimientos.csv', parse_dates=['FECHA'])

# Mostrar los primeros registros
#print(df.head())

# Verificar valores nulos
if df.isnull().any().any():
    print("⚠️ Hay datos faltantes. Revisar el archivo.")

# Convertir montos a una sola moneda (ej: USD a UYU con tasa simulada)
tasa_usd_uyu = 39  # valor estimado
df['Monto_UYU'] = df.apply(
    lambda row: row['MONTO'] * tasa_usd_uyu if row['MONEDA'] == 'USD' else row['MONTO'], axis=1
)

# Agrupar por tipo de movimiento
resumen = df.groupby('TIPO')['Monto_UYU'].sum()
print("\nResumen por tipo de operación:")
#print(resumen)

# Visualización
resumen.plot(kind='bar', color='skyblue')
plt.title('Resumen de Movimientos Financieros (UYU)')
plt.ylabel('Monto')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('resumen.png')
plt.show()

# Exportar reporte a Excel
with pd.ExcelWriter('reporte_financiero.xlsx') as writer:
    df.to_excel(writer, sheet_name='Movimientos', index=False)
    resumen.to_frame(name='Monto Total').to_excel(writer, sheet_name='Resumen')