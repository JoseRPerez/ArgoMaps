from calls import getMyLabel
from definitions import size_hercules_cluster
from starplot import _, DsoType



'''
def plotBigGC(p):
	p.globular_clusters(
		where=[ ((_.size.isnull()) | (_.size < size_hercules_cluster)), ((_.magnitude.isnull()) | (_.magnitude < 11.3))],
		label_fn=getMyLabel,
		true_size=False, 
	)


def plotSmallGC(p):
	p.style.dso_globular_cluster.label.offset_x = 7
	p.style.dso_globular_cluster.label.offset_y = 7

	p.globular_clusters(
		where=[_.size >= size_hercules_cluster, _.magnitude < 11.3],
		label_fn=getMyLabel,
		true_size=True, 
	)
'''

def plotClusters(p):
	condition = ((_.size.isnull()) | (_.size < size_hercules_cluster)), ((_.magnitude.isnull()) | (_.magnitude < 11.3))


	p.dsos(
		where=[
			_.type.isin(
				[     
					DsoType.OPEN_CLUSTER.value,
					DsoType.GLOBULAR_CLUSTER.value,
				]),
		  	(_.size.isnull()) | (_.size < size_hercules_cluster),
			(_.magnitude.isnull()) | (_.magnitude < 11.3),
		],
		where_true_size=[_.size >= size_hercules_cluster],
		label_fn = getMyLabel,
	)
