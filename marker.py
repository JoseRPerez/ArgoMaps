

def getMarker(tipo: str) -> tuple[str, str]:
	#colores para (PN, N, G, GCl, OC, Car, Doble, Doble colorida, EX)
	if tipo == "PN":
		return '#69b655', 'circle_crosshair'
	elif tipo == "N":
		return '#69b655', 'circle'
	elif tipo == "G":
		return '#e6ae53', 'ellipse'
	elif tipo == "GCl":
		return '#e6ae53', 'circle_plus'
	elif tipo == "OC":
		return '#e6ae53', 'circle_dotted_edge'
	elif tipo == "Car":
		return "#ff6464", 'circle'
	elif tipo == "Doble":
		return '#e6ae53', 'circle_line'
	elif tipo == "Doble colorida":
		return '#ff50c5', 'circle_line'
	elif tipo == 'EX':
		return 'white', 'plus'


def plotMarker(p, tipo, coords, label):
	if tipo != None:
		ar,dec = coords
		color,symbol = getMarker(tipo)
		p.marker(
				ra=ar,
				dec=dec,
				style={
					"marker": {
						"size": 6,
						"fill": 'none',
						"symbol": symbol,
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
				label=label,
			)
			
		#circulo tipo telrad
		p.marker(
				ra=ar,
				dec=dec,
				style={
					"marker": {
						"size": 150,
						"symbol": 'circle',
						"fill": 'none',
						"edge_color": 'red',
						"alpha": 0.5,
					},
				},
				label=label,
			)
		
		
		