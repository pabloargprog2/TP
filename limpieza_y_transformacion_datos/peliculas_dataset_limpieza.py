"""""import pandas as pd
ruta_dataset = "./movies_dataset.csv"
df = pd.read_csv(ruta_dataset)

#eliminacion columnas solicitadas
columnas_a_eliminar = ['video', 'imdb_id', 'adult', 'original_title', 'poster_path', 'homepage']
df = df.drop(columns=columnas_a_eliminar)
#rellenar con 0 en las columnas solicitadas
df[['revenue', 'budget']] = df[['revenue', 'budget']].fillna(0)
print(df[['revenue', 'budget']].isnull().sum())
#eliminacion de valores nulos de la columna solicitada
df = df.dropna(subset=['release_date'])
# Convertir las columnas 'revenue' y 'budget' a numérico (reemplazando valores no válidos por NaN)
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
#creacion de la columna solicitada
df['return'] = df.apply(lambda row: row['revenue'] / row['budget'] 
                        if row['budget'] > 0 else 0, axis=1)
# Asegurarse de que la columna 'release_date' esté en formato de fecha (AAAA-mm-dd)
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# Eliminar valores nulos en 'release_date' (fechas no válidas)
#df = df.dropna(subset=['release_date'])

# Crear la columna 'release_year' extrayendo el año de la fecha de estreno
df['release_year'] = df['release_date'].dt.year

# Verificar los resultados
print(df[['release_date', 'release_year']].head())
#desanidar columna belongs_to_collection
import ast
def extract_collection_info(row):
    
    if pd.isna(row):
        return None, None
    try:
        collection = ast.literal_eval(row) if isinstance(row, str) else row
        if isinstance(collection, dict):
            return collection.get('id'), collection.get('name')
    except (ValueError, SyntaxError):
        return None, None

# Aplicar la función
df[['collection_id', 'collection_name']] = df['belongs_to_collection'].apply(
    extract_collection_info).apply(pd.Series)
#desanidar columna production_companies
def extract_company_names(row):
    if pd.isna(row):
        return None
    try:
        companies = ast.literal_eval(row) if isinstance(row, str) else row
        if isinstance(companies, list):
            return [company.get('name') for company in companies if isinstance(company, dict) and 'name' in company]
    except (ValueError, SyntaxError):
        return None

# Aplicar la función
df['production_company_names'] = df['production_companies'].apply(extract_company_names)
#desanidar columna genres
def extract_genre_names(row):
    if pd.isna(row):
        return None
    try:
        genres = ast.literal_eval(row) if isinstance(row, str) else row
        if isinstance(genres, list):
            return [genre.get('name') for genre in genres if isinstance(genre, dict) and 'name' in genre]
    except (ValueError, SyntaxError):
        return None

# Aplicar la función a la columna 'genres'
df['genre_names'] = df['genres'].apply(extract_genre_names)
# Guardar el DataFrame en un archivo CSV
df.to_csv("movies_dataset_final.csv", index=False)

print("Archivo CSV guardado exitosamente como 'movies_dataset_final.csv'.")"""""