echo Putting breakpoint...\n
break *main+195
echo Waiting for user input...\n
c
d 1
echo A\n
x/4xw *(int*)($ebp-0x14)
echo B\n
x/4xw *(int*)($ebp-0x0C)
echo C\n
x/4xw *(int*)($ebp-0x10)
