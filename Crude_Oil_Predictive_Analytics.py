# %% [markdown]
# # **Proyek Pertama : Predictive Analytics**
# 
# **Nama : Iqbal Tio Ardiansyah**
# 
# **Group : M06**

# %% [markdown]
# **Mengimport library yang dibutuhkan**

# %%
import yfinance as yf
import pandas as pd
import numpy as np

import seaborn as sns
from matplotlib import pyplot as plt
%matplotlib inline

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV, train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor

# %% [markdown]
# **Mengambil data Crude Oil pada yahoo finance**

# %%
cl = yf.Ticker("CL")
cl = cl.history(period="max")

# %%
cl

# %% [markdown]
# **Menghapus kolom yang tak digunakan**

# %%
cl = cl.drop(['Dividends', 'Stock Splits'], axis=1)

# %%
cl

# %% [markdown]
# **Menampilkan jumlah banyak data dan kolom pada dataset kita**

# %%
print(f'The data has {cl.shape[0]} records and {cl.shape[1]} columns.')

# %%
cl.info()

# %%
cl.describe()

# %% [markdown]
# **Melihat data null pada dataset**

# %%
cl.isnull().sum()

# %%
high = (cl.High == 0).sum()
low = (cl.Low == 0).sum()
open = (cl.Open == 0).sum()
close = (cl.Close == 0).sum()
vol = (cl.Volume == 0).sum()


print(high,low,open,close,vol)

# %% [markdown]
# **Visualisasi data**

# %%
numerical_col = [col for col in cl.columns if cl[col].dtypes == 'float64']
plt.subplots(figsize=(10,7))
sns.boxplot(data=cl[numerical_col]).set_title("Crude Oil Price")
plt.show()

# %% [markdown]
# **Menangani outliers pada data**

# %%
Q1 = cl.quantile(0.25)
Q3 = cl.quantile(0.75)
IQR = Q3-Q1
cl=cl[~((cl<(Q1-1.5*IQR))|(cl>(Q3+1.5*IQR))).any(axis=1)]

cl.shape

# %%
numerical_col = [col for col in cl.columns if cl[col].dtypes == 'float64']
plt.subplots(figsize=(10,7))
sns.boxplot(data=cl[numerical_col]).set_title("Crude Oil Price")
plt.show()

# %% [markdown]
# **Univariate Analytics**

# %%
cl.hist(bins=50, figsize=(20,15))
plt.show()

# %% [markdown]
# **Multivariate Analytics**

# %%
sns.pairplot(cl[numerical_col], diag_kind='kde')
plt.show()

# %%
plt.figure(figsize=(10,8))
corr = cl[numerical_col].corr().round(2)
sns.heatmap(data=corr, annot=True, vmin=-1, vmax=1, cmap='coolwarm', linewidth=0.5)
plt.title('Correlation matrix for numerical feature', size=15)
plt.show()

# %%
x = cl.iloc[:, 0:].values
y = cl.iloc[:,-1].values
print(x)

# %%
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state=42)

# %%
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

# %%
models = pd.DataFrame(columns=['train_mse', 'test_mse'], index=['Gradient Boosting', 'KNN', 'Random Forest'])

# %% [markdown]
# **Modeling**

# %%
def grid_search(model, hyperparameters):
  results = GridSearchCV(
      model,
      hyperparameters,
      cv=5,
      verbose = 1,
      n_jobs = -1,
  )

  return results

# %%
gradient_boost = GradientBoostingRegressor()
hyperparameters = {
    'learning_rate': [0.1, 0.01, 0.001, 0.0001, 0.00001],
    'n_estimators': [250, 500, 750, 1000],
    'criterion': ['friedman_mse', 'squared_error'],
}
gradient_boost_search = grid_search(gradient_boost, hyperparameters)
gradient_boost_search.fit(x_train, y_train)
print(gradient_boost_search.best_estimator_)
print(gradient_boost_search.best_params_)
print(gradient_boost_search.best_score_)

# %%
knn = KNeighborsRegressor()
hyperparameters = {
    'n_neighbors': [1,2,3,4,5,6,7,8,9,10],
}

knn_search = grid_search(knn, hyperparameters)
knn_search.fit(x_train, y_train)
print(knn_search.best_estimator_)
print(knn_search.best_params_)
print(knn_search.best_score_)

# %%
rf = RandomForestRegressor()
hyperparameters = {
    'n_estimators' : [10, 25, 50, 75, 100],
    'criterion' : ['squared_error', 'absolute_error', 'poisson'],
}

rdForestSearch = grid_search(rf, hyperparameters)
rdForestSearch.fit(x_train, y_train)
print(rdForestSearch.best_estimator_)
print(rdForestSearch.best_params_)
print(rdForestSearch.best_score_)

# %% [markdown]
# **Model Training**

# %%
gradient_boost = GradientBoostingRegressor(criterion='friedman_mse', learning_rate=0.01, n_estimators=1000)
gradient_boost.fit(x_train, y_train)

# %%
knn = KNeighborsRegressor(n_neighbors=4)
knn.fit(x_train, y_train)

# %%
rf = RandomForestRegressor(criterion='absolute_error', n_estimators=75)
rf.fit(x_train, y_train)

# %%
model_dict = {
    'Gradient Boosting':gradient_boost,
    'KNN':knn,
    'Random Forest':rf,
}

for name,model in model_dict.items():
  models.loc[name, 'train_mse'] = mean_squared_error(y_train, model.predict(x_train))
  models.loc[name, 'test_mse'] = mean_squared_error(y_test, model.predict(x_test))

models

# %%
models.sort_values(by='test_mse', ascending=True).plot(kind="barh", zorder=3)

# %%
gradientBoostAcc = gradient_boost.score(x_test, y_test)*100
randomForestAcc = rf.score(x_test, y_test)*100
knnAcc = knn.score(x_test, y_test)*100

# %%
eval_list = [[gradientBoostAcc],[randomForestAcc],[knnAcc]]
eval = pd.DataFrame(eval_list,
                    columns=['Acc (%)'],
                    index=['Gradient Boosting','Random Forest','K-Nearest Neighbor'])
eval

# %% [markdown]
# **Prediksi**

# %%
prediksi = x_test[:1].copy()
pred_dict = {'y_true':y_test[:1]}
for name, model in model_dict.items():
    pred_dict['prediksi_'+name] = model.predict(prediksi).round(1)
 
pd.DataFrame(pred_dict)


