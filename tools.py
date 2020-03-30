import csv


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
						countries_confirmed[w['Country/Region']][w['ObservationDate']] = countries_confirmed[w['Country/Region']][w['ObservationDate']] + int(w['Confirmed'].split('.')[0])
					else:
						countries_confirmed[w['Country/Region']][w['ObservationDate']] = int(w['Confirmed'].split('.')[0])
				else:
					countries_confirmed[w['Country/Region']] = dict()
					countries_confirmed[w['Country/Region']][w['ObservationDate']] = int(w['Confirmed'].split('.')[0])
	return countries_confirmed
