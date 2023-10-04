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

np
