import load_ext_files as load


carbono = load.leer_cabono()
dobles = load.leer_dobles()
abells_pn = load.leer_abells()
exoticos = load.leer_exoticos()
galaxias = load.leer_galaxias()


#objetos de nuestra coleccion

def plotCarbon(p):	
	#Carbono
	for i, row in carbono.iterrows():
		p.marker(
			ra = row["AR"] * 15,
			dec = row["DEC"],
			style={
				"marker": {
					"size": 6,
					"symbol": 'circle',
					"fill": "full" ,
					"color": "#ff6464",
					"edge_color": "#ff6464",
					"alpha": 0.8,
					"zorder": 2000,
				},
				"label": {
					"font_size": 8,
					"font_color": "darkgray",
					"font_alpha": 1,
					"offset_x": "auto",
					"offset_y": "auto",
				},
			},
			label=row["REF"],
		)

def plotDobles(p):
	#Dobles
	for i, row in dobles.iterrows():
		color = '#ff50c5' if row["CLASS"] == 'Doble Colorida' else '#e6ae53'
		p.marker(
			ra=row["AR"] * 15,
			dec=row["DEC"],
			style={
				"marker": {
					"size": 10,
					"symbol": 'circle_line',
					"color": color,
					"edge_color": color,
					"alpha": 0.8,
					"zorder": 2000,
				},
				"label": {
					"font_size": 8,
					"font_color": "darkgray",
					"font_alpha": 1,
					"offset_x": "auto",
					"offset_y": "auto",
				},
			},
			label=row["Label"],
		)

def plotAbells(p):
	#Abell PN
	for i, row in abells_pn.iterrows():
		p.marker(
			ra=row["AR"] * 15,
			dec=row["DEC"],
			style={
				"marker": {
					"size": 15,
					"symbol": 'circle_crosshair',
					"edge_color": '#69b655',
					"alpha": 0.8,
					"zorder": 1000,
					"fill": 'none',
				},
				"label": {
					"font_size": 8,
					"font_color": "darkgray",
					"font_alpha": 1,
					"offset_x": "auto",
					"offset_y": "auto",
				},
			},
			label=row["REF"],
		)

def plotExotic(p):
	#Exoticos
	for i, row in exoticos.iterrows():
		color = None
		symbol = 'circle'
		if row["CLASS"] == 'Quasar':
			edge_color = 'white'
			size = 8
			edge_width = 1
			line_style = 'solid' 
		elif row["CLASS"] == 'GlxGroup':
			edge_color = '#ff54e2'
			size = 17
			edge_width = 0.4
			line_style = 'dotted'
		else:
			edge_color = 'orange'
			size = 8
			edge_width = 1
			line_style = 'solid'
		p.marker(
			ra=row["AR"] * 15,
			dec=row["DEC"],
			style={
				"marker": {
					"size": size,
					"symbol": symbol,
					"edge_color": edge_color,
					"line_style": line_style,
					"color": None,
					"alpha": 0.5,
					"zorder": 1000,
					"fill": 'none',
				},
				"label": {
					"font_size": 8,
					"font_color": "darkgray",
					"font_alpha": 1,
					"offset_x": "auto",
					"offset_y": "auto",
				},
			},
			label=row["REF"],
		)


def plotMyGalaxies(p):	
	# Galaxias peculiares
	for i, row in galaxias.iterrows():
		p.marker(
			ra = row["AR"] * 15,
			dec = row["DEC"],
			style={
				"marker": {
					"size": 12,
					"symbol": 'ellipse',
					"fill": "none" ,
					"edge_color": "#e6ae53",
					"alpha": 0.8,
					"zorder": 2000,
				},
				"label": {
					"font_size": 8,
					"font_color": "darkgray",
					"font_alpha": 1,
					"offset_x": "auto",
					"offset_y": "auto",
				},
			},
			label=row["REF"],
		)
