"""""import pandas as pd
dataset_credits = pd.read_csv("./credits_dataset_final.csv")
df = pd.read_csv("./movies_dataset_final.csv")
merged_dataset = pd.merge(df, dataset_credits, on="id", how="inner")
merged_dataset.to_csv("./dataset.csv", index=False)
print("Dataset combinado guardado como 'dataset.csv'.")
dataset= pd.read_csv("./dataset.csv")
# Eliminar columnas específicas
columnas_a_eliminar = ["original_language", "production_countries", "runtime", "spoken_languages", "status", "tagline", "collection_id","collection_name", "production_company_names"]
dataset_final = dataset.drop(columns=columnas_a_eliminar)

# Guardar el nuevo dataset en un archivo CSV
dataset_final.to_csv('dataset_final.csv', index=False)
columnas_seleccionadas = ['release_date', 'title', 'release_year', "vote_average", "vote_count"]
dataset_funciones_basicas = dataset[columnas_seleccionadas]
dataset_funciones_basicas.to_csv('dataset_funciones_basicas.csv', index=False)
columnas_seleccionadass = ['id', 'title', 'return', "actor_names", "director_name", "revenue", "budget", "release_date"]
dataset_actor_director = dataset_final[columnas_seleccionadass]
dataset_actor_director.to_csv('dataset_actor_director.csv', index=False)
columnas_seleccionadasss = ['vote_average', 'title', 'vote_count', "popularity", "overview", "genre_names"]
dataset_modelo = dataset_final[columnas_seleccionadasss]
dataset_modelo.to_csv('dataset_modelo.csv', index=False) """""