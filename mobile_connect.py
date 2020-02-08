import cv2
import numpy as np
import requests

while True:
    
    photo="http://10.37.108.234:8080/shot.jpg"
    photo_url=requests.get(photo) #send requests on url
    con=photo_url.content

    bytearray_con =bytearray(con)
    photo_1d=np.array(bytearray_con, dtype=np.uint8) #uint8 is the datatype of your photo and bytearay ko 1D 							      arary mei convert kr liya
    photo=cv2.imdecode(photo_1d, -1) # -1 use iss liye kiya hai ki imdecode function 2 variable maangta hai and 					imdecode 1D convert into 3D
    
    cv2.imshow('rohit',photo)
    if cv2.waitKey(1)==13:
        break
cv2.destroyAllWindows()
