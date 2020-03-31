import tools
import matplotlib.pyplot as plt
from collections import OrderedDict

def get_smoothed(list, index, n):
    a = list[index * n]
    b = list[index * (n + 1)]
    for i in range(n):
        a += list[index * n - i][1]
    for i in range(n):
        b += list[index * n - i - 1][1]
    return a - b

current_infected = tools.get_current_infected()
confirmed = tools.get_countries_confirmed_date_dict()
countries = confirmed.keys()
dynamic = dict()
for country in countries:
    N = 6  # DAYS FOR MEAN
    current = sorted(confirmed[country].items())
    current_infected_country = sorted(current_infected[country].items())
    size = int(len(current) / N)
    size -= 1
    while size > 2:
        if current_infected_country[size * N - N][1] > 0:
            if country in dynamic.keys():
                dynamic[country][current[size * N][0]] = get_smoothed(current, size, N) / current_infected_country[size * N - N][1]
            else:
                dynamic[country] = dict()
                dynamic[country][current[size * N][0]] = get_smoothed(current, size, N) / current_infected_country[size * N - N][1]
        else:
            if country in dynamic.keys():
                dynamic[country][current[size * N][0]] = -1
            else:
                dynamic[country] = dict()
                dynamic[country][current[size * N][0]] = -1
        print(get_smoothed(current, size, N), current_infected_country[size * N - 2 * N][1], dynamic[country][current[size * N][0]])
        size -= 1
    dynamic[country] = OrderedDict(dynamic[country])
    plt.rc('xtick',labelsize=3)
    fig, ax = plt.subplots()
    ax.set_title(country)
    ax.set_xlabel("Date")
    ax.set_ylabel("Counted in progress")
    ax.plot(list(dynamic[country].keys().__reversed__()), list(dynamic[country].values().__reversed__()))
    ax.set(xlabel='date', ylabel='confirmed')
    for tick in ax.get_xticklabels():
        tick.set_rotation(45)
    ax.grid()
    fig.savefig('r_pics/' + country + '.png', dpi=800)
    plt.close()
    print(country + ' - completed')