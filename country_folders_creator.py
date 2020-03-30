import csv
import os
import tools


for c in tools.get_countries_and_provinces_dict().keys():
	os.mkdir('pics/' + c)
