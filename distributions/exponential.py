import math, scipy

def pdf(x, theta):
	"""Returns the probability density function of the exponential distribution with mean theta"""
	num = math.exp(-x / theta)
	den = theta
	out = num / den
	return(out)
	
def cdf(x, theta):
	"""Returns the cumulative distribution function of the exponential distribution with mean theta"""
	out = 1 - math.exp(-x/theta)
	return(out)
	
def percentile(p, theta):
	"""Returns the pth percentile of the exponential distribution with mean theta"""
	if p > 1:
		p1 = p / 100
	else:
		p1 = p
		
	if p1 > 1:
		out = "The 'p' argument must be a percentile less than 1"
	else:
		out = -theta * math.log(1 - p1)
	return(out)
	
def moment(k, theta):
	"""Returns the kth moment of the exponential distribution with mean theta"""
	try:
		k > - 1
	except:
		print('This function can only accept values of k greater than -1')
	
	out = (theta ** k) * math.gamma(k + 1)
	return(out)
	
def mean(theta):
	"""Returns the expected value of the exponential distribution with mean theta"""
	return(theta)
	
def variance(theta):
	"""Returns the variance of the exponential distribution with mean theta"""
	out = moment(2, theta=theta) - (mean(theta=theta)**2)
	return(out)
	
def var(theta):
	"""Alias for variance"""
	out = variance(theta)
	return(out)
	
def standard_deviation(theta):
	"""Returns the standard deviation of the exponential distribution with mean theta"""
	out = math.sqrt(variance(theta=theta))
	return(out)
	
def sd(theta):
	"""Alias for standard_deviation"""
	out = standard_deviation(theta=theta)
	return(out)
	
def limited_moment(k, limit, theta):
	"""Returns the kth moment of the exponential distribution with mean theta, limited to limit"""
	out = (theta ** k) * math.gamma(k + 1) * scipy.special.gammainc(k+1, limit/theta) + (limit ** k) * math.exp(-limit / theta)
	return(out)
	
def limited_mean(limit, theta):
	"""Returns the limited mean of the exponential distribution with mean theta"""
	out = limited_moment(k=1, limit=limit, theta=theta)
	return(out)
	
def limited_variance(limit, theta):
	"""Returns the limited variance of the exponential distrubtion with mean theta"""
	out = limited_moment(k=2, limit=limit, theta=theta) - (limited_mean(limit=limit, theta=theta) ** 2)
	return(out)
	
def limited_sd(limit, theta):
	"""Returns the standard deviation for an exponential distribution with mean theta, limited to limit"""
	out = math.sqrt(limited_variance(limit=limit, theta=theta)
	return(out)
	
def value_at_risk(p, theta):
	"""Returns the value at risk of the exponential distribution with mean theta, at probability p"""
	out = percentile(p=p, theta=theta)
	return(out)
	
def VaR(p, theta):
	"""Alias for value_at_risk"""
	out = value_at_risk(p=p, theta=theta)
	return(out)

def median(theta):
	"""Returns the median of the exponential distribution with mean theta"""
	out = math.log(2) * theta
	return(out)
	
def tail_value_at_risk(p, theta):
	"""Returns the TVaR at probability p for the exponential distribution with mean theta"""
	out = -theta * math.log(1 - p) + theta
	return(out)
	
def moment_generating_function(z, theta):
	"""Returns the moment-generating function (mgf) at z of the exponential distribution with mean theta"""
	out = (1 - theta * z) ** (-1)
	return(out)
	
def mgf(z, theta):
	"""Alias for moment_generating_function"""
	out = moment_generating_function(z=z, theta=theta)
	return(out)
	
def mode():
	"""Returns the mode of the exponential distribution"""
	return(0)
		
def skewness():
	"""Returns the skewness of the exponential distribution"""
	return(2)
	
def fisher_information(theta):
	"""Returns the Fisher information for an exponential distrubtion with mean theta"""
	out = theta**2
  return(out)
