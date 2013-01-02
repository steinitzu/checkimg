from argparse import ArgumentParser
import logging

from checkimg import img_is_good, check_dir

def _print_one_file(path, good=True, showgood=True, showbad=True):
    if good and showgood:
        print path, 'GOOD'
    elif not good and showbad:
        print path, 'BAD'

def print_one_file(path, show_bad=True, show_good=True):
    isgood = img_is_good(path)
    _print_one_file(path, isgood, show_good, show_bad)

def print_dir(path, showgood=True, showbad=True):
    for fb in check_dir(path):
        _print_one_file(
            fb[0], 
            good=fb[1],
            showgood=showgood,
            showbad=showbad
            )


def main():
    parser = ArgumentParser()
    parser.add_argument(
        'filename',
        help='Image file to check'
        )
    parser.add_argument(
        '-d', '--directory', dest='directory',
        help='Treat filename as a directory and scan it recursively.',
        action='store_true', default=False
        )
    parser.add_argument(
        '-b', '--show-bad', dest='show_bad',
        help='Show bad files in output. (default)',
        action='store_true', default=True
        )
    parser.add_argument(
        '-g', '--show-good', dest='show_good',
        help='Show good files in output. (default)',
        action='store_true', default=True
        )
    parser.add_argument(
        '-B', '--not-show-bad', dest='show_bad',
        help='Don\'t show bad files in output.',
        action='store_false', default=True
        )
    parser.add_argument(
        '-G', '--not-show-good', dest='show_good',
        help='Don\'t show good files in output.',
        action='store_false', default=True
        )


    args = parser.parse_args()
    if args.directory:
        print_dir(
            args.filename,
            showgood=args.show_good,
            showbad=args.show_bad
            )
    else:
        print_one_file(
            args.filename, 
            show_good=args.show_good,
            show_bad=args.show_bad
            )

    

if __name__ == '__main__':
    main()

