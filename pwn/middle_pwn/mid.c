#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void backdoor ()
{
    system("/bin/sh");
}

int main(void)
{
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    int a = 0;
    char s [20];
    memset(s,'\x00',20);
    printf("hello,what's your name?,%13$p\n");
    read(0,s,0x40);
    printf("ok,%s.",s);
    return 0;
}
