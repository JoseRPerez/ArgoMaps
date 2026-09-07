from calls import getMyLabel
from definitions import DARK_NEBULA, EMISSION_NEBULA, REFLECTION_NEBULA, size_ring_nebula, limit_nebula_mag, SUPERNOVA_REMNANT, PLANETARY_NEBULA, HII_IONIZED_REGION, STAR_CLUSTER_NEBULA, NEBULA
from starplot import _, DsoType, DSO



def PlotNebulas(p):
	#tomamos el tamaño aparente del anillo como referencia	
	#helix = DSO.get(ngc="7293")
	#turtleNeb = DSO.get(ngc="6210")	
	
	big_limit_size = 0.07407469 # helix.size tamaño de la helix	
	small_limit_size = 0.00006944	# turtleNeb.size tamaño de ngc 6210 la tortuga
	
	#p.style.dso_nebula.marker.zorder = 1000

	#Nebulosas grandes
	p.style.dso_nebula.marker.edge_color = "#69b655"	#verde
	p.style.dso_nebula.marker.color = "#69b655"			#verde
	p.style.dso_planetary_nebula.marker.edge_color = "#69b655"
	p.style.dso_planetary_nebula.marker.fill = "none"
	
	#p.messier()	

	p.dsos(
		where=[
			_.type.isin(
				[                
					DsoType.NEBULA.value,
					DsoType.EMISSION_NEBULA.value,
					DsoType.REFLECTION_NEBULA.value,
					DsoType.PLANETARY_NEBULA.value,
					DsoType.STAR_CLUSTER_NEBULA.value,
				]),
		  	(_.magnitude <= limit_nebula_mag) | (_.magnitude.isnull()),
			(_.size > small_limit_size) & (_.size < 4.75),
		],
		where_true_size=[_.size >= big_limit_size],
		label_fn=getMyLabel,
	)
	
	#Nebulosas planetarias pequeñas
	p.style.dso_planetary_nebula.marker.edge_color = "red"
	p.style.dso_planetary_nebula.marker.fill = "none"
	#p.style.dso_planetary_nebula.marker.size = 15

	p.dsos(
		where=[
			_.type.isin(
				[                
					DsoType.PLANETARY_NEBULA.value,			
				]),
		  	(_.magnitude <= limit_nebula_mag) | (_.magnitude.isnull()),
			_.size <= small_limit_size,
		],
		where_true_size=[False],
		label_fn=getMyLabel,
	)


	#Regiones HII y remanentes
	#p.style.dso_nebula.marker.symbol = 'square'
	p.style.dso_nebula.marker.edge_color = "tomato"
	#p.style.dso_nebula.marker.size = 7
	#p.style.dso_nebula.marker.fill = "full"
	p.style.dso_nebula.marker.color = "tomato"
	#p.style.dso_nebula.marker.alpha = 0.3
	#p.style.dso_nebula.label.offset_x = "auto"
	#p.style.dso_nebula.label.offset_y = "auto"

	p.dsos(
		where=[
			_.type.isin(
				[                
					DsoType.HII_IONIZED_REGION.value,
					DsoType.SUPERNOVA_REMNANT.value,
				]),
		  	(_.magnitude < limit_nebula_mag) | (_.magnitude.isnull()),
			#(_.size > small_limit_size) & (_.size < 3),
			#(_.m.isnull()),
		],
		where_true_size = [_.size >= big_limit_size],
		label_fn=getMyLabel,
	)


	#DARK NEBULA
	#p.style.dso_nebula.marker.symbol = 'square'
	p.style.dso_nebula.marker.edge_color = "lightgray"
	#p.style.dso_nebula.marker.size = 7
	#p.style.dso_nebula.marker.fill = "full"
	p.style.dso_nebula.marker.color = "black"
	#p.style.dso_nebula.marker.alpha = 0.3
	#p.style.dso_nebula.label.offset_x = 7
	#p.style.dso_nebula.label.offset_y = 7

	p.dsos(
		where=[
			_.type.isin(
				[                
					DsoType.DARK_NEBULA.value,
				]),
		  	#(_.magnitude < limit_nebula_mag) | (_.magnitude.isnull()),
		],
		where_true_size = [_.size >= big_limit_size],
		label_fn=getMyLabel,
	)


'''
def plotPN(p):
	getSmall_PN(p)
	getBig_PN(p)
	getHelix(p)


def plotNebs(p):
	getReflAndEmiNeb(p)
	getDarkNeb(p)
	plotHIIandSR(p)


def plotHIIandSR(p):
	#p.style.dso_hii_ionized_region.marker.alpha = 0.3
	p.style.dso_supernova_remnant.marker.alpha = 0.3

	# nebulosas pequeñas
	p.dsos(
		where=[(_.type == HII_IONIZED_REGION) | (_.type == SUPERNOVA_REMNANT) , _.magnitude <= limit_nebula_mag, _.size <= 0.1],
		label_fn=getMyLabel,
		true_size = False,
	)

	# nebulosas grandes
	# Si no meto magnitudes no definidas no entra pacman
	p.dsos(
		where=[(_.type == HII_IONIZED_REGION) | (_.type == SUPERNOVA_REMNANT) ,
		(_.magnitude <= limit_nebula_mag) | (_.magnitude.isnull()) , _.size > 0.1],
		label_fn=getMyLabel,
		true_size = True,
	)


def getReflAndEmiNeb(p):
	p.style.dso_nebula.marker.size = 7
	p.style.dso_nebula.marker.symbol = 'square'
	p.style.dso_nebula.marker.alpha = 0.3
	p.style.dso_nebula.label.offset_x = 7
	p.style.dso_nebula.label.offset_y = 7
	
	
	p.nebula(
		where=[(_.type == REFLECTION_NEBULA) | (_.type == EMISSION_NEBULA) , _.magnitude <= limit_nebula_mag, _.size <= 0.1],
		label_fn=getMyLabel,
		true_size=False, 
	)

	p.nebula(
		where=[(_.type == REFLECTION_NEBULA) | (_.type == EMISSION_NEBULA) , _.magnitude <= limit_nebula_mag, _.size > 0.1],
		label_fn=getMyLabel,
		true_size=True, 
	)
	
	p.nebula(
		where=[(_.type == STAR_CLUSTER_NEBULA) | (_.type == NEBULA),
		_.magnitude <= limit_nebula_mag, _.size > 0.1],
		label_fn=getMyLabel,
		true_size=True, 
	)


def getDarkNeb(p):
	#p.style.dso_hii_ionized_region.marker.alpha = 0.3
	p.dsos(
		where=[_.type == DARK_NEBULA ],
		label_fn=getMyLabel,
		true_size=False,
	)



def getSmall_PN(p):
	##desafios de planetarias (very small size)
	p.style.dso_planetary_nebula.marker.edge_color = "red"
	p.style.dso_planetary_nebula.marker.size = 15

	p.nebula(
		where=[_.type == PLANETARY_NEBULA, _.size <= 0.00001, _.magnitude <= limit_nebula_mag],
		label_fn=getMyLabel,
		true_size=False,
	)


def getBig_PN(p):
	#Dibuja nebulosas planetarias y de emisión pero no HII ni SNR
	#Machaco ajustes de estilo porque desde yml no esta funcionando
	p.style.dso_planetary_nebula.marker.size = 15
	p.style.dso_planetary_nebula.marker.edge_color = '#69b655'
	p.style.dso_planetary_nebula.marker.color = None
	p.style.dso_planetary_nebula.marker.fill = 'none'
	
	p.nebula(
		where=[(_.size <= size_ring_nebula) & (_.size > 0.00001), _.magnitude <= limit_nebula_mag, _.type == PLANETARY_NEBULA],
		label_fn=getMyLabel,
		true_size=False,
	)

def getHelix(p):
	#Agregamos a mano la helix Nebula pues al poner en la linea de arriba true_size = True no toma el icono correcto
	p.style.dso_planetary_nebula.marker.size = 25
	p.style.dso_planetary_nebula.marker.edge_color = '#69b655'
	p.style.dso_planetary_nebula.marker.color = None
	p.style.dso_planetary_nebula.marker.fill = 'none'

	p.nebula(
		where=[_.type == PLANETARY_NEBULA, _.size > size_ring_nebula, _.magnitude <= limit_nebula_mag],
		label_fn=getMyLabel,
		true_size=False,
	)







#EN UN PRINCIPIO NO HACEMOS USO DE ESTE METODO
def getBig(p):
	#Nebulosas muy grandes, estilo diferente para que muestre bien la etiqueta
	p.style.dso_planetary_nebula.marker.edge_color = "#69b655"
	p.style.dso_nebula.label.offset_x = 7
	p.style.dso_nebula.label.offset_y = 7
	
	p.nebula(
		where=[_.type != PLANETARY_NEBULA , _.size > size_ring_nebula, _.magnitude < limit_nebula_mag],
		label_fn=getMyLabel,
		true_size=True,
	)

'''
