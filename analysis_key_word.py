import os 
from shutil import copyfile
from time import time
INPUT_DIR = "gs_result"
OUTPUT_DIR = "relevant"
filenames = os.listdir(INPUT_DIR)

filters = [
	"behavioral om",
	"behavioral operations",
	"behavior in operations",
	"empirical operations",
	"empirical om",
	"healthcare operations",
	"humanitarian operations",
	"inventory control",
	"inventory model",
	"inventory theory",
	"operations management",
	"revenue management",
	"service operations",
	"supply chain", 
	"supply risk management",
	"sustainable om",
	"sustainable operations",
	"production management",
	["finance", "om", "interface"],
	["marketing", "om", "interface"],
	["finance", "operations", "interface"],
	["marketing", "operations", "interface"],
	["marketing", "manufacturing", "interface"],
	["finance", "manufacturing", "interface"]
]

filename_list = []

def contains_all(filters, sentence):
	for filt in filters:
		if filt not in sentence:
			return False

	return True


for filename in filenames:
	matched = False
	label_str = ""
	with open(os.path.join(INPUT_DIR, filename), 'r') as fp:
		lines = fp.readlines()
		try:
			label_str = lines[3].lower()
		except:
			continue
		
		for filt in filters:
			if type(filt) is str and filt in label_str:
				matched = True
				print("match at condition 1")
				break
				
			elif type(filt) is list and contains_all(filt, label_str):
				matched = True
				print("match at condition 2")
				break

	if matched is True:
		print (label_str)
		copyfile(os.path.join(INPUT_DIR, filename),
				os.path.join(OUTPUT_DIR, filename))









