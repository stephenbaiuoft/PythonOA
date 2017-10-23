import sys
import processhtml as ph

def main():
    # input_file = ""
    # output_file = ""
    # while len(input_file) == 0 or len(output_file) == 0:
    #     if len(input_file) == 0:
    #         input_file = input("please enter input filename: ")
    #     if len(output_file) == 0:
    #         output_file = input("please enter output filename: ")

    input_file = "test.html"
    output_file = "o1.txt"
    input_file1 = "t2.html"
    output_file2 = "o2.txt"
    process_file(input_file, output_file)
    process_file(input_file1, output_file2)

    pass

def process_file(input_file, output_file):
    r_dic = ph.init_regex()

    try:
        fin = open(input_file, 'rt')
        fout = open(output_file, 'wt')
        try:
            # read the entire file
            ftxt = fin.read()
            #print(ftxt)
            foutput = ph.process_line(ftxt, r_dic)

            print("\noutput is:\n" + foutput)
            fout.writelines(ftxt)


        except IOError:
            print(IOError)
            print("error with ph processing")

    except IOError:
        print("failed to open " + input_file + " or " + output_file)
        print(IOError)
        fin.close()
        fout.close()

if __name__ == '__main__':
    main()
