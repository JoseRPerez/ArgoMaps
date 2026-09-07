import pandas as pd


####### DATOS EXTERNOS ###########
file_carbono = 'data/carbonos.csv'
file_dobles = 'data/dobles.csv'
file_cartas = 'data/cartas.csv'
file_abells = 'data/planetary_nebula.csv'
file_exoticos = 'data/exoticos.csv'
file_galaxias = 'data/galaxias.csv'
##################################

############### RECURSOS ###############
def leer_cabono():
	return pd.read_csv(file_carbono, dtype={'AR': float, 'DEC': float})

def leer_dobles():
	return pd.read_csv(file_dobles, dtype={'AR': float, 'DEC': float})

def leer_abells():
	return pd.read_csv(file_abells, dtype={'AR': float, 'DEC': float})

def leer_exoticos():
	return pd.read_csv(file_exoticos, dtype={'AR': float, 'DEC': float})

def leer_galaxias():
	return pd.read_csv(file_galaxias, dtype={'AR': float, 'DEC': float})

def definir_cartas():
	return pd.read_csv(file_cartas, dtype={'AR_MIN': float, 'AR_MAX': float, 'DEC_MIN': float, 'DEC_MAX': float})

