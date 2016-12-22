import scipy.misc
import json
import glob
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def showBbox(image_root_dir,anno_file):
	with open(anno_file,'r') as fi:
		annos = json.load(fi)
		img_files = glob.glob(os.path.join(image_root_dir,'*.jpg'))
		assert(len(annos)==len(img_files))
  		for anno in annos:
  			if 'shark' in anno_file or 'yft' in anno_file:
  				img = scipy.misc.imread(anno['filename'])
  			else:
  				img = scipy.misc.imread(os.path.join(image_root_dir,anno['filename']))
  			fig,ax = plt.subplots(1)
  			ax.imshow(img)
  			
  			for rec in anno['annotations']:
  				rec_patch = patches.Rectangle((rec['x'],rec['y']),rec['width'],rec['height'],linewidth=1,\
  					edgecolor='r',facecolor='none')
  				ax.add_patch(rec_patch)
  			plt.show()







showBbox('../data/train/YFT/','../data/annotation/bbox/yft_labels.json')