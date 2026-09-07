from starplot import MapPlot, _
from calls import getCatalog, getStarSizes, getFontSizes, getProjection, alpha
from definitions import limit_mag_star, limit_mag_star_label
from styleDef import style

def plotBasicElements(p):
    #DEFINICION DE LINEAS Y ELEMENTOS BASICOS DE LA CARTA
	p.gridlines()
	p.constellations()
	p.constellation_borders()
	p.celestial_equator(style = None, label = 'Ecuador Celeste')
	#p.milky_way()
	p.ecliptic(label = "Eclíptica")
	
	# Ajuste del borde exterior (grosor, color, transparencia)
	for spine in p.ax.spines.values():
		spine.set_edgecolor("white")
		spine.set_linewidth(3)
		spine.set_alpha(1.0)

        
def plotStars(p, magLimit = limit_mag_star):
	# DEFINIMOS CARACTERISTICAS DEL DIBUJADO Y ETIQUETDO DE LAS ESTRELLAS	
	p.stars(
		#catalog = getCatalog(),
		where=[_.magnitude < magLimit],
		where_labels =[_.magnitude < limit_mag_star_label],
		bayer_labels=True,
		flamsteed_labels=True,
		size_fn = getStarSizes(),
	    #size_fn=_sizer,
    	alpha_fn=alpha,
		#color_fn=my_color_definition,#No me gusta el resultado
		style={
			"label": {
				"font_size": getFontSizes()["stars"],
			},
		}
	)


def definir_mapa(ra_min, ra_max, dec_min, dec_max):
	# DEFINIMOS LAS DIMENSIONES Y COORDENADAS DE LA CARTA
	return  MapPlot(
		projection=getProjection(dec_max, ra_min, ra_max),
		ra_min=ra_min, # limit the map to a specific area
		ra_max=ra_max,
		dec_min=dec_min,
		dec_max=dec_max,
		style=style,
		resolution=6500,
		hide_colliding=True,
		#scale=1,	#si queremos que todo sea el doble de grande poner 2
		autoscale=True,  # automatically adjust the scale based on the resolution
	)