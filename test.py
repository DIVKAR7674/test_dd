import numpy as np
from matplotlib import cm
import open3d as o3d
VIRIDIS = np.array(cm.get_cmap('plasma').colors)
VID_RANGE = np.linspace(0.0, 255.0, VIRIDIS.shape[0])
LABEL_COLORS = np.array([
    (255, 255, 255), # None
    (70, 70, 70),    # Building
    (100, 40, 40),   # Fences
    (55, 90, 80),    # Other
    (220, 20, 60),   # Pedestrian
    (153, 153, 153), # Pole
    (157, 234, 50),  # RoadLines
    (128, 64, 128),  # Road
    (244, 35, 232),  # Sidewalk
    (107, 142, 35),  # Vegetation
    (0, 0, 142),     # Vehicle
    (102, 102, 156), # Wall
    (220, 220, 0),   # TrafficSign
    (70, 130, 180),  # Sky
    (81, 0, 81),     # Ground
    (150, 100, 100), # Bridge
    (230, 150, 140), # RailTrack
    (180, 165, 180), # GuardRail
    (250, 170, 30),  # TrafficLight
    (110, 190, 160), # Static
    (170, 120, 50),  # Dynamic
    (45, 60, 150),   # Water
    (145, 170, 100), # Terrain
])  # normalize each channel [0-1] since is what Open3D uses

#print(VIRIDIS,VIRIDIS.shape)
#print(VID_RANGE)

def visu_pcd(points_l,hud_w=640,hud_h=480,lidar_r=50):
    #lidar_data=np.array(points_l[:,:2])
    lidar_data=points_l[:,:2]
    lidar_data*=min(hud_h,hud_w)/(2.0*lidar_r)
    lidar_data+=(0.5*hud_h,0.5*hud_w)
    lidar_data=np.fabs(lidar_data)
    lidar_data=lidar_data.astype(np.int32)
    lidar_data=np.reshape(lidar_data,(-1,2))
    lidar_img_size=(hud_h,hud_w,3)
    lidar_img=np.zeros((lidar_img_size),dtype=np.uint8)
    lidar_img[tuple(lidar_data.T)]=(255,0,255)
    return lidar_img

