import matplotlib.pyplot as plt
import random_process
import sys
import os
from tqdm import tqdm

BALANCE_PLOTS_FOLDER = 'plots/balance/'

if __name__ == '__main__':
    network_size = int(sys.argv[1])
    max_balance = int(sys.argv[2])
    perturbation = float(sys.argv[3])
    iterations = int(sys.argv[4])

    # Build balance plots folder.
    if not os.path.exists(BALANCE_PLOTS_FOLDER):
        os.makedirs(BALANCE_PLOTS_FOLDER)

    balances = []
    steps = []
    super_linearity = []
    for b in tqdm(xrange(1, max_balance + 1)):
        balances.append(b)
        s = random_process.average_run(network_size, b, perturbation, iterations)
        steps.append(s)
        super_linearity.append(s / float(b))

    # Plot number of payments
    plt.plot(balances, steps)
    plt.xlabel('Initial balance')
    plt.ylabel('Number of payments')
    plt.savefig(BALANCE_PLOTS_FOLDER + 'balances.png')
    plt.close()

    # Plot "super linearity"
    plt.plot(balances, super_linearity)
    plt.xlabel('Initial balance')
    plt.ylabel('G')
    plt.savefig(BALANCE_PLOTS_FOLDER + 'superlinearity.png')
    plt.close()


