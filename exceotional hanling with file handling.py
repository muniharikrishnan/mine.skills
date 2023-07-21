try:
    with open("mhk.txt","r") as file:
        file.read()
except FileNotFoundError:
    print("file is not exist")
except FileExistsError:
    print("file is already exists ,create a new file")
except:
    print("name error")
else:
    print("try block is successfully executed")
finally:
    print("exception handling with file handling is successfully execured")
    
