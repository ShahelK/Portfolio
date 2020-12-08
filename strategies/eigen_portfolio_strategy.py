# Basic libraries
import os
import warnings
import numpy as np
warnings.filterwarnings("ignore")

class EigenPortfolioStrategy:
	def __init__(self):
		print("Eigen portfolio strategy has been created")
		
	def generate_portfolio(self, symbols, covariance_matrix, eigen_portfolio_number):
		
		eig_values, eig_vectors = np.linalg.eigh(covariance_matrix)
		market_eigen_portfolio = eig_vectors[:,-1] / np.sum(eig_vectors[:,-1]) 
		eigen_portfolio = eig_vectors[:,-eigen_portfolio_number] / np.sum(eig_vectors[:,-eigen_portfolio_number]) 

		portfolio_weights_dictionary = dict([(symbols[x], eigen_portfolio[x]) for x in range(0, len(eigen_portfolio))])
		return portfolio_weights_dictionary
