import numpy as np

nums1 = [1, 2, 3, 4]

np_nums1 = np.array(nums1)
np_nums2 = np.array((1, 2, 3))
np_nums3 = np.array([[1, 2, 3], [4, 5, 6]])

print(np_nums3)
print(np_nums1.ndim)
print(np_nums2.ndim)
print(np_nums3.ndim)

np_nums4 = np.array([[1, 2, 3], [4, 5, 6]], ndmin=4)
print(np_nums4, "\n", np_nums4.ndim)

np_text1 = np.array([1, 2, 3, 4], dtype='S')
print(np_text1)

np_nums5 = np.array([1, 2, 3, 4], dtype='i4')
print(np_nums5)
print(np_nums5.dtype)

np_nums6 = np.array([1.1, 2.2, 3.3])
np_nums7 = np_nums6.astype('i')
print(np_nums6, "\n", np_nums7)

np_nums8 = np_nums7.copy()
np_nums9 = np_nums7.view()
np_nums7[0] = 12

print(np_nums7)
print(np_nums8)
print(np_nums9)

print(np_nums8.base)
print(np_nums9.base)

print(np_nums3, np_nums3.shape, "\n", np_nums4, np_nums4.shape)

np_nums10 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
np_nums11 = np_nums10.reshape(4, 3)
np_nums12 = np_nums10.reshape(2, 2, 3)
np_nums13 = np_nums10.reshape(2, 3, -1)
np_nums14 = np_nums13.reshape(-1)

print(np_nums11)
print(np_nums11.ndim)
print(np_nums12)
print(np_nums12.ndim)
print(np_nums13)
print(np_nums13.ndim)
print(np_nums14)
print(np_nums14.ndim)

for i in np_nums12:
    print(i)

for i in np_nums12:
    for j in i:
        for k in j:
            print(k)

for i in np.nditer(np_nums12, flags=['buffered'], op_dtypes=['S']):
    print(i)

for idx, e in np.ndenumerate(np_nums10):
    print(idx, e)
