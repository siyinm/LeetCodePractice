一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

 

```
示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
```

### Solution

异或的性质

- 两个数字异或的结果a^b是将 a 和 b 的二进制每一位进行运算，得出的数字。 运算的逻辑是
  **如果同一位的数字相同则为 0，不同则为 1**

- 任何数和本身异或则为0

- 任何数和 0 异或是本身

- 异或满足交换律。 即 a ^ b ^ c ，等价于 a ^ c ^ b



分组的条件

1. 两个只出现一次的数字在不同的组中；
2. 相同的数字会被分到相同的组中。

记这两个只出现了一次的数字为 a和 b，那么所有数字抑或的结果就等于a和b 抑或的结果, 记为x

x的第i位为1，表示第i位两数字不同，以此为依据划分数组

两个数组的异或和就是两个数字的答案