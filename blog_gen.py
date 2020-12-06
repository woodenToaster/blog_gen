import argparse
import datetime
import os
import sys

days_in_month = {
    1: 31,
    2: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

def init_unit(unit_dir, month, day):
    if args.day > days_in_month[args.month]:
        sys.exit("There are only {} days in month {}".format(days_in_month[args.month], args.month))

    assert(args.day)
    assert(args.month)

    os.mkdir(unit_dir)
    year = 20
    weeks = ["Week{}".format(x + 1) for x in range(4)]
    for week in weeks:
        week_dir = os.path.join(unit_dir, week)
        os.mkdir(week_dir)
        for _ in range(7):
            date_dir = "{}_{}_{}".format(month, day, year)
            date_path = os.path.join(week_dir, date_dir)
            os.mkdir(date_path)

            if day == days_in_month[month]:
                month += 1
                day = 1
            else:
                day += 1

            if month == 13:
                month = 1
                year += 1

def transfer_photos(unit_dir, week):
    assert(os.path.exists(unit_dir))

    week_dir = os.path.join(unit_dir, "Week{}".format(week))

    photos_fnames = [
        'Photos.zip',
        'Photos (1).zip'
        'Photos (2).zip'
        'Photos (3).zip'
        'Photos (4).zip'
        'Photos (5).zip'
        'Photos (6).zip'
    ]

    day_dirs = os.listdir(week_dir)
    for fname in sorted(day_dirs, key=lambda date: datetime.datetime.strptime(date, '%m_%d_%y')):
        print(os.path.join(week_dir, fname))


def main(args):
    base_dir = 'D:/drawing/work'

    unit_dir = os.path.join(base_dir, args.unit)

    if (args.day and args.month):
        init_unit(unit_dir, args.month, args.day)
    elif (args.week):
        transfer_photos(unit_dir, args.week)
    else:
        sys.exit("Either a day or a week is required")

    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--unit', required=True, help='The name of the unit')
    parser.add_argument('--month', type=int, help='The month number (January = 1)')
    parser.add_argument('--day', type=int, help='The start day of the month')
    parser.add_argument('--week', type=int, help='The week number to unzip photos for')

    args = parser.parse_args()

    main(args)
