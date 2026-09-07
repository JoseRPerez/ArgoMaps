#from turtle import mainloop
from starplot import _, settings
import load_ext_files as load
from calls import *
from definitions import *
from chart_def import *
from nebulas import PlotNebulas
from galaxies import *
from clusters import *
from marker import plotMarker
from myDSOs import *
from coord_extract import extractor
from clusters import *
import pandas as pd
import gc
import matplotlib.pyplot as plt

##### CARGA DATOS PERSONALIZADOS #####
cartas = load.definir_cartas()
######################################

#settings.language = "en"


def plotDSOs(p):
	#plotBigGC(p)	#ok
	#plotSmallGC(p)	#ok
	plotClusters(p)

	#plotSmall_OC(p)	#ok
	#plotBig_OC(p)	#ok

	#plotPN(p)		#ok
	#plotNebs(p)		#ok
	
	PlotNebulas(p)	
	
	#plot_SmallGlx(p)#ok
	#plot_BigGlx(p)	#ok
	plot_Glx(p)
	
	plotDobles(p)	#ok
	

def mainPlot(carta, nivel, objeto, isStar):
	semicampoAR = 1.2 * 15	#h a grados
	semicampoDEC= 18
	
	# Caso 1: Carta por defecto la de objeto	
	if not any([carta, nivel, objeto, isStar]):
		return PlotOne(*getDataChart())

	# Caso 2: Centrado en Objeto o Estrella
	if objeto or isStar:
		data = getStarData() if isStar else getData()
		ra, dec, tipo, label = data[:4]

		return PlotOne(
			ra - semicampoAR,
			ra + semicampoAR,
			dec - semicampoDEC,
			dec + semicampoDEC,
			tipo,
			label,
			(ra, dec)
		)
	
	# Caso 3: Filtrado por carta o nivel usando Pandas directamente
	filtro = pd.Series(False, index=cartas.index)
	if carta:
		filtro |= (cartas['TITLE'] == carta)
	if nivel:
		filtro |= (cartas['TITLE'].str[0] == nivel)

	for _, row in cartas[filtro].iterrows():
		PlotOne(
			row['AR_MIN'] * 15,
			row['AR_MAX'] * 15,
			row['DEC_MIN'],
			row['DEC_MAX'],
			None,
			row['TITLE'],
			None
		)
	

def PlotOne(ra_min,ra_max,dec_min,dec_max,tipo,label,coords):
	print(f'{label}: {ra_min} -> {ra_max} // {dec_min} -> {dec_max}')

	try:	
		p = definir_mapa(ra_min, ra_max, dec_min, dec_max)

		p.title(label)	
		plotBasicElements(p)
		plotStars(p)

		plotDSOs(p)

		# Objetos de coleccion personal
		plotCarbon(p)
		#plotDobles(p)
		plotAbells(p)
		plotExotic(p)
		plotMyGalaxies(p)
		
		# Agregamos un circulo tipo telrad para caso objeto/estrella	
		plotMarker(p, tipo, coords, label)

		# Esportamos la carta
		p.export(f"{label}.png", padding=0.08, transparent = False)
	except Exception as e:
		print(f"Error generando carga: {e}")
	finally:	
		del(p.style)
		del(p)
		plt.close("all")
		gc.collect()
	

def getData():
	ar = float(input("AR del objeto en formato decimal (0-24): ")) * 15
	dec= float(input("DEC del objeto en formato decimal: "))
	tipo=input("Tipo de Objeto (PN, N, G, GCl, OC, Car, Doble, DobleColorida, EX): ")
	label=input("Etiqueta del objeto: ")

	return (ar,dec,tipo,label)


def getStarData():
	tipo=input("Tipo de Objeto (Doble, DobleColorida): ")
	label=input("Etiqueta de la Estrella: ")
	datos = extractor()
	
	return (datos[0] * 15 ,datos[1],tipo,label)


def getDataChart():
	ar_min = float(input("AR min de la carta en formato decimal (0-24): ")) * 15
	ar_max = float(input("AR max de la carta en formato decimal (0-24): ")) * 15
	
	dec_min= float(input("DEC min de la carta en formato decimal: "))
	dec_max= float(input("DEC max de la carta en formato decimal: "))
	
	label=input("Etiqueta de la carta: ")

	return ar_min,ar_max,dec_min,dec_max,None,label,None


def Salir():
	exit()


def CoordCarta():
	mainPlot(False,False,False,False)

def CoordStar():
	mainPlot(False,False,False,True) 


def CartaObjeto():
	mainPlot(False,False,True,False)


def Cartas():
	for key,value in menu2.items():
		print(f'{key}: {value[0]}')
	op = input("Opción: ")

	menu2[op][1]()


def printOneChart():
	carta = input("Nombre de la carta: ")
	mainPlot(carta,False,False,False)


def printLevel():
	nivel = input("Nivel (0 al 4): ")
	mainPlot(False,nivel,False,False)

####### MAIN #######

menu1 = {
	'1': ('\tImprimir Carta Objeto', CartaObjeto),
	'2': ('\tImprimir Cartas', Cartas),
	'3': ('\tCarta por Coordenadas', CoordCarta),
	'4': ('\tCarta para Estrella', CoordStar),
	'x': ('\tSalir', Salir)
}

menu2 = {
	'1': ('\tImprimir Carta', printOneChart),
	'2': ('\tImprimir Nivel Completo', printLevel),
}


print("Si se produce un error en no se que geometry")
print("hay que comentar la linea p.milky_way() de chart_def.py")

while True:
	print("Seleccionar Opción:")

	for key,value in menu1.items():
		print(f'{key}: {value[0]}')

	op = input("Opción: ")

	menu1[op][1]()	##ejecucion de la funcion





