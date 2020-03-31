import csv
import os
import dict_data_pool


for c in dict_data_pool.get_countries_and_provinces_dict().keys():
	os.mkdir('pics/' + c)
