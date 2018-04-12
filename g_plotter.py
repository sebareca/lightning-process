import matplotlib.pyplot as plt
import random_process
import sys
import os

G_PLOTS_FOLDER = 'plots/g/'

if __name__ == '__main__':
    max_balance = int(sys.argv[1])
    p = float(sys.argv[2])

    # Build balance plots folder.
    if not os.path.exists(G_PLOTS_FOLDER):
        os.makedirs(G_PLOTS_FOLDER)

    balances = []
    values = []
    for b in xrange(1, max_balance + 1):
        balances.append(b)
        values.append(random_process.g(b, p))

    plt.plot(balances, values)
    plt.xlabel('Initial balance')
    plt.ylabel('G')
    plt.savefig(G_PLOTS_FOLDER + 'g.png')
    plt.close()