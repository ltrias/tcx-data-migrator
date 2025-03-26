import sys
import messages
import TCXFile


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
    src_file = TCXFile.TCXFile(sys.argv[1])
    dst_file = TCXFile.TCXFile(sys.argv[2])

    src_file.save(sys.argv[1].replace('.tcx', '_out.tcx'))
    dst_file.save(sys.argv[2].replace('.tcx', '_out.tcx'))


if __name__ == '__main__':
    main()
