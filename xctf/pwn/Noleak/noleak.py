from pwn import *
context(arch="amd64",os="linux",terminal=["tmux","splitw","-h"],log_level="debug")
GDB = args["GDB"]
p= process("./timu",env={"LD_PRELOAD":"./libc-2.23.so"})

if GDB=="1":
    gdb.attach(p)

print(p.recv())
pause()
