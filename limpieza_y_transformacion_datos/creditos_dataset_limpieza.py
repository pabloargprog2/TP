"""""import pandas as pd
import ast

ruta_dataset = "./credits.csv"
df = pd.read_csv(ruta_dataset) # Función para extraer nombres de los actores
def get_actor_names(cast_column):
    try:
        cast_list = ast.literal_eval(cast_column)  # Convertir cadena JSON a lista
        return ", ".join([member['name'] for member in cast_list if 'name' in member])
    except (ValueError, SyntaxError):
        return None

# Función para extraer el nombre del director
def get_director_name(crew_column):
    try:
        crew_list = ast.literal_eval(crew_column)  # Convertir cadena JSON a lista
        for member in crew_list:
            if member.get('job') == 'Director':
                return member.get('name')
        return None
    except (ValueError, SyntaxError):
        return None

# Crear las nuevas columnas
df['actor_names'] = df['cast'].apply(get_actor_names)
df['director_name'] = df['crew'].apply(get_director_name)
# Crear el nuevo dataset con las columnas deseadas
new_df = df[['id', 'actor_names', 'director_name']]

# Guardar el nuevo dataset a un archivo CSV
new_df.to_csv("credits_dataset_final.csv", index=False)

print("Nuevo dataset creado y guardado como 'creditos_dataset_final.csv'")
"""""