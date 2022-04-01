import matplotlib
import matplotlib.pyplot as plt
import numpy as np

eps = 11.8
q = 1.6
N = 50
x0 = 4
x1 = 8
ND = 10
NA = ND
V0 = 1
epsilon = chr(949)
#micro = chr()

def main():
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    #ax.xaxis.set_ticks_position('bottom')
    #ax.yaxis.set_ticks_position('left')

    ax.set_ylabel(chr(949) + "(x) (kV/m)")
    ax.set_xlabel("x (" + chr(956) + "m)")

    ax.yaxis.set_label_position("right")
    ax.xaxis.set_label_position("top")

    #x = np.linspace(0, 10, 700)
    
    dh = ND / N
    dx = (x1 - x0) / (N - 1)
    C = -(q/eps) * dh * x1

    for i in range(N-1):

        h = (i + 1) * dh
        x = x1 - i * dx
        y = np.linspace(x - dx, x, 100)
        if i != 0:
            C = -(q/eps) * dh * x + C
        e = (q/eps) * h * y + C
        plt.plot(y, e, color='red')


    C = -(q/eps) * dh * x + C
    y = np.linspace(0, x0, 600)
    e = (q/eps) * ND * y + C
    plt.plot(y, e, color='red')

    C = -(q/eps) * dh * x1

    for i in range(N-1):

        h = -(i + 1) * dh
        x = -x1 + i * dx
        y = np.linspace(x, x + dx, 100)
        if i != 0:
            C = +(q/eps) * dh * x + C
        e = (q/eps) * h * y + C
        plt.plot(y, e, color='red')

    C = +(q/eps) * dh * x + C
    y = np.linspace(-x0, 0, 600)
    e = -(q/eps) * ND * y + C
    plt.plot(y, e, color='red')

    plt.show()


if __name__ == '__main__':
    main()