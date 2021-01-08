#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

int main() {
    int fd;
    int pid;
    pid = getpid();
    printf("Process id is: %d\n", pid);
    printf("Press return to open new file descriptor.");
    getchar();
    fd = open("testing.txt",O_CREAT);
    if (fd == -1) {
        printf("Failed to open file.\n");
        return 1;
    }
    printf("Press return to close file descriptor and exit.");
    getchar();
    close(fd);
    return 0;
}
