#%%

!pip3.12 install matplotlib
import matplotlib.pyplot as plt
import numpy as np
# %%
def arma_sim(x0,phi,theta, sigma, N):
    epsilon = sigma*np.random.randn(N+1)
    x = [x0]
    for t in np.arange(1,N):
        xt= phi*x[t-1]+epsilon[t]+theta*epsilon[t-1]
        x- np.append(x,xt)
    return x

# %%
np.random.seed(97)
x_arma = arma_sim