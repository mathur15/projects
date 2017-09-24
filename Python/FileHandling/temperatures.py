temperatures = [10,-20,-289,100]
def convert():
    with open("textFile.txt","w") as file:
        for item in temperatures:
            if item > 273:
                f = item * 9/5+32
                print(f)
                file.write(str(f)+"/n")
convert()
