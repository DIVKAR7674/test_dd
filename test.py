import matplotlib.pyplot as plt
import numpy as np
from test_2 import *
#import pcl
from show import *
# from tool import *
import open3d as o3d

#points=load_pc_from_bin('bin/83.bin')

#full_cloud2.pcd
#bunny.pcd
url='C:/Users/DIWAKAR/Downloads/lidar_projection-master/lidar_projection-master/full_cloud2.pcd'
pcd = o3d.io.read_point_cloud(url)
out_arr = np.asarray(pcd.points)

	#print(out_arr.shape)
	#i=np.ones(127088)
	#i*=255
	#print(i,i.shape)
	#out_f=np.c_[out_arr,i]
print("output array from input list : ", out_arr,out_arr.shape)
lidar = out_arr

HRES = 0.35         # horizontal resolution (assuming 20Hz setting)
VRES = 0.4          # vertical res
VFOV = (-24.9, 2.0) # Field of view (-ve, +ve) along vertical axis
Y_FUDGE = 5         # y fudge factor for velodyne HDL 64E
viz_mayavi(lidar, vals="height")

#lidar_to_2d_front_view(lidar, v_res=VRES, h_res=HRES, v_fov=VFOV, val="depth",saveto="pic/lidar_depth1.png", y_fudge=Y_FUDGE)

#lidar_to_2d_front_view(lidar, v_res=VRES, h_res=HRES, v_fov=VFOV, val="height",saveto="pic/lidar_height1.png", y_fudge=Y_FUDGE)

#lidar_to_2d_front_view(lidar, v_res=VRES, h_res=HRES, v_fov=VFOV,val="reflectance", saveto="pic/lidar_reflectance1.png",y_fudge=Y_FUDGE)

#im=birds_eye_point_cloud(lidar, side_range=(-10, 10), fwd_range=(-10, 10), res=0.1, saveto="C:/Users/DIWAKAR/Downloads/lidar_projection-master/lidar_projection-master/pic/lidar_pil_02.png")

# im = point_cloud_to_panorama(lidar,v_res=0.42, h_res=0.35,v_fov=(-24.9, 2.0),y_fudge=3,d_range=(0,100))
# plt.imshow(im,cmap='spectral')
# plt.savefig("pic/spec1.png")
# plt.show()

# plt.imshow(im, cmap="Spectral", vmin=0, vmax=255)
# plt.show()

