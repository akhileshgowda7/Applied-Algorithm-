# Expectation-Maximization Algorithm for Clustering

import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error
from scipy.stats import multivariate_normal
import copy


def EM(D, k, eps):
    n = len(D)
    d = len(D[0])
    predictions = []
    means = []
    iterations_list = []
    for _ in range(20):
        posterior_probability = np.empty((k, n))
        new_mu = np.empty((k, d))
        mu = np.array([np.array(D[np.random.randint(0, n)]) for _ in range(k)])
        priors = np.array(np.full(k, 1 / k))
        cov_mat = np.array([np.identity(d) for _ in range(k)])
        error = 1
        prediction = []
        iterations = 0
        while error >= eps:
            iterations += 1
            for i in range(k):
                pdf = multivariate_normal.pdf(
                    D,
                    mean=mu[i],
                    cov=cov_mat[i]
                )
                posterior_probability[i] = np.matmul(pdf.reshape(n, 1), priors[i].reshape(1))
            for i in range(n):
                total = 0
                for j in range(k):
                    total += posterior_probability[j][i]
                for j in range(k):
                    posterior_probability[j][i] = posterior_probability[j][i] / total
            for i in range(k):
                weight = (np.sum(posterior_probability[i]) + eps)
                new_mu[i] = np.matmul(posterior_probability[i].reshape(1, n), D) / weight
                priors[i] = weight / n
                numerator = np.zeros((d, d))
                for j in range(n):
                    difference = np.subtract(D[j], mu[i]).reshape((d, 1))
                    product = posterior_probability[i][j] * np.matmul(difference, np.transpose(difference))
                    numerator += product
                cov_mat[i] = numerator / (np.sum(posterior_probability[i]) + eps)
                for x in range(d):
                    for y in range(d):
                        if x == y:
                            cov_mat[i][x][y] += eps
            error = mean_squared_error(mu, new_mu)
            mu = copy.deepcopy(new_mu)
        prediction = np.argmax(posterior_probability, axis=0)
        predictions.append(prediction)
        means.append(mu)
        iterations_list.append(iterations)
    return means, predictions, iterations_list

ionosphere_df = pd.read_csv('ionosphere.data', header=None)
D = ionosphere_df.iloc[:, :-1].to_numpy()
true_classes = np.array(pd.get_dummies(ionosphere_df.iloc[:, -1]).b)
true_means = np.array([list(ionosphere_df[ionosphere_df[34] == 'g'].mean()), np.array(list(ionosphere_df[ionosphere_df[34] == 'b'].mean()))])
ionosphere_graphs_data = {}
for k in [2, 3, 4, 5]:
    predicted_means, predicted_classes, iterations = EM(D, k, 0.000001)
    ionosphere_graphs_data[k] = {'error_rates': [], 'iterations': []}
    ionosphere_graphs_data[k]['iterations'] = iterations
    for j in range(len(predicted_means)):
        error = 0
        mean = predicted_means[j]
        for i in range(len(mean)):
            temp = true_means[0] - mean[i]
            sum_sq = np.dot(temp.T, temp)
            eucl1 = np.sqrt(sum_sq)
            temp = true_means[1] - mean[i]
            sum_sq = np.dot(temp.T, temp)
            eucl2 = np.sqrt(sum_sq)
            indices = [index for index, element in enumerate(predicted_classes[j]) if element == i]
            cluster = 'b'
            if eucl1 < eucl2:
                cluster = 'g'
            for index in indices:
                if ionosphere_df.iloc[index,-1] != cluster:
                    error += 1
        ionosphere_graphs_data[k]['error_rates'].append(error/len(D))
    print(min(ionosphere_graphs_data[k]['error_rates']))