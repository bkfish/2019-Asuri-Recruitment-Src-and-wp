## easy
首先看到是一个pyc文件，然后直接扔到在线解密:
```python
#!/usr/bin/env python
# encoding: utf-8
# 如果觉得不错，可以推荐给你的朋友！http://tool.lu/pyc

def encrypt_for_each():
    index = [
        0] * 100
    for i in range(100):
        tmp = i ^ 77
        yield tmp
        None
    


def encrypt(msg, key):
    iters = encrypt_for_each()
    enc = []
    for (m, k) in zip(msg, key):
        e = m ^ k ^ iters.__next__()
        enc.append(e)
    
    return enc


def generate_key():
    
    def check_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    test = [
        8,
        61,
        85,
        25,
        121,
        53,
        26,
        0,
        81,
        52,
        124,
        22,
        137,
        56,
        94,
        107,
        59,
        132,
        90,
        3,
        51,
        46,
        77,
        127,
        35,
        86,
        134,
        20,
        73,
        32,
        66,
        99,
        7,
        69,
        122,
        4,
        142,
        23,
        80,
        109,
        60,
        79,
        36,
        62,
        5,
        104,
        102,
        14,
        58,
        149,
        31,
        96,
        68,
        114,
        116,
        11,
        95,
        87,
        146,
        123,
        15,
        135,
        33,
        37,
        110,
        19,
        106,
        30,
        130,
        101,
        97,
        98,
        141,
        2,
        47,
        6,
        24,
        131,
        16,
        111,
        150,
        55,
        1,
        76,
        12,
        138,
        64,
        120,
        118,
        29,
        145,
        147,
        9,
        113,
        103,
        40,
        92,
        71,
        72,
        129,
        139,
        100,
        63,
        133,
        42,
        125,
        74,
        88,
        143,
        144,
        38,
        140,
        67,
        119,
        136,
        115,
        54,
        21,
        50,
        108,
        128,
        57,
        112,
        43,
        84,
        70,
        78,
        28,
        41,
        93,
        44,
        13,
        18,
        10,
        48,
        27,
        83,
        65,
        17,
        75,
        126,
        39,
        49,
        91,
        34,
        82,
        45,
        148,
        105,
        89,
        117]
    key = (lambda .0: continue[ i for i in .0 ])(filter(check_prime, test))
    return key

if __name__ == '__main__':
    key = generate_key()
    msg = [
        22,
        21,
        167,
        66,
        9,
        27,
        3,
        119,
        42,
        99,
        68,
        86,
        13,
        166,
        3,
        120,
        22,
        59,
        9,
        77,
        40,
        3,
        233,
        41,
        67,
        108,
        80,
        179,
        86,
        36,
        31,
        107,
        77,
        4,
        75]
    print('encryt message is {}'.format(msg))
```
然后就是python的简单逆向啦，发现加密的其实是一个异或，所以只需要重新把加密代码放到`encrypt`里面执行即可。

#### flag
`flag{P7th0n_Is_1nt3rst1ng_@nD_e4sy}`