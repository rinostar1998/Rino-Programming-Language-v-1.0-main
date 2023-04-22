import Rino

openFile = input("Run file or use terminal inputs? y/n: ")


if openFile == "y":

    directory = input("Input name of file and/or directory: ")

    with open(directory) as f:
        if f'{f.name.split(".")[len(f.name.split(".")) - 1]}' == "rno":
            text = f.read()
            result, error = Rino.run('[code_input]', text)

            if(error):
                print(error.as_string())
            elif result:
                if len(result.elements) == 1:
                    print(repr(result.elements[0]))
                else:
                   print(result)
        else: print("File loader only supports .rno files.")
else:
    while True:

        text = input("Input Code: ")
        result, error = Rino.run('[code_input]', text)

        if(error):
            print(error.as_string())
        elif result:
            if len(result.elements) == 1:
                print(repr(result.elements[0]))
            else:
                print(result)