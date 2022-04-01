import matplotlib
import matplotlib.pyplot as plt
import numpy as np

eps = 1
q = 1
N = 5
x0 = 7
x1 = 13
ND = 10

def main():
    #plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    #x = np.linspace(0, 10, 700)
    
    dh = ND / N
    dx = (x1 - x0) / (N - 1)
    C0 = -(q/eps) * dh * x1

    for i in range(N):

        h = (i + 1) * dh
        x = x1 - i * dx
        y = np.linspace(x - dx, x, 100)
        C = C0 - ((q/eps) * dh * x * i) + 3*i
        print(C, h, x, dh, dx)
        e = (q/eps) * h * y + C
        plt.plot(y, e, color='red')

    plt.show()


if __name__ == '__main__':
    main()