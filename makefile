demos: fd_demo hash_demo

hash_demo: hash_demo.py
	hash_demo.py > hash_demo.out

fd_demo: fd_demo.c
	gcc -o fd_demo fd_demo.c

xxd_demo: xxd_demo
	xxd xxd_demo > xxd_demo.hex
