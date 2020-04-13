import csv
from collections import OrderedDict


def get_countries_set():
	countries = set()
	with open('data/covid_19_data.csv', newline='') as csvfile:
		timereader = csv.DictReader(csvfile)
		for w in timereader:
			if w['Country/Region'] != '':
				countries.add(w['Country/Region'])
	return countries


def get_countries_and_provinces_dict():
	country_and_province = dict()
	with open('data/covid_19_data.csv', newline='') as csvfile:
		timereader = csv.DictReader(csvfile)
		for w in timereader:
			if w['Country/Region'] != '' and w['Province/State'] != '':
				if w['Country/Region'] in country_and_province.keys():
					country_and_province[w['Country/Region']].add(w['Province/State'])
				else:
					country_and_province[w['Country/Region']] = set()
					country_and_province[w['Country/Region']].add(w['Province/State'])
	return country_and_province


def get_provinces_confirmed_list():
	province_and_confirmed = dict()
	with open('data/covid_19_data.csv', newline='') as csvfile:
		timereader = csv.DictReader(csvfile)
		for w in timereader:
			if w['Country/Region'] != '' and w['Province/State'] != '':
				if w['Province/State'] in province_and_confirmed.keys():
					province_and_confirmed[w['Province/State']].append(int(w['Confirmed'].split('.')[0]))
				else:
					province_and_confirmed[w['Province/State']] = []
					province_and_confirmed[w['Province/State']].append(int(w['Confirmed'].split('.')[0]))
	return province_and_confirmed


def get_countries_confirmed_date_dict():
	countries_confirmed = dict()
	with open('data/covid_19_data.csv', newline='') as csvfile:
		timereader = csv.DictReader(csvfile)
		for w in timereader:
			if w['Country/Region'] != '':
				if w['Country/Region'] in countries_confirmed.keys():
					if w['ObservationDate'] in countries_confirmed[w['Country/Region']].keys():
						countries_confirmed[w['Country/Region']][w['ObservationDate']] = \
							countries_confirmed[w['Country/Region']][w['ObservationDate']] + int(
								w['Confirmed'].split('.')[0])
					else:
						countries_confirmed[w['Country/Region']][w['ObservationDate']] = int(
							w['Confirmed'].split('.')[0])
				else:
					countries_confirmed[w['Country/Region']] = dict()
					countries_confirmed[w['Country/Region']][w['ObservationDate']] = int(w['Confirmed'].split('.')[0])
	return countries_confirmed


def get_current_infected():
	current_infected = dict()
	with open('data/covid_19_data.csv', newline='') as csvfile:
		timereader = csv.DictReader(csvfile)
		for w in timereader:
			if w['Country/Region'] != '':
				if w['Country/Region'] in current_infected.keys():
					if w['ObservationDate'] in current_infected[w['Country/Region']].keys():
						current_infected[w['Country/Region']][w['ObservationDate']] = \
							current_infected[w['Country/Region']][w['ObservationDate']] + int(
								w['Confirmed'].split('.')[0]) - (
									int(w['Recovered'].split('.')[0]) + int(w['Deaths'].split('.')[0]))
					else:
						current_infected[w['Country/Region']][w['ObservationDate']] = int(
							w['Confirmed'].split('.')[0]) - (int(w['Recovered'].split('.')[0]) + int(
							w['Deaths'].split('.')[0]))
				else:
					current_infected[w['Country/Region']] = dict()
					current_infected[w['Country/Region']][w['ObservationDate']] = int(w['Confirmed'].split('.')[0]) - (
							int(w['Recovered'].split('.')[0]) + int(w['Deaths'].split('.')[0]))
	return current_infected


def get_countries_removed():
	countries_removed = dict()
	with open('data/covid_19_data.csv', newline='') as csvfile:
		timereader = csv.DictReader(csvfile)
		for w in timereader:
			if w['Country/Region'] != '':
				if w['Country/Region'] in countries_removed.keys():
					if w['ObservationDate'] in countries_removed[w['Country/Region']].keys():
						countries_removed[w['Country/Region']][w['ObservationDate']] = \
							countries_removed[w['Country/Region']][w['ObservationDate']] + int(w['Recovered'].split('.')[0]) + int(
							w['Deaths'].split('.')[0])
					else:
						countries_removed[w['Country/Region']][w['ObservationDate']] = int(w['Recovered'].split('.')[0]) + int(
							w['Deaths'].split('.')[0])
				else:
					countries_removed[w['Country/Region']] = dict()
					countries_removed[w['Country/Region']][w['ObservationDate']] = int(w['Recovered'].split('.')[0]) + int(
							w['Deaths'].split('.')[0])
	return countries_removed


def get_countries_removed_per_day():
	countries_and_removed = get_countries_removed()
	removed_per_day = dict()
	for country in countries_and_removed.keys():
		try:
			countries_and_removed_list = sorted(countries_and_removed[country].items())
			for i in range(len(countries_and_removed_list) - 1):
				if country in removed_per_day.keys():
					removed_per_day[country][countries_and_removed_list[i][0]] = countries_and_removed_list[i + 1][
						                                                                1] - \
					                                                                countries_and_removed_list[i][1]
					if removed_per_day[country][countries_and_removed_list[i][0]] < 0:
						removed_per_day[country][countries_and_removed_list[i][0]] = 0
				else:
					removed_per_day[country] = dict()
					removed_per_day[country][countries_and_removed_list[i][0]] = countries_and_removed_list[i + 1][
						                                                                1] - \
					                                                                countries_and_removed_list[i][1]
					if removed_per_day[country][countries_and_removed_list[i][0]] < 0:
						removed_per_day[country][countries_and_removed_list[i][0]] = 0

		except KeyError:
			continue
	return removed_per_day


def get_infected_per_day():
	countries_and_confirmed = get_countries_confirmed_date_dict()
	infected_per_day = dict()
	for country in countries_and_confirmed.keys():
		try:
			countries_and_confirmed_list = sorted(countries_and_confirmed[country].items())
			for i in range(len(countries_and_confirmed_list) - 1):
				if country in infected_per_day.keys():
					infected_per_day[country][countries_and_confirmed_list[i][0]] = countries_and_confirmed_list[i + 1][1] - \
					                                                       countries_and_confirmed_list[i][1]
					if infected_per_day[country][countries_and_confirmed_list[i][0]] < 0:
						infected_per_day[country][countries_and_confirmed_list[i][0]] = 0
				else:
					infected_per_day[country] = dict()
					infected_per_day[country][countries_and_confirmed_list[i][0]] = countries_and_confirmed_list[i + 1][1] - \
					                                                       countries_and_confirmed_list[i][1]
					if infected_per_day[country][countries_and_confirmed_list[i][0]] < 0:
						infected_per_day[country][countries_and_confirmed_list[i][0]] = 0

		except KeyError:
			continue
	return infected_per_day


def get_susceptible_dict(N, country):
	confirmed = get_countries_confirmed_date_dict()[country]
	susceptible_dict = dict()
	for date in confirmed:
		susceptible_dict[date] = N - confirmed[date]
	return susceptible_dict


