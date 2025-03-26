import sys
import messages


def valid_parameters(param):
    result = True

    if len(param) < 3:
        result = False

        return result


def main():
    messages.print_header()

    if not valid_parameters(sys.argv):
        messages.print_usage()
        return


if __name__ == '__main__':
    main()
