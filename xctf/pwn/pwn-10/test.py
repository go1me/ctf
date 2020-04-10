from pwn import *
context(arch="i386",os="linux",log_level="debug")
p=remote(
elf=ELF("./pwn")
libc=EL
