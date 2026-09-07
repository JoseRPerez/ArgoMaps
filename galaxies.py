from calls import getMyLabel
from definitions import size_sculptor_glx, size_triangulo_glx
from starplot import _, DsoType 


def plot_Glx(p):
	conditions = _.magnitude < 11.7
	p.style.dso_galaxy.marker.zorder = 0
	p.style.dso_galaxy.marker.edge_color = "#e6ae53"

	p.dsos(
		where=[
			_.type.isin(
				[
					DsoType.GALAXY.value,
			]),
			conditions,
		],
		where_true_size=[_.size >= size_sculptor_glx],
		label_fn=getMyLabel,
	)
	

	# Grupos galaxias
	p.style.dso_galaxy.marker.edge_color = "hotpink"
	p.style.dso_galaxy.marker.size = 12
	p.style.dso_galaxy.marker.fill = "none"
	
	p.dsos(
		where=[
			_.type.isin(
				[
					DsoType.GALAXY_TRIPLET.value,
					DsoType.GALAXY_PAIR.value,
					DsoType.GROUP_OF_GALAXIES.value		
				]),
		  	(_.magnitude < 11.7) | (_.magnitude.isnull()),
		],
		where_true_size=[_.size >= size_sculptor_glx],
		label_fn=getMyLabel,
)
		

'''
def plot_SmallGlx(p):
	p.galaxies(
		where=[_.size < size_sculptor_glx, _.magnitude < 11.7],
		label_fn=getMyLabel,
		true_size=False,
	)


def plot_BigGlx(p):
	p.style.dso_galaxy.label.offset_x = 7
	p.style.dso_galaxy.label.offset_y = 7
	
	p.galaxies(
		#where=[(_.size > size_sculptor_glx) & (_.size < size_triangulo_glx), _.magnitude < 12],
		where=[_.size >= size_sculptor_glx, _.magnitude < 12],
		label_fn=getMyLabel,
		true_size=True,
	)

'''

'''
		#NO SIRVE SE PUEDE BORRAR
		#Dibujamos las galaxias mas grandes (nubes de magallanes y andromeda)
		style.dso_galaxy.marker.fill = 'none'
		glx_color = style.dso_galaxy.marker.color
		style.dso_galaxy.marker.color = None
		style.dso_galaxy.marker.edge_color = glx_color
		p.galaxies(
			where=[_.size > size_triangulo_glx],
			label_fn=getLabel(),
			true_size=True,
		)
	'''