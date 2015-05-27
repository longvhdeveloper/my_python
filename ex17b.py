from os.path import exists

from_file = raw_input("Enter your source file : ")
to_file = raw_input("Enter you destination file : ")
if exists(from_file):
    in_file = open(from_file)
    in_data = in_file.read()

    print "Copy from %s to %s" % (from_file, to_file)
    print "The input file %d bytes long" % len(in_data)

    if exists(to_file):
        print "Destination file is exists. Do you want replace by hit RETURN, CTRL-C to abort"
    else:
        print "Ready, hit RETURN to continue, CTRL-C to abort."
    raw_input('?')
    output_file = open(to_file, 'w')
    output_file.write(in_data)

    print "Alright, all done"

    output_file.close()
    in_file.close()
else:
    print "Your souce file is not exist"
