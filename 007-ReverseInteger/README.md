## Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: $[−2^{31},  2^{31} − 1]$. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

### Solution

核心：

```cpp
while (x)
{
  res = res * 10 + x % 10; // 加号前面是先取得的值保持最高位, 后面则是取得原数的个位.
  x /= 10; // 裁剪原数, 确保能够从低位到高位的值, 能够被依次取得.
}
```

- Solution 1:

  Python转成str做很方便，倒转使用str ```[::-1]```

- Solution2：

  用上面写的数学方法

- Range的考虑

  1<<31: $-2^{31}$

  1<<31-1: $2^{31}​$

  
