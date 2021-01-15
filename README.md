# Knowledge of file handling

***Problem Definition***

Write sample file handling program that covers file operations like Create a new file, Open an existing file, Read file contents, Search data on a file,
Write into a new file, Close a file.

***File Handling Operations***

1. Create a file: Opening a file in "x"  mode creates a file and returns error if the file exist.

2. Open a file: We use open () function in Python to open a file in read or write mode.

            open(filename, mode)
            
            - Mode:
             1. “ r “, for reading.
             2. “ w “, for writing.
             3. “ a “, for appending.
             4. “ r+ “, for both reading and writing

3. Read from file: The read() method returns the specified number of bytes from the file. Default is -1 which means 
the whole file.

            file.read([size])
        
4. Write to a file: The write() write the specified text or bytes to the file. It overwrites the previous data in file.

            file.write('content to write')
            
5. Append to a file: Opening the file in 'a' or 'a+' mode  positions the handle at the end of the file. The data 
being written will be inserted at the end, after the existing data.

**Instructions to run program**

 

#References
- [w3school](https://www.w3schools.com/)
- [GeeksforGeeks](https://www.geeksforgeeks.org/)