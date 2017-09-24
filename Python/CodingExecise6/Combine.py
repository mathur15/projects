import glob
import datetime
#make a list of the text files in the current directory
files = glob.glob("*.txt")
combined_content = ""

#open the a new file to in which you combine all the text files to read
with open(str(datetime.datetime.now())+".txt","w") as file:
    for item in files:
        with open(item,"r") as temp_file:
            combined_content += temp_file.read()
            combined_content += "\n"
    file.write(combined_content)
