import matplotlib.pyplot as plt
import numpy as np
import time
import matplotlib.cm as cm
import sys

plt.ion()

class GEMDistribution():
    def __init__(self, alpha):
        self.alpha = alpha
        self.cutoffs = [0]

    def sample(self):
        rand = np.random.uniform()

        while self.cutoffs[-1] < rand:
            new_sample = np.random.beta(1, self.alpha)
            scaled = new_sample * (1. - self.cutoffs[-1])
            self.cutoffs.append(self.cutoffs[-1] + scaled)

#        print "CUTOFFS", self.cutoffs
#        print "RAND", rand

        for i, cutoff in enumerate(self.cutoffs):
            if rand > cutoff and rand <= self.cutoffs[i+1]:
                return i

    def plot(self, slice=None):
        if slice == None:
            slice = len(self.cutoffs)
        plt.hlines(1,0,1)
        plt.eventplot(self.cutoffs[:slice], orientation='horizontal', colors='b')
        plt.show()
        plt.pause(0.0001)

    def keep_plotting(self, sleep=False):
        for i in xrange(len(self.cutoffs) + 1):
            self.plot(i)
            time.sleep(sleep)


#dist = GEMDistribution(2)
#for i in xrange(10):
#    print dist.sample()

class DirichletProcess():
    def __init__(self, alpha, mu_prior, sigma):
        self.dist = GEMDistribution(alpha)

        self.clusters = []  # (mean, sigma) pairs

        self.mu_prior = mu_prior  # (mean, sigma) pair of prior
        self.sigma = sigma  # sigma for each cluster

        self.points = []  # (x, y, cluster) tuples

    def add_point(self):
        cluster = self.dist.sample()

        while cluster >= len(self.clusters):
            # need to generate clusters
            new_mu = np.random.multivariate_normal(self.mu_prior[0], self.mu_prior[1])
            self.clusters.append( (new_mu, self.sigma) )

        cluster_mean = self.clusters[cluster][0]
        cluster_sig = self.clusters[cluster][1]
        new_point = np.random.multivariate_normal(cluster_mean, cluster_sig)

        to_add = (new_point[0], new_point[1], cluster)

        self.points.append(to_add)

    def plot(self):
        xs = [pt[0] for pt in self.points]
        ys = [pt[1] for pt in self.points]
        labels = [pt[2] for pt in self.points]

        plt.scatter(xs, ys, c=labels)
        plt.show()
        plt.pause(0.0001)

    def keep_plotting(self, steps, sleep=0.5):
        for i in xrange(steps):
            self.add_point()
            self.plot()
            draw = True
            time.sleep(sleep)


if __name__ == "__main__":

    assert len(sys.argv) == 3

    alpha = float(sys.argv[1])
    sleep = float(sys.argv[2])

    gem = GEMDistribution(alpha)

    for i in xrange(1000):
        gem.sample()

    gem.keep_plotting(sleep=sleep)

