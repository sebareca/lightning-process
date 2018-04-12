import random


def run_process(network_size, initial_balance, perturbation, amounts_dist):
    """ Run a simulation of a star shaped Lightning Network. Return the number of payments
        that where made before one of the channels balance went to zero.

    :param network_size: Integer, number of leaves.
    :param initial_balance: Integer, initial balance of each channel.
    :param perturbation: Float, indicates the bias of choosing node 0 to be the receiver,
        0 <= perturbation <= n - 1 / n.
    :param amounts_dist: A function that returns payment amounts.
    :return: Integer, the number of payments that where made before one of the channels balance went to zero.
    """
    # Build network.
    balances = {}
    for i in xrange(0, network_size):
        balances[i] = initial_balance

    # Build receiver probability array.
    receiver_pa = [1 / float(network_size) + perturbation]
    for i in xrange(1, network_size):
        receiver_pa.append(1 / float(network_size) - perturbation / (network_size - 1))

    steps = 1
    while True:
        # Choose receiver.
        receiver = _random_index(receiver_pa)

        # Choose sender. Avoid using custom random function if we can.
        sender = random.randint(0, network_size - 2)
        if sender >= receiver:
            sender += 1

        # Make payment.
        balances[sender] += amounts_dist()
        balances[receiver] -= amounts_dist()

        if balances[receiver] <= 0:
            return steps
        else:
            steps += 1


def average_run(network_size, initial_balance, perturbation, amounts_dist, iterations):
    """ Run simulation `iterations` times, return an average.

    """
    steps_sum = 0
    for i in xrange(0, iterations):
        steps_sum += run_process(network_size, initial_balance, perturbation, amounts_dist)

    return steps_sum / float(iterations)


def _random_index(pa):
    """ Choose a random integer n such that 0 <= n < len(ps) where the probability of choosing n
        is given by pa[n].

    :param pa: An array of probabilities, pa[0] + ... + pa[len(ps) - 1] must be equal to 1.0.
    :return: A random integer n such that 0 <= n < len(pa)
    """
    p = random.random()
    p_sum = 0
    for i in xrange(0, len(pa)):
        if p_sum <= p < p_sum + pa[i]:
            return i
        else:
            p_sum += pa[i]
