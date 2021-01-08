BITS 64

global _start

;constants
;system call ordinals
%define sys_read    0x000 
%define sys_write   0x001 
%define sys_open    0x002 
%define sys_exit    0x03C

;flag values
%define O_RDONLY    0x000
%define O_WRONLY    0x001
%define O_CREAT     0x040
%define S_IXUSR     0x040
%define S_IWUSR     0x080
%define S_IRUSR     0x100

;locals
%define buflen      0x100 

;constants and global variables
section .data 

source_file:
    db "source.txt", 0
destination_file:
    db "destination.txt", 0
buf:
    times buflen db 0

;code
section .text

_start:
    mov rdi, source_file ;fname
    mov rsi, O_RDONLY ;flags
    xor rdx, rdx ;mode
    mov rax, sys_open
    syscall

    mov rdi, rax ;fd
    mov rsi, buf ;buf
    mov rdx, buflen ;count
    mov rax, sys_read
    syscall
    
    mov rdi, destination_file ;fname
    mov rsi, O_WRONLY  
    or rsi, O_CREAT ;flags
    mov rdx, S_IRUSR 
    or rdx, S_IWUSR ;mode
    mov rax, sys_open
    syscall

    mov rdi, rax ; fd
    mov rsi, buf ;buf
    mov rdx, buflen ; count
    mov rax, sys_write
    syscall

    xor rdi, rdi
    mov rax, sys_exit
    syscall
