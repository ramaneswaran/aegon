import math
import urllib.request
import json

KEY = 'ade775fb2c66ac0b75d18477ce90c5a8'

url = 'http://api.ipstack.com/60.243.113.124?access_key='+KEY



def get_gps(xmid, ymid, tempGPS):

#Returns the gps value

    #GPS of UAV
    with urllib.request.urlopen(url) as response:
        resp = response.read().decode('utf-8')  
        obj = json.loads(resp)
        lat = float(obj['latitude'])
        lon = float(obj['longitude'])

    #Center of image / The images are 1280*720
    x_center = 640
    y_center = 360

    #Calculating distance from center
    x = float(x_center-xmid)
    y = float(y_center-ymid)

    #Field of view for the camera
    fov_ver = 72.2
    fov_hor = 94.4

    #Average distance for demo
    h = 2.0

    a = (2*h)/math.cos(fov_hor/2)
    b = (2*h)/math.cos(fov_ver/2)

    scale_x = a/1280.0
    scale_y = b/720.0

    offset_target = [(scale_x*x)/110000.0,( scale_y*y)/110000.0]

    GPS = {'latitude': round((lat + offset_target[0]),5), 
            'longitude': round((lon + offset_target[1]),5)}
    
    if(tempGPS['latitude'] != GPS['latitude'] and tempGPS['latitude'] != GPS['latitude']):
        #Write to file
        
        with open('utils/data.txt', 'a') as outfile:
            json.dump(GPS, outfile)
    return GPS
