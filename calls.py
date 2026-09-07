import math
from starplot import Star, DSO
from starplot import StereoNorth, Miller, Mercator

############### CALLABLES ###############
		
def isTrueSizeHII(dso: DSO) -> bool:
	if dso.size <= 0.01 or dso.size != dso.size:
		return False
	else:
		return True


def isTrueSize(dso: DSO) -> bool:
	if dso.size <= 0.01 or dso.size != dso.size:
		return False
	else:
		return True


def isTrueSizeSuperNova(dso: DSO) -> bool:
	if dso.size <= 0.01:
		return False
	else:
		return True


def isTrueSizeOtherNebs(dso: DSO) -> bool:
	if dso.size <= 0.01:
		return False
	else:
		return True

def messierSize(dso: DSO) -> bool:
	if dso.size != dso.size or dso.size < 0.01:
		return False
	else:
		return True 


def getProjection(decmax, ra_min, ra_max):
	#determinacion del tipo de proyeccion
	#obviamos declinaciones bajas
	center = (ra_min + ra_max) / 2.	# orientación antigua del mapa
	# center = 0 valor por defecto no me gusta	
	if decmax >= 70:		
		return StereoNorth(center_ra = center % 360)
	else:
		return Miller(center_ra = center % 360)



def size_log_mio_1(star: Star) -> str:
	mag = star.magnitude
	a = 9000
	b = 0.65
	return a*math.exp(-b*(mag+1.5))


def getStarSizes():
	return size_log_mio_1


def alpha(s):
	#return 0.98 - 0.0106 * s.magnitude - 0.00573 * s.magnitude * s.magnitude
	if s.magnitude > 11.5:
		return 0.15
	if s.magnitude > 8:
		return 2.6145 - 0.2143 * s.magnitude
	else:
		return 0.9



'''
#No me gusta el resultado
def my_color_definition(s):
	if s.bv > 2:
		return color_by_bv
	else:
		return '#808080'
        
'''

'''
def getMyLabel(dso: DSO) -> str:
	if dso.common_names:
		if dso.m:
			return f"M{dso.m} {dso.common_names[0]}"
		elif dso.ngc:
			return f"M{dso.ngc} {dso.common_names[0]}"
		elif dso.ic:
			return f"M{dso.ic} {dso.common_names[0]}"
	if dso.m:
		return f"M{dso.m}"
	if dso.ngc:
		return dso.ngc
	if dso.ic:
		return f"IC{dso.ic}"
	
	return dso.name
'''

def getMyLabel(dso: DSO) -> str:
    # 1. Determinar el código del catálogo principal
    if dso.m:
        cat_id = f"M{dso.m}"
    elif dso.ngc:
        cat_id = f"{dso.ngc}"
    elif dso.ic:
        cat_id = f"IC{dso.ic}"
    else:
        cat_id = dso.name

    # 2. Si tiene nombre común, añadirlo al final
    if dso.common_names:
        return f"{cat_id} {dso.common_names[0]}"

    return cat_id
	


def getFontSizes():
	return {"stars": 10, "bayer": 10, "flamsteed": 10}

def getCatalog():
	#return "hipparcos"
	return "big-sky-mag11"  #definitivamente dejaremos este que es mas completo

