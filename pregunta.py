"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():
    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df = df.apply(lambda x: x.astype(str).str.lower())    
    df = df.replace("_", " ", regex=True)
    df = df.replace("-", " ", regex=True)
    df = df.drop_duplicates()

    return df
