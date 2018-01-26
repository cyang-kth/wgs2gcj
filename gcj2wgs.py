'''
Author: Can Yang
Date: 2018.1.26
'''
import json
import eviltransform
def read_geojson(filename):
    with open(filename) as f:
        data = json.load(f)
        return data
def wgs2gcj(inputfile,outputfile):
	data = read_geojson(inputfile)
	for feature in data['features']:
	    if feature['geometry']['type']=='LineString':
	        # 2D array
	        #feature = data['features'][100]
	        pts=feature['geometry']['coordinates']
	        for i in range(len(pts)):
	            temp = eviltransform.wgs2gcj(pts[i][1],pts[i][0])
	            pts[i] =[temp[1],temp[0]]
	with open(outputfile, 'w') as outfile:
	    json.dump(data, outfile)
inputfile = "network.geojson"
outputfile = "network_gcj_v2.geojson"
wgs2gcj(inputfile,outputfile)


