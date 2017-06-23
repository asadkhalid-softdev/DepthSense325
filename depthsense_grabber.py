import numpy as np
import cv2
import DepthSense as dsc
import matplotlib.pyplot as plt

#============================= SIMPLE DATA CAPTURE AND DISPLAY =============================#
def img_cap():
    	while(1):
        	color,gray=get_colorMap()
		depth_mat,depth_gray,depth_col=get_depthMap()
		conf_gray,conf_col=get_confidenceMap()
		sync_img,sync_gray=get_syncMap()
		dep_conf=np.concatenate((conf_col,depth_col),axis=1)
		col_sync=np.concatenate((color,sync_img),axis=1)
		#================== IMAGE DISPLAY
        	cv2.imshow('view1', dep_conf)
        	cv2.imshow('view2', col_sync)
		if cv2.waitKey(1) & 0xFF == ord('q'):
            		break
        cv2.destroyAllWindows()

#============================= GET DEPTH FRAME AND DEPTH MATRIX =============================#
def get_depthMap():
	depth_mat = dsc.getDepthMap()
	depth_mat[depth_mat>30000]=0
	depth_gray = depth_mat.copy()
        np.clip(depth_gray, 0, 2**10 - 1, depth_gray)
        depth_gray >>=2
        depth_gray = depth_gray.astype(np.uint8)
	cmap = plt.get_cmap('jet_r')
	depth_col = cmap(depth_gray)
	depth_col = np.delete(depth_col, 3, 2)
	depth_col = cv2.resize(depth_col, (640, 480))
	depth_gray = cv2.resize(depth_gray, (640, 480))
        return depth_mat,depth_gray,depth_col

#============================= GET CONFIDENCE FRAME =============================#
def get_confidenceMap():
	conf_mat = dsc.getConfidenceMap()
	conf_gray = conf_mat.copy()
        np.clip(conf_gray, 0, 2**10 - 1, conf_gray)
        conf_gray >>=2
        conf_gray = conf_gray.astype(np.uint8)
	cmap = plt.get_cmap('jet_r')
	conf_col = cmap(conf_gray)
	conf_col = np.delete(conf_col, 3, 2)
	conf_col = cv2.resize(conf_col, (640, 480))
	conf_gray = cv2.resize(conf_gray, (640, 480))
        return conf_gray,conf_col

#============================= GET COLOR FRAME =============================#
def get_colorMap():
	cim = dsc.getColourMap()
	cim_gray = cv2.cvtColor(cim,cv2.COLOR_BGR2GRAY)
	return cim,cim_gray

#============================= GET SYNC FRAME =============================#
def get_syncMap():
	sync = dsc.getSyncMap()
	sync_gray = cv2.cvtColor(sync,cv2.COLOR_BGR2GRAY)
	sync = cv2.resize(sync, (640, 480))
	sync_gray = cv2.resize(sync_gray, (640, 480))
	return sync,sync_gray

#============================= GET VERTICES MATRIX =============================#
def get_vertices():
	vertices_mat = dsc.getVertices()
	return vertices_mat


#============================= MAIN =============================#
dsc.start()
img_cap()
dsc.stop()

