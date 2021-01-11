
# exception handling left

def getChoice():
    print("-----------Operations------------------")
    print("1. Create a new File\n 2. Open existing file\n "
          "3. Read file contents\n 4. Write to new file\n "
          "5. Search data in file\n 6. Append to existing file and Read incremental data\n 7.  Exit")

    choice = int(input(" enter Your choice"))
    return choice


if __name__ == '__main__':

    choice = getChoice()
    while choice != 7:
         if choice == 1:
             file_name = str(input("Enter file name to create(eg. abc.txt):  "))
             with open(file_name, 'w+') as fp:
                 print("file created")
         elif choice == 2:
            file_name = str(input("Enter file name(eg. abc.txt):  "))
            with open(file_name,'r') as fp:
                print("file opened")
                #for each in fp:
                print(fp.tell())
         elif choice == 3:
             file_name = str(input("Enter file name(eg. abc.txt):  "))
             with open(file_name, 'r') as fp:
                 print(fp.read())

         elif choice == 4:
             file_name = str(input("Enter file name to write into(eg. abc.txt):  "))
             content= input("enter content(max 100 character) ")
             if len(content)>100:
                  raise Exception("limit exceeded")
             else:
                 with open(file_name, "w+") as fp:
                     fp.write(content)

         elif choice == 5:
             # search
            string_to_search = str(input("Enter string to search"))
            file_name = str(input("Enter file name(eg. abc.txt):  "))

            with open(file_name, 'r') as read_obj:
                # Read all lines in the file one by one
                for line in read_obj:
                     # For each line, check if line contains the string
                     if string_to_search in line:
                         print("found")

                     else:
                         print("not found")

         elif choice == 6:
             file_name = str(input("Enter file name to write into(eg. abc.txt):  "))
             content = input("enter content(max 100 character) ")
             if len(content) > 100:
                 raise Exception("limit exceeded")
             else:
                 with open(file_name, "a+") as fp:
                     pos= fp.tell()
                     fp.write("\n"+ content)
                     fp.seek(pos)
                     print(fp.read())

         else:
             print("Invalid choice. Please choose again!\n")
         choice = getChoice()


