def edit_file(text):
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
            line_length = len(line)   # x == line_length
            while line_length > 0:
                if line_length > 64:  # the sign was >= and it's a bug ever since in array of 5,
                                      # there last element is not at array[5] but array[4]
                    i = j
                    j += 64
                    if line[j] == ' ':
                        new_file.write(line[i: j])
                        new_file.write('\n')
                    else:
                        while line[j] != ' ' and j != -1:
                            j -= 1
                        new_file.write(line[i: j])
                        new_file.write('\n')
                        if j == -1:
                            break
                    line_length -= (j - i)
                else:
                    new_file.write(line[j: j+line_length+1])
                    new_file.write('\n')
                    line_length = 0
    new_file.close()

if __name__ == '__main__':
    codes = []
    files = input("Give me the files...\n")     # a string
    files += " "      # so that the else in line 48 will be execute at the end of the loop
    file = ''
    for char in files:
        if char != ' ':
            file += char
        else:
            codes.append(file)
            file = ''
    while '' in codes:
        codes.remove('')
    for code in codes:
        edit_file(code)
    print(f"All of these documents is successfully edited!\n\t{codes}")
