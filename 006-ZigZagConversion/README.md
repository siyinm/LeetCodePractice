## Zig Zag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
```
P   A   H   N
A P L S I I G
Y   I   R
```

1. 对(nRows-1)取余，可以区分行数。

2. 对(nRows-1)做除，可以区分当前是上升还是下降（偶数上升，奇数下降）。

3. 用string来储存character比数组更方便，别建二维数组了

4. 上下上下上下...循环，可以设flag判断是否转向，参考第2条