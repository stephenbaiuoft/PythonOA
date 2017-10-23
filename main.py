import sys
import processhtml as ph

def main():
    input_file = ""
    output_file = ""
    while len(input_file) == 0 or len(output_file) == 0:
        if len(input_file) == 0:
            input_file = input("please enter input filename: ")
        if len(output_file) == 0:
            output_file = input("please enter output filename: ")

    process_file(input_file, output_file)


    pass

def process_file(input_file, output_file):
    r_dic = ph.init_regex()

    try:
        fin = open(input_file, 'rt')
        fout = open(output_file, 'wt')
        try:
            for line in fin:
                line = ph.process_line(line, r_dic)
                fout.writelines(line)
                print (line)
        except:
            print("error with ph processing")

    except IOError:
        print("failed to open " + input_file + " or " + output_file)
        print(IOError)
        fin.close()
        fout.close()

if __name__ == '__main__':
    main()
