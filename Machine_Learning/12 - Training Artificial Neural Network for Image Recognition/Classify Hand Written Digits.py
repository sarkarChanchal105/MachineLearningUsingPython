"""
Source :
http://yann.lecun.com/exdb/mnist/
"""

import os,struct,numpy as np
import matplotlib.pyplot as plt
from tables.table import _index_name_of_


def load_mnist(path,kind='train'):
    """
    Load MNIST data from path
    :param path:
    :param kind:
    :return:
    """
    labels_path = os.path.join(path,'%s-labels-idx1-ubyte'% kind)

    images_path= os.path.join(path,'%s-images-idx3-ubyte'% kind )

    with open(labels_path,'rb') as lbpath:
        magin, n=struct.unpack('>II',lbpath.read(8))
        labels=np.fromfile(lbpath,dtype=np.uint8)

    with open(images_path,'rb') as imgpath:
        magic,num,rows,cols = struct.unpack(">IIII",imgpath.read(16))
        images= np.fromfile(imgpath,dtype=np.uint8).reshape(len(labels),784)

    return images, labels


def show_few_digit():
    X_train, y_train = load_mnist('../../large-data-files/mnist', kind='train')
    X_test, y_test = load_mnist('../../large-data-files/mnist', kind='t10k')

    fig,ax = plt.subplots(nrows=2,ncols=5,sharex=True,sharey=True)

    ax=ax.flatten()
    for i in range(10):
         img=X_train[y_train==i][0].reshape(28,28)
         ax[i].imshow(img,cmap='Greys', interpolation='nearest')

    plt.show()


def show_same_digit():
    X_train, y_train = load_mnist('../../large-data-files/mnist', kind='train')
    X_test, y_test = load_mnist('../../large-data-files/mnist', kind='t10k')

    fig, ax = plt.subplots(nrows=2, ncols=5, sharex=True, sharey=True)

    ax = ax.flatten()
    for i in range(10):
        img = X_train[y_train == 7][i].reshape(28, 28)
        ax[i].imshow(img, cmap='Greys', interpolation='nearest')

    plt.show()


def main():
    show_few_digit()
    show_same_digit()


if __name__ == main():
    main()

