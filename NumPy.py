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

a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])

c = np.concatenate((a, b), axis=0)
print(c)
print(c.ndim, "\n")

d = np.concatenate((a, b), axis=1)
print(d)
print(d.ndim, "\n")

e = np.concatenate((a, b), axis=None)
print(e)
print(e.ndim, "\n")

f = np.stack((a, b))
print(f)
print(f.ndim, "\n")

g = np.vstack((a, b))
print(g)
print(g.ndim, "\n")

h = np.hstack((a, b))
print(h)
print(h.ndim, "\n")

i = np.dstack((a, b))
print(i)
print(i.ndim, "\n")

arr1 = np.array([1, 2, 3, 4, 5, 6])

arr2 = np.array_split(arr1, 3)
print(arr2, "\n")

arr3 = np.array_split(arr1, 4)
print(arr3, "\n")

arr4 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
arr5 = np.array_split(arr4, 3)
print(arr5, "\n")

arr6 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

arr7 = np.array_split(arr6, 3, axis=1)
print(arr7, "\n")

arr8 = np.hsplit(arr6, 3)
print(arr8)

arr9 = np.vsplit(arr6, 3)
print(arr9)


arr10 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]])
arr11 = np.dsplit(arr10, 3)
print(arr11)
print(arr11[0].ndim)

j = np.where(arr1 == 4)
print(j)

arr12 = np.array([6, 7, 8, 9])
k = np.searchsorted(arr12, 7)
print(k)

l = np.searchsorted(arr12, 7, side='right')
print(l)

arr13 = np.array([2, 4, 6, 8])
m = np.searchsorted(arr13, [1, 3, 5, 7])
print(m)

arr14 = np.array([3, 46, 32, 1, 5])
print(np.sort(arr14))
print(arr14)

arr15 = np.array(["banana", "cherry", "apple", "watermelon"])
print(np.sort(arr15))
print(arr15)

arr16 = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr16 = arr16 % 2 == 0
filtered_arr16 = arr16[filter_arr16]
print(filtered_arr16)
