//gcc -o prprpr -fstack-protector-all -no-pie prprpr.c
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

void sayHello1(char * str) {
    printf("Hello %s", str);
}

void sayHello2(char * str) {
    printf("Hello ");
    printf(str);
}

int main()
{
    char name[0x28];
    char doo[0x28];

    setvbuf(stdin, 0LL, 2, 0LL);
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stderr, 0LL, 2, 0LL);

    *(long long *)(name + 0x20) = (long long)sayHello1;

    puts("Please tell me your name!");
    gets(name);

    ((void (*)(char *))*(long long *)(name + 0x20))(name);
    
    puts("What do you want to do?");
    gets(doo);

    return 0;
}
