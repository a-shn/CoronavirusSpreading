import tools
import matplotlib.pyplot as plt


countries_and_confirmed = tools.get_countries_confirmed_date_dict()
for country in countries_and_confirmed.keys():
	plt.rc('xtick', labelsize=1)
	fig, ax = plt.subplots()
	ax.plot(list(countries_and_confirmed[country].keys()), list(countries_and_confirmed[country].values()))
	ax.set(xlabel='date', ylabel='confirmed')
	ax.grid()
	fig.savefig('pics/' + country + '.png', dpi=500)
	plt.close()
	print(country + ' - completed')
