import math

def get_gps(xmid, ymid):

#Returns the gps value

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

    scale_x = a/640.0
    scale_y = b/480.0

    offset_target = [(scale_x*x)/110.0,( scale_y*y)/110.0]

    print(offset_target)
    
