import numpy as np
import matplotlib.pyplot as pt

X = np.array([[145, 156, 147, 157, 175, 160, 162, 184]]).T;
y = np.array([[60, 65, 61, 66, 71, 64, 65, 75]]).T;

pt.plot(X, y, 'ro');
pt.xlabel("Height(cm)");
pt.ylabel("Weight(kg)");

demension = X.shape;
ones = np.ones((demension[0], 1));

Xbar = np.concatenate((ones, X), axis=1)
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A),b);
wAfter = np.array([w[:, 0]]);
print(wAfter)
x1 = np.linspace(130,190, 2).reshape(2, 1);
ones2 = np.ones((2, 1));
xtest = np.concatenate((ones2, x1), axis=1).T
print(xtest)
ytest = np.dot(wAfter, xtest)
pt.plot(x1, ytest.T);
pt.show()


