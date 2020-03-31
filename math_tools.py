def get_smoothed_with_mean_of_days(data_dict, days):
	"""
	Smooths data like mean of values for days period
	Args:
		data_dict (dict): {$country: {$date: value}}
		days (int)
	Returns:
		dict
	"""
	smoothed_dict = dict()
	for country in data_dict.keys():
		tmp_list = sorted(data_dict[country].items())
		for i in range(len(data_dict[country]) // days):
			if country in smoothed_dict.keys():
				smoothed_dict[country][tmp_list[i * days][0]] = mean_of_dictlist_for_period(tmp_list, i * days, days)
			else:
				smoothed_dict[country] = dict()
				smoothed_dict[country][tmp_list[i * days][0]] = mean_of_dictlist_for_period(tmp_list, i * days, days)
	return smoothed_dict


def mean_of_dictlist_for_period(dictlist, begin, period):
	sum = 0
	for i in range(period):
		sum += dictlist[begin + i][1]
	return sum / period