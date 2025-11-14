name=input("Enter the name:")
parts=name.split(".")
if len(parts)>1:
    print("The file extension is:",parts[-1])
else:
    print("no extension found.")