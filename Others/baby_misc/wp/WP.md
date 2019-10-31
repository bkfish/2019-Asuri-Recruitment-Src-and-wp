## babymisc
首先检查文件类型（binwalk等工具即可），发现这个`babymisc`是一个压缩包，解压开发现里面还有一个压缩包。而且里面的压缩包还是加密了的。

### 选择明文攻击
当拥有压缩包中一个内容完全一致的文件时，我们就能利用算法的漏洞，在较短的时间内爆破出zip的密码（这一题测试的时候5min即可得到答案）。这里`babymisc`给出的`README.txt`和`misc`压缩包中的`README.txt`的CRC32值相等，说明内容一致。所以这里可以使用选择明文攻击。

这里推荐使用工具`archpr.exe`，可以直接可视化完成。具体操作步骤可参考[https://www.cnblogs.com/xdjun/p/7657105.html](https://www.cnblogs.com/xdjun/p/7657105.html)

爆破得到密码为`1145141919`，得到flag
```
flag{welcome_to_Misc}
```