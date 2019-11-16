#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>    

int door()
{
    system("/bin/sh");
}

int main()
{
    setvbuf(stdin, 0LL, 2, 0LL);
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stderr, 0LL, 2, 0LL);

    int a[20], size;
    unsigned usize;

    puts("I have a door.Could you open it?");
    puts("Please input your passworld size");

    scanf("%d",&size);

    if(size >= 20 || size < 0)
        exit(0);
    else {
	    puts("Please input your password");
	    usize = size - 1;
        read(0, a, usize);
    }
    return 0;
}
