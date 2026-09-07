from skyfield.api import Star, load
from skyfield.data import hipparcos

with load.open(hipparcos.URL) as f:
    df = hipparcos.load_dataframe(f)
    

def extractor():
	code = input("Introducir Código HIP: E(x)it ")
	
	#if code == "x":
	#	return False
	
	try:
		star = Star.from_dataframe(df.loc[int(code)])
		print(f'Coordenadas encontrandas: ra = {star.ra.hours} // dec = {star.dec.degrees}')
		#print("RA: ",star.ra.hours)
		#print("DEC: ", star.dec.degrees)
		return(star.ra.hours, star.dec.degrees)
	
	except:
		print("killo no encuento el code")