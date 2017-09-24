import datetime
"""
Practice of datetime
"""

filename = datetime.datetime.now()

#create empty file
def create_file():
    """
    this function creates an empty file
    """
    with open(filename.strftime("%Y-%m-%d-%H-%M")+".txt","w") as file:
        file.write("")
create_file()
