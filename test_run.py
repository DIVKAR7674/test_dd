import numpy as np
import cv2,sys
import lmdb
import reloading

# C:\Users\DIWAKAR\Downloads\zzzbzurhpz_1\zzzbzurhpz
path='C:\\Users\\DIWAKAR\\Downloads\\zzzbzurhpz_1\\zzzbzurhpz'
print(path)
txn=lmdb.open(path)
# print("####",txn)

def load_bev(lmdb_txn, idx, channels=range(12)):

    bevs = [cv2.imdecode(np.frombuffer(lmdb_txn.get(f'map_{i}_{idx:05d}'.encode()), dtype=np.uint8), cv2.IMREAD_GRAYSCALE) for i in channels]

    return np.stack(bevs, axis=-1)

def load_img(lmdb_txn,  idx,tag='rgb_2'):
    if 'rgb' in tag:
        mode = cv2.IMREAD_COLOR
    elif 'sem' in tag:
        mode = cv2.IMREAD_GRAYSCALE
    else:
        raise NotImplemented

    return cv2.imdecode(np.frombuffer(lmdb_txn.get('{}_{:05d}'.format(tag, idx).encode()), dtype=np.uint8), mode)

with txn.begin() as t:
    key=list(t.cursor().iternext(values=False))
    #print(key)
    #length = txn.stat()['entries']
    # t.get('len'.encode())
    decoded =t.get('len'.encode()).decode('utf-8')
    print(decoded)
    channels=[0,1,2]
    for i in range(int(decoded)):
        cv2.imshow("front",load_img(t,i))
        cv2.imshow("bev",load_bev(t,i,channels))
        cv2.waitKey(0)
        #load_bev(txn,i)
sys.exit(0)
# img = np.zeros((512,512,1), np.uint8)
# pts = np.array([[0,0],[1,1],[10,5],[20,30],[70,20],[50,10],[320,0],[0,240]], np.int32)
# pts = pts.reshape((-1,1,2))
# cv2.polylines(img,[pts],True,(255,255,255))
# max_distance=50.0 #look-ahead-distance
# width,height=320,240 #gps_img_w,gps_img_h
# scale_factor=4 #pixels_per_m

# image_points=pts
# #np.array(image_points,np.int32)
# gps_img=np.zeros((height,width,1),dtype=np.uint8)
# cv2.polylines(gps_img,[image_points],False,(255,255,255),thickness=2)
# #cv2.circle(gps_img,(width//2,height//2),2*scale_factor,255)
# cv2.imshow("img",gps_img)
# aaa=abs(np.array([-2,3]))
# print("##aa",aaa)
# cv2.waitKey(5000)

# print(160%100)