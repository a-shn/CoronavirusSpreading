import os
import matplotlib.pyplot as plt
import dict_data_pool as dp
import SIR_model


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
			ax.axvline(x=extrema, linewidth=0.7, color='r', linestyle='--')
		for tick in ax.get_xticklabels():
			tick.set_rotation(45)
		ax.grid()
		fig.savefig('./' + folder + '/' + country + '.png', dpi=800)
		plt.close()
		print(country + ' - completed')


def get_pics_of_confirmed_with_sir_model(country, population, days, predate, folder):
	dict_of_country_with_dates = dp.get_countries_confirmed_date_dict()[country]
	sir_arr = SIR_model.sir_model(population, country, predate, days)
	edge = list(dict_of_country_with_dates.keys()).index(predate)
	if not os.path.exists('./' + folder):
		os.mkdir(folder)

	plt.rc('xtick', labelsize=3)
	fig, ax = plt.subplots()
	ax.set_title('SIR')
	ax.set_xlabel("Day")
	ax.set_ylabel("Counted in progress")
	tmp = [i for i in range(max(edge + len(sir_arr), len(dict_of_country_with_dates)))]
	ax.plot(tmp[:len(dict_of_country_with_dates)], list(dict_of_country_with_dates.values()))
	ax.plot(tmp[edge:edge + len(sir_arr)], [i[1] + i[2] for i in sir_arr], 'ro', markersize=1)
	ax.set(xlabel='day', ylabel='confirmed')
	ax.grid()
	fig.savefig('./' + folder + '/' + country + '_SIR.png', dpi=1200)
	plt.show()
	plt.close()


