import numpy as np
import pandas as pd
from sklearn.gaussian_process import GaussianProcessRegressor
import matplotlib.pyplot as plt
from skopt import gp_minimize

data = pd.read_csv("tp2_atdn_donnees.csv")

X = data[['Humidité (%)', 'Température (°C)']].values
y = data['Rendement agricole (t/ha)'].values

gp = GaussianProcessRegressor()
gp.fit(X, y)


def f(params):
    humidite, temperature = params
    X_test = np.array([[humidite, temperature]])
    pred = gp.predict(X_test)  
    return -pred.item() 

res = gp_minimize(f,  
                  dimensions=[(50, 90), (15, 35)], 
                  n_calls=20, 
                  random_state=42)

x_iters = np.array(res.x_iters)  
y_iters = -np.array(res.func_vals) 


print("Meilleure humidité et température pour maximiser le rendement : ", res.x)
print("Rendement maximal estimé : ", -res.fun)

plt.figure(figsize=(8, 5))
plt.plot(range(1, len(y_iters) + 1), y_iters, marker='o')
plt.xlabel("Itération")
plt.ylabel("Rendement estimé (t/ha)")
plt.title("Évolution du rendement estimé au fil des itérations")
plt.grid()
plt.show()

