
from functions import *
import numpy as np 
import open3d as o3d
import cv2
from test import *


def Function(points):

	#points = parse_url(url)
	THRESHOLD=0.40
	ground_points, non_ground_points = getGround_World(points, float(THRESHOLD))
	ground_points = changeIntensity(ground_points, GROUND_COLOR)
	non_ground_points = changeIntensity(non_ground_points, NON_GROUND_COLOR)
	points = np.concatenate((ground_points, non_ground_points))
	#print("points",points)
	sensor_url = getSensor_url(points)
	print(sensor_url)
	return sensor_url
  
 
if __name__ == '__main__':
	url='C:/Users/DIWAKAR/Downloads/ground-detection-master/ground-detection-master/milk_cartoon_all_small_clorox.pcd'
	#full_cloud2.pcd
	#bunny.pcd
	pcd = o3d.io.read_point_cloud(url)
	out_arr = np.asarray(pcd.points)
	#print(out_arr.shape)
	#i=np.ones(127088)
	#i*=255
	#print(i,i.shape)
	#out_f=np.c_[out_arr,i]
	print("output array from input list : ", out_arr,out_arr.shape)
	temp=Function(out_arr)
	# temp1=np.array
	img=visu_pcd(temp)
	image = cv2.flip(img, -1)
	cv2.imshow("img",image)
	cv2.waitKey(5000)
    