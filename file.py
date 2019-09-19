def replace_dots():

    with open('referat.txt', 'r', encoding='utf-8') as file:
        read_file = file.read()
        print(len(read_file))
        print(len(read_file.split()))
        read_file = read_file.replace('.', '!')
        return(read_file)

if __name__ == "__main__":
    with open('referat2.txt', 'w', encoding='utf-8') as file_two:
        file_two.write(replace_dots())
