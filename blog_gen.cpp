#include <stdio.h>

enum Months {
    Months_January = 1,
    Months_February,
    Months_March,
    Months_April,
    Months_May,
    Months_June,
    Months_July,
    Months_August,
    Months_September,
    Months_October,
    Months_November,
    Months_December,
};

enum Weekdays {
    Weekdays_Monday,
    Weekdays_Tuesday,
    Weekdays_Wednesday,
    Weekdays_Thursday,
    Weekdays_Friday,
    Weekdays_Saturday,
    Weekdays_Sunday
};

struct Options {
    bool new_week;
    char *unit;
    Months month;
    int week;
};

int GetDaysInMonth(Months month) {
    static const int kDaysPerMonth[] = {
        0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31,
    };

    int result = kDaysPerMonth[month + 1];

    return result;
}

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
