import Rino

openFile = input("Run file or use terminal inputs? y/n: ")


if openFile == "y":

    directory = input("Input name of file and/or directory: ")

    with open(directory) as f:
        if f'{f.name.split(".")[len(f.name.split(".")) - 1]}' == "rno":
            text = f.read()
        else: print("File loader only supports .rno files.")
else:
    while True:

        text = input("Input Code: ")
        result, error = Rino.run('[code_input]', text)

        if(error):
            print(error.as_string())
        elif result:
            print(result)