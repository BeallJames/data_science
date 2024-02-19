import numpy as np
from sklearn import neighbors

## Playing with numpy
a = 3  # scalar
x = np.array([4, 5, 6])  # vector
y = np.array([7, 8, 9])

x_scaled = a * x   # scalar-vector product
sum_xy = x + y     # sum of two vectors

prod_xy = x * y    # elementwise product of two vectors
x_dot_y = x.dot(y) # dot product of two vectors

norm_x = np.linalg.norm(x)  # norm of vector
norm_y = np.linalg.norm(y)

dist_yx = np.linalg.norm(y - x)  # norm of vector difference (distance between two points)
dist_xy = np.linalg.norm(x - y)

## Movie recommendation example
possible_genres = ["horror", "action", "comedy", "romance", "drama"]

# Ratings of movies by each user (input features)
emma_x = np.array([1, 3, 5, 3, 4, 2])
alex_x = np.array([5, 1, 1, 2, 5, 2])
kate_x = np.array([2, 2, 3, 3, 2, 2])
carl_x = np.array([1, 1, 4, 5, 5, 2])
lily_x = np.array([3, 3, 2, 4, 1, 2])
sean_x = np.array([4, 3, 4, 2, 1, 2])

# Each user's favorite genre (feature to predict)
emma_y = "action"
alex_y = "horror"
kate_y = "comedy"
carl_y = "action"
lily_y = "comedy"
sean_y = ""  # try to predict sean's favorite genre!

# KNN is as simple as this
dist_emma_to_sean = np.linalg.norm(emma_x - sean_x)

# KNN with sklearn
k = 1  # try different values of k
clf = neighbors.KNeighborsClassifier(k)

data_x = np.array([emma_x, alex_x, kate_x, carl_x, lily_x])
data_y = np.array([emma_y, alex_y, kate_y, carl_y, lily_y])

clf.fit(data_x, data_y)

sean_y = clf.predict(np.array([sean_x]))[0]



# PS C:\Users\beall\OneDrive\Desktop\data_science\text\math\control_room\03_vectors_knn> ipython
# Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 8.21.0 -- An enhanced Interactive Python. Type '?' for help.

# In [1]: emma_x
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# Cell In[1], line 1
# ----> 1 emma_x

# NameError: name 'emma_x' is not defined

# In [2]: exit
# PS C:\Users\beall\OneDrive\Desktop\data_science\text\math\control_room\03_vectors_knn> ipython i- main.py
# [TerminalIPythonApp] WARNING | File 'i-' doesn't exist
# PS C:\Users\beall\OneDrive\Desktop\data_science\text\math\control_room\03_vectors_knn> ipython -i main.py
# Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 8.21.0 -- An enhanced Interactive Python. Type '?' for help.

# In [1]: em
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# Cell In[1], line 1
# ----> 1 em

# NameError: name 'em' is not defined

# In [2]: emma_y
# Out[2]: 'action'

# In [3]: emma_x
# Out[3]: array([1, 3, 5, 3, 4, 2])

# In [4]: np.linalg.norm(y - x) # sqrt((4-1)^2 + (5-2)^2 + (6-3)^2) = sqrt(27)
# Out[4]: 5.196152422706632

# In [5]: np.linalg.norm(lily_x - sean_x)
# Out[5]: 3.0

# In [6]: lily_y
# Out[6]: 'comedy'

# In [7]: data_x
# Out[7]:
# array([[1, 3, 5, 3, 4, 2],
#        [5, 1, 1, 2, 5, 2],
#        [2, 2, 3, 3, 2, 2],
#        [1, 1, 4, 5, 5, 2],
#        [3, 3, 2, 4, 1, 2]])

# In [8]: data_y
# Out[8]: array(['action', 'horror', 'comedy', 'action', 'comedy'], dtype='<U6')

# In [9]: from sklearn import neighbors, datasets

# In [10]: neighbors
# Out[10]: <module 'sklearn.neighbors' from 'C:\\Users\\beall\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\sklearn\\neighbors\\__init__.py'>  

# In [11]: k=1

# In [12]: clf
# Out[12]: KNeighborsClassifier(n_neighbors=1)

# In [13]: k=2

# In [14]: clf
# Out[14]: KNeighborsClassifier(n_neighbors=1)

# In [15]: k
# Out[15]: 2

# In [16]: clf
# Out[16]: KNeighborsClassifier(n_neighbors=1)

# In [17]: clf.fit()
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# Cell In[17], line 1
# ----> 1 clf.fit()

# File ~\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\base.py:1351, in _fit_context.<locals>.decorator.<locals>.wrapper(estimator, *args, **kwargs)
#    1344     estimator._validate_params()
#    1346 with config_context(
#    1347     skip_parameter_validation=(
#    1348         prefer_skip_nested_validation or global_skip_validation
#    1349     )
#    1350 ):
# -> 1351     return fit_method(estimator, *args, **kwargs)

# TypeError: KNeighborsClassifier.fit() missing 2 required positional arguments: 'X' and 'y'

# In [18]: clf.fit(data_x,data_y)
# Out[18]: KNeighborsClassifier(n_neighbors=1)

# In [19]: clf.predict(sean_x)
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# Cell In[19], line 1
# ----> 1 clf.predict(sean_x)

# File ~\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\neighbors\_classification.py:271, in KNeighborsClassifier.predict(self, X)
#     268         return self.classes_[np.argmax(probabilities, axis=1)]
#     269     # In that case, we do not need the distances to perform
#     270     # the weighting so we do not compute them.
# --> 271     neigh_ind = self.kneighbors(X, return_distance=False)
#     272     neigh_dist = None
#     273 else:

# File ~\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\neighbors\_base.py:826, in KNeighborsMixin.kneighbors(self, X, n_neighbors, return_distance)
#     824         X = _check_precomputed(X)
#     825     else:
# --> 826         X = self._validate_data(X, accept_sparse="csr", reset=False, order="C")
#     828 n_samples_fit = self.n_samples_fit_
#     829 if n_neighbors > n_samples_fit:

# File ~\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\base.py:633, in BaseEstimator._validate_data(self, X, y, reset, validate_separately, cast_to_ndarray, **check_params)
#     631         out = X, y
#     632 elif not no_val_X and no_val_y:
# --> 633     out = check_array(X, input_name="X", **check_params)
#     634 elif no_val_X and not no_val_y:
#     635     out = _check_y(y, **check_params)

# File ~\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\utils\validation.py:989, in check_array(array, accept_sparse, accept_large_sparse, dtype, order, copy, force_all_finite, ensure_2d, allow_nd, ensure_min_samples, ensure_min_features, estimator, input_name)
#     982         else:
#     983             msg = (
#     984                 f"Expected 2D array, got 1D array instead:\narray={array}.\n"
#     985                 "Reshape your data either using array.reshape(-1, 1) if "
#     986                 "your data has a single feature or array.reshape(1, -1) "
#     987                 "if it contains a single sample."
#     988             )
# --> 989         raise ValueError(msg)
#     991 if dtype_numeric and hasattr(array.dtype, "kind") and array.dtype.kind in "USV":
#     992     raise ValueError(
#     993         "dtype='numeric' is not compatible with arrays of bytes/strings."
#     994         "Convert your data to numeric values explicitly instead."
#     995     )

# ValueError: Expected 2D array, got 1D array instead:
# array=[4 3 4 2 1 2].
# Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.

# In [20]: clf.predict(np.array([sean_x]))
# Out[20]: array(['comedy'], dtype='<U6')

# In [21]: sean_y = clf.predict(np.array([sean_x]))[0]

# In [22]: sean_y
# Out[22]: 'comedy'

# In [23]: clear
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# Cell In[23], line 1
# ----> 1 clear

# NameError: name 'clear' is not defined

# In [24]: clear
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# Cell In[24], line 1
# ----> 1 clear

# NameError: name 'clear' is not defined

# In [25]: k=3

# In [26]: k
# Out[26]: 3

# In [27]: clf2 = neighbors.KNeighborsClassifier(k)

# In [28]: clf2
# Out[28]: KNeighborsClassifier(n_neighbors=3)

# In [29]: clf2.fit(data_x, data_y)
# Out[29]: KNeighborsClassifier(n_neighbors=3)

# In [30]: clf2.predict(np.array([sean_x]))
# Out[30]: array(['comedy'], dtype='<U6')