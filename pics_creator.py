import os
import matplotlib.pyplot as plt


def get_pics(dict_with_date_dicts, folder):
	if not os.path.exists('./' + folder):
		os.mkdir(folder)
	for country in dict_with_date_dicts.keys():
		plt.rc('xtick', labelsize=3)
		fig, ax = plt.subplots()
		ax.set_title(country)
		ax.set_xlabel("Date")
		ax.set_ylabel("Counted in progress")
		ax.plot(list(dict_with_date_dicts[country].keys()), list(dict_with_date_dicts[country].values()))
		ax.set(xlabel='date', ylabel='confirmed')
		for tick in ax.get_xticklabels():
			tick.set_rotation(45)
		ax.grid()
		fig.savefig('./' + folder + '/' + country + '.png', dpi=800)
		plt.close()
		print(country + ' - completed')


def get_pics_with_extremas(dict_with_date_dicts, extremas, folder):
	if not os.path.exists('./' + folder):
		os.mkdir(folder)
	for country in dict_with_date_dicts.keys():
		plt.rc('xtick', labelsize=3)
		fig, ax = plt.subplots()
		ax.set_title(country)
		ax.set_xlabel("Date")
		ax.set_ylabel("Counted in progress")
		ax.plot(list(dict_with_date_dicts[country].keys()), list(dict_with_date_dicts[country].values()))
		ax.set(xlabel='date', ylabel='confirmed')
		for extrema in extremas[country]:
			ax.axvline(x=extrema, linewidth=1, color='r')
		for tick in ax.get_xticklabels():
			tick.set_rotation(45)
		ax.grid()
		fig.savefig('./' + folder + '/' + country + '.png', dpi=800)
		plt.close()
		print(country + ' - completed')