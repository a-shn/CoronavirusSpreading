import dict_data_pool as data
import math_tools
import pics_creator

smoothed_dict = math_tools.get_smoothed_with_mean_of_days(data.get_infected_per_day(), 5)
extremas_dict = dict()

for country in smoothed_dict.keys():
	smoothed_list = sorted(smoothed_dict[country].items())
	extremas_dict[country] = []
	for i in range(len(smoothed_list) - 2):
		if smoothed_list[i][1] < smoothed_list[i + 1][1] and smoothed_list[i + 1][1] > smoothed_list[i + 2][1]:
			extremas_dict[country].append(smoothed_list[i + 1][0])

pics_creator.get_pics_with_extremas(smoothed_dict, extremas_dict, 'extremas')
