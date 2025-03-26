import sys
import os


def valid_parameters(param):
    result = True

    if len(param) < 3:
        result = False

        return result


def print_usage():
    message = """
    Usage: python +script_name+  <src filename> <dst filename> <metric>
        <src filename>: origin of the <metric> data
        <dst filename>: file where <src filename> <metric> will be merged into
        <metric>: metric to migrate, defaults to HR (heart rate)
    """

    print(message.replace("+script_name+", os.path.basename(__file__)))


def print_header():
    message = """TCX Data Migrator by Lucas Trias - github.com/ltrias
    Allows to merge data from a tcx file into another one
    For instance, merge Polar chest strap heart rate data into Garmin watch tracked activity"""

    print(message)


def main():
    print_header()

    if not valid_parameters(sys.argv):
        print_usage()
        return


if __name__ == '__main__':
    main()
