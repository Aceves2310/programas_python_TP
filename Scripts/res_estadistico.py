import numpy as np 
import pandas as pd
import argparse 

#crear un objeto de conexión
parser= argparse.ArgumentParser(description = "Programa para graficar un histograma")
parser.add_argument('archivo')
args= parser.parse_args()

df= pd.read_csv(args.archivo)
print(df.describe())      