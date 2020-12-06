#include <stdio.h>

struct Options {
    bool new_week;
    char *unit;
    int week;
};

void PrintUsage(char *program) {
    fprintf(stderr, "");
    exit(0);
}

Options HandleArgs(int argc, char **argv) {

    if () {
    }
}

int main(int argc, char **argv) {
    Options opt = HandleArgs(argc, argv);

    return 0;
}
