import os 
from shutil import copyfile
from time import time
from collections import defaultdict
INPUT_DIR = "gs_result"

keys = ["machine learning", "artificial intelligence", "computer vision","bioinformatics", "data mining","neuroscience"
"robotics", "image processing", "software engineering", "ecology"]

count_dic = defaultdict()

filenames = os.listdir(INPUT_DIR)

for filename in filenames:
	label_str = ""
	with open(os.path.join(INPUT_DIR, filename), 'r') as fp:
		try:
			lines = fp.readlines()
			for key in keys:
					if key in lines[3]:
						if not count_dic.get(key):
							count_dic[key] = 1
						else:
							count_dic[key] += 1	
						print (key, lines[1])
		except:
			continue
		

print (count_dic)
