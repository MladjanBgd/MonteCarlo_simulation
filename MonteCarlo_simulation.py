import random
import math
import pandas as pd
from matplotlib import pyplot as plt
from tqdm import tqdm


def calc_pi(N=100_000_000):
    # Monte Carlo simulation for approximation of Pi value
    Nin = 0
    Ntot = 0

    for i in tqdm(range(N)):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        d = math.sqrt(x**2 + y**2)
        if d < 1:
            Nin += 1

        Ntot += 1

    pi = 4 * (Nin / Ntot)

    print(f"And the pi number is: {format(pi, '.5f')}, Nin={Nin}, Ntot={Ntot}")
    print(f"Exact value of pi is: {format(math.pi, '.5f')}")
    print(f"And approx with 22/7: {format(22/7, '.5f')}")


def buffon_prob(N=1_000_000):
    # Monte Carlo simulation for "Buffon's needle problem"
    l = 5  # length of needle
    w = 10  # distance between lines //spacing
    match = 0
    p_frame = []

    for i in tqdm(range(N)):
        x = random.uniform(0, w)
        alpha = random.uniform(0, math.pi * 0.5)
        d = l * math.cos(alpha)
        pt1 = x - d / 2
        pt2 = x + d / 2

        if (pt2 >= 0 and pt1 <= 0) or (pt2 >= w and pt1 <= w):
            match += 1
        p_frame.append(match / N)
        # print(
        #     f"x={x:.2f}, alpha={alpha:.2f}, d={d:.2f}, pt1={pt1:.2f}, pt2={pt2:.2f}, i,match={i,match}"
        # )

    print(f"Probability is match/total={match/N:.4f}")
    print(f"Trialas={N} with match={match}, pi approx: {2*(N/match)*(l/w)}")

    pd.Series(p_frame).plot(kind="line")
    plt.ylabel("Probability")
    plt.axhline(y=(2 / math.pi) * (l / w), color="red")
    plt.axhline(y=p_frame[-1], color="green")
    plt.show()


calc_pi(N=10_000)
buffon_prob(N=5_000)
