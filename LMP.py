import pandas as pd
import unicodedata

# Cargar el archivo original, saltando las primeras filas si no contienen encabezados
df = pd.read_csv("data/03.csv", skiprows=2)

# Limpiar nombres de columnas: quitar espacios y normalizar tildes
df.columns = df.columns.str.strip()
df.columns = [unicodedata.normalize('NFKD', col).encode('ASCII', 'ignore').decode('utf-8') for col in df.columns]

# Mostrar columnas detectadas para verificar
print("🧾 Columnas detectadas:", df.columns.tolist())

# Intentar renombrar y reorganizar columnas
try:
    df_transformado = pd.DataFrame({
        "Categoría": df["Title"],
        "Descripción": df["Descripcion"],
        "Nivel": df["Severity"],
        "Área": "BSAR-BSCO-BSCR-BSR-BSMX",  # Área fija para este caso
        "Cantidad": df["Total"]
    })

    # Guardar el nuevo archivo
    df_transformado.to_csv("03_formateado.csv", index=False)
    print("✅ Archivo transformado y guardado como '03_formateado.csv'")

except KeyError as e:
    print(f"❌ Error: No se encontró la columna esperada: {e}")
    print("💡 Revisa los nombres exactos de las columnas en el archivo original.")
