import math
import csv
import os
import matplotlib.pyplot as plt
import numpy as np

# cwd = os.getcwd()
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def openFile(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        return list(reader)


def ramspeedAxValues(ax, x,title, labels,createdAxes,maxy):
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_xlabel('Test')
    ax.set_ylabel('Mb/s')
    ax.set_ylim([0,maxy])
    ax.set_title(title)
    ax.legend()

    for item in createdAxes:
       ax.bar_label(item, padding=3)

    return ax

def iozoneAxValues(ax,x,title, labels,createdAxes,maxy):
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_xlabel('Test')
    ax.set_ylabel('kBytes/s')
    ax.set_ylim([0,maxy])
    ax.set_title(title)
    ax.legend()

    for item in createdAxes:
       ax.bar_label(item, padding=3)

    return ax


def plotRamspeed():
    
    ramspeed3_docker = np.array(openFile('results/ramspeed/ramspeed3-docker.csv'))
    rampseed6_docker = np.array(openFile('results/ramspeed/ramspeed6-docker.csv'))

    ramspeed3_lin = np.array(openFile('results/ramspeed/ramspeed3_lin.csv'))
    ramspeed6_lin = np.array(openFile('results/ramspeed/ramspeed6_lin.csv'))

    ramspeed3_qemu = np.array(openFile('results/ramspeed/ramspeed3_qm.csv'))
    ramspeed6_qemu = np.array(openFile('results/ramspeed/ramspeed6_qm.csv'))

    y3Max = (float(max(ramspeed3_lin[:,0])) + 1000)
    y6Max = (float(max(ramspeed6_lin[:,0])) + 1000)

    labels = ramspeed3_lin[:, 1].tolist()
    x = np.arange(len(labels))

    fig, ax = plt.subplots(2,1)

    # Windows vs HyperV
    createdAxes = []
    createdAxes.append(ax[0].bar(x, ramspeed3_docker[:, 0].astype(np.float), 0.25, label='Docker'))
    createdAxes.append(ax[0].bar(x + 0.25, ramspeed3_lin[:, 0].astype(np.float),0.25, label='Linux Mint'))
    createdAxes.append(ax[0].bar(x + 0.50, ramspeed3_qemu[:, 0].astype(np.float),0.25, label='Qemu'))
    ax[0] = ramspeedAxValues(ax[0],x,'Integer Docker vs. Mint vs. Qemu',labels,createdAxes,y3Max)

    createdAxes = []
    createdAxes.append(ax[1].bar(x, rampseed6_docker[:, 0].astype(np.float), 0.25, label='Docker'))
    createdAxes.append(ax[1].bar(x + 0.25, ramspeed6_lin[:, 0].astype(np.float),0.25, label='Linux Mint'))
    createdAxes.append(ax[1].bar(x + 0.50, ramspeed6_qemu[:, 0].astype(np.float),0.25, label='Qemu'))
    ax[1] = ramspeedAxValues(ax[1],x,'Float Docker vs. Mint vs. Qemu',labels,createdAxes,y6Max)

    fig.tight_layout()
    plt.show()

def plotIozone():
    
    iozone_docker = np.array(openFile('results/iozone/iozone-t2-docker.csv'))
    iozone_lin    = np.array(openFile('results/iozone/iozone-t2-lin.csv'))
    iozone_qemu   = np.array(openFile('results/iozone/iozone-t2-qm.csv'))

    yMax = (float(max(iozone_lin[:,0])) + 5e5)

    labels = iozone_lin[:, 1].tolist()
    x = np.arange(len(labels))

    width = 0.25  # the width of the bars

    fig, ax = plt.subplots()
    createdAxes = []
    createdAxes.append(ax.bar(x-0.25, iozone_docker[:, 0].astype(np.float), 0.25, label='Docker'))
    createdAxes.append(ax.bar(x, iozone_lin[:, 0].astype(np.float),0.25, label='Linux Mint'))
    createdAxes.append(ax.bar(x+0.25, iozone_qemu[:, 0].astype(np.float),0.25, label='Qemu'))
    ax = iozoneAxValues(ax,x,'Docker vs. Mint vs. Qemu',labels,createdAxes,yMax)


    fig.tight_layout()
    plt.show()

def main():
    plotRamspeed()


if __name__ == "__main__":
    main()