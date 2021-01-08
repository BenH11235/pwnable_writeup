#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


int main(){
	setresuid(getegid(), getegid(), getegid());
	setresgid(getegid(), getegid(), getegid());
	system("bash -c 'echo shock_me'");
	return 0;
}

