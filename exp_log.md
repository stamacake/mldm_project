# Exps

## efficientnet

### first_try
METRICS:
- RMSE: 0.1969

Key points:
- embeddings from efficientnet
- One FC layer at top
- soft BCE loss 

Main problems:
- hard overfitting

Main progress:
- baseline
- validation scheme

### l2_regularization
METRICS:
- RMSE: 0.1884

Key points:
- L2 regularization on FC layer

Main progress:
- regularization makes problem with overfitting a little bit better. now we can see that validation score improved.

### l1_regularization
METRICS:
- RMSE: 0.1872

Key points:
- L1 regularization on FC layer

Main progress:
- approximately same as l2 regularization


### dim_reduction_pca
METRICS:
- RMSE: 0.2081

Key points:
- PCA embeddings reduction

Main problems:
- seems that linear reduction only make score worse

### dim_reduction
METRICS:
- RMSE: 0.1871 - 0.2+

Key points:
- Combine autoencoder and supervised problem
- adjsut reconstruction weight to proper regularization (learnable projection to lower space)

Main problems:
- overfitting appers anyway


### augmentation
METRICS:
- RMSE: 0.1797

Key points:
- use efficient net as backbone in the model itself. No embedding extraction.
- rotation and horizontal flipping augmentation (seem that do not affect strongly on picture perseption)
- All iamges in RAM but just because problems with shared memory

Main progress:
- score improved

Main problems:
- seems that there is an underfitting

