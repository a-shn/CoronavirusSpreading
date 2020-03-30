import tools
import matplotlib.pyplot as plt


countries_and_provinces = tools.get_countries_and_provinces_dict()
provinces_and_confirmed = tools.get_provinces_confirmed_list()
for country in countries_and_provinces.keys():
	for province in countries_and_provinces[country]:
		tmp = [i for i in range(len(provinces_and_confirmed[province]))]
		fig, ax = plt.subplots()
		ax.plot(tmp, provinces_and_confirmed[province])
		ax.set(xlabel='day', ylabel='confirmed')
		ax.grid()
		fig.savefig('pics/' + country + '/' + province + '.png', dpi=500)
		plt.close()
