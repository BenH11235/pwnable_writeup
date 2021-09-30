booklet: a_first_introduction_to_system_exploitation.tex demos
	pdflatex a_first_introduction_to_system_exploitation.tex
	pdflatex a_first_introduction_to_system_exploitation.tex #for table of contents

demos: fd_demo hash_demo xxd_demo

hash_demo: ./code/hash_demo.py
	./code/hash_demo.py > ./code/hash_demo.out

fd_demo: ./code/fd_demo.c
	gcc -o ./code/fd_demo ./code/fd_demo.c

xxd_demo: ./code/xxd_demo
	xxd ./code/xxd_demo > ./code/xxd_demo.hex

clean: 
	rm -f *.aux *.log *.out *.toc *.pdf

all: booklet


