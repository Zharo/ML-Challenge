import h5py

f = h5py.File("X_train.h5")

print(list(f.keys()))

dset = f['data']
print(dset.shape)
print(dset.dtype)