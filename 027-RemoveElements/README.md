Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

### solution

两个指针，都从头开始，一个用来填充一个寻找！=val 的项

l: 指向当前填充位

r: 指向寻找位

最后返回 l 