import dict_data_pool as dp


def sir_iteration(y, N, beta, gamma):
	S, I, R = y
	dS_dt = - beta * I * S / N
	dI_dt = beta * I * S / N - gamma * I
	dR_dt = gamma * I
	return dS_dt, dI_dt, dR_dt


def find_mean_beta(dS_dT_arr, S_arr, I_arr, N):
	betas = []
	beta_sum = 0
	for i in range(len(dS_dT_arr)):
		try:
			beta = dS_dT_arr[i] * N / (I_arr[i] * S_arr[i])
			betas.append(beta)
		except ZeroDivisionError:
			betas.append(None)
			continue
	for beta in betas:
		if beta is not None and beta != 0:
			beta_sum += beta
	return beta_sum / len(betas)


def find_mean_gamma(dR_dT_arr, I_arr):
	gammas = []
	gamma_sum = 0
	for i in range(len(dR_dT_arr)):
		try:
			gamma = dR_dT_arr[i] / I_arr[i]
			gammas.append(gamma)
		except ZeroDivisionError:
			gammas.append(None)
			continue
	for gamma in gammas:
		if gamma is not None and gamma != 0:
			gamma_sum += gamma
	return gamma_sum / len(gammas)


def sir_model(N, country, predate, days):
	dS_dT_arr = list(dp.get_infected_per_day()[country].values())
	dR_dT_arr = list(dp.get_countries_removed_per_day()[country].values())
	S0 = dp.get_susceptible_dict(N, country)[predate]
	I0 = dp.get_current_infected()[country][predate]
	R0 = dp.get_countries_removed()[country][predate]
	S_arr = list(dp.get_susceptible_dict(N, country).values())
	I_arr = list(dp.get_current_infected()[country].values())
	dates = list(dp.get_infected_per_day()[country].keys())
	edge = dates.index(predate)
	# beta = find_mean_beta(dS_dT_arr[:edge], S_arr[:edge], I_arr[:edge], N)
	# gamma = find_mean_gamma(dR_dT_arr[:edge], I_arr[:edge])
	beta = find_mean_beta(dS_dT_arr, S_arr, I_arr, N)
	gamma = find_mean_gamma(dR_dT_arr, I_arr)
	print('S0 = ' + str(S0) + ', I0 = ' + str(I0) + ', R0 = ' + str(R0) + ', beta = ' + str(beta) + ', gamma = ' + str(gamma))
	y = [S0, I0, R0]
	y_arr = [y.copy()]
	for i in range(days):
		dy_dt = sir_iteration(y, N, beta, gamma)
		y[0] += dy_dt[0]
		y[1] += dy_dt[1]
		y[2] += dy_dt[2]
		y_arr.append(y.copy())
	return y_arr


