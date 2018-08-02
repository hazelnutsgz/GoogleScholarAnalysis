# infer the gender of each author according to the 'gs_name.txt'

from datetime import datetime
from gender_detector import GenderDetector
detector = GenderDetector('us')

file_name = open("gs_name.txt", "r");
lines_name = file_name.read().split("\n")

all_name = []; all_gender = [];

for x in lines_name:
    if (len(x) > 0):
        all_name.append(x)
        yy = x.split(" ")
        #       print yy[0],
        author_gender = 'unknown'
        try:
            author_gender = detector.guess(yy[0])
        except:
            pass
        print author_gender
        all_gender.append(author_gender)

