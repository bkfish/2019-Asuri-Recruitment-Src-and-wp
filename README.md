## 2019年Asuri招新赛安排
### 一、时间安排
时间预定于11月8号（周五），晚上6点半到10点，时长3个半小时
### 二、题目类型
本次招新赛分为 web,pwn,others(crypto+rev+misc)三类题型，每个题型分为easy,medium,hard三个等级
一般而言难易程度`easy<medium<hard`
### 三、出题
共有9道题


|方向|简单|中等|困难|主负责人|
|---|-------|--------|---------|-----|
|Web|baby-web|medium-web|hard-web|XXX|
|pwn|baby-pwn|medium-pwn|hard-pwn|XXX|
|others|baby-随意|medium-随意|hard-随意|XXX|

#### 出题人于11月5号前将题目文件发与题目负责人
题目文件目录格式
```
└─题目名称
    ├─题目描述.md            -------------关于文件部署以及其他相关注意事项         
    ├─wp                 
    │  ├─exp.py             -------------exp
    │  └─wp.md              -------------writeup
    └─src                   -------------题目源码
       ├─bin                -------------供选手下载的源文件
       └─others             -------------生成题目或者部署需要的其他文件（非必须）      
```