def file_string(text):
    with open(text, 'r') as file:
        lines = file.read().split('\n')
    file.close()

    # in case we want to delete empty line uncomment below
    # while '' in lines:
    #     lines.remove('')

    new_file = open(text, 'w')
    for line in lines:
        if len(line) < 64:
            new_file.write(line)
            new_file.write('\n')
        else:
            j = 0
            x = len(line)
            while x > 0:
                if x > 64:  # the sign was >= and it's a bug ever since array
                            # of 5, there is no element in array[5] because
                            # maksimum is array[4]
                    i = j
                    j += 64
                    if line[j] == ' ':
                        new_file.write(line[i: j])
                        new_file.write('\n')
                    else:
                        while line[j] != ' ':
                            j -= 1
                        new_file.write(line[i: j])
                        new_file.write('\n')
                    x -= (j - i)
                else:
                    new_file.write(line[j: j+x+1])
                    new_file.write('\n')
                    x = 0
    new_file.close()

if __name__ == '__main__':
    codes = []
    strings = input("Give me the files...\n")
    strings += " "      # so that the else in line 47 will be execute at the end of the loop
    cod = ''
    for i in strings:
        if i != ' ':
            cod += i
        else:
            codes.append(cod)
            cod = ''
    while '' in codes:
        codes.remove('')
    for code in codes:
        file_string(code)
    print(f"All of these documents is successfully edited!\n\t{codes}")
