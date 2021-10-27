def edit_file(file_name):
    # read the text of the file and split it according to newline,
    # and store the content to 'lines' variable
    file = open(file_name, "r")
    lines = file.read().split("\n")
    file.close()

    # replace the file that we edit by creating a new file with the same name
    new_file = open(file_name, "w")

    max_char_per_line = 64
    # loop through all the text from the file
    for line in lines:
        line = line.strip()
        # simply just write it to the file, if the length of the line is less/equal than 64
        if len(line) <= max_char_per_line:
            new_file.write(line)
            new_file.write("\n")
        else:
            while len(line) > max_char_per_line:
                i = max_char_per_line
                # if the 65th char is " ", then write the text from 0 to 64
                if line[i] == " ":
                    new_file.write(line[0: i])
                    new_file.write("\n")
                    line = line[i: len(line)]
                # if the 65th char is not " ",
                else:
                    # then we look for (<65)th char that is " "
                    while line[i] != " " and i != -1:
                        i -= 1
                    # if we couldn't find the " ", because the word is longer than 64 chars
                    # then we cut the word, and then put "-" at the end
                    if i == -1:
                        new_file.write(line[0: max_char_per_line])
                        new_file.write("-")
                        # we delete the string that already written
                        line = line[max_char_per_line: len(line)]
                    # if we can find the " " at the (<65)th char, then we write it
                    else:
                        new_file.write(line[0: i])
                        # we delete the string that already written
                        line = line[i: len(line)]
                    new_file.write("\n")
            else:
                new_file.write(line)
                new_file.write("\n")
    
    # close and save the file
    new_file.close()

# it starts here
if __name__ == "__main__":
    # asking input the names of the files
    input_desc = "Give me all the files...\n" \
            "Separate the name of the files with a space.\n" \
            "For example: \'file_1 file_2\'\n\n"
    files_string = input(input_desc)

    # split the string of the input according to space,
    # so we have an array that consists of files' name
    files_array = files_string.split()

    # edit all the files with loop
    for file in files_array:
        edit_file(file)
    
    print(f"All of these documents is successfully edited!\n\t{files_array}")