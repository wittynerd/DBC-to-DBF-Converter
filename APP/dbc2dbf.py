'''

Converts all the DBC files in the current working directory (where the script is run from)
to DBF keeping the same name

'''

import os
##import canmatrix.convert as convert
import convert
import sys


if __name__ == "__main__":
    #print(sys.argv)
    #print(os.getcwd())

    '''

    if a dbc file/directory is provided as a argument
    convert that particular file/files in the directory.
    If no argument supplied, convert all the dbc files, if any,
    in the current working directory
    
    '''

    files = []
    for entry in sys.argv[1:]:
        if(os.path.isdir(entry)):
            Allfiles = os.scandir(entry)
            for f in Allfiles:
                files.append(f.path) if f.path.lower().endswith('.dbc') else None  
            pass
        elif(os.path.isfile(entry) and entry.lower().endswith('.dbc')):
            files.append(entry)
            pass
        pass
    
    if files == []:
        Allfiles = os.scandir(os.getcwd())
        for f in Allfiles:
            files.append(f.path) if f.path.lower().endswith('.dbc') else None 
        pass

    print(files)
    
    for file in files:
        #print(file)
               
        input_file = file
        #print(input_file)
        
        output_file = list(os.path.split(file))
        output_file[1] = output_file[1].replace("dbc", "dbf")
        output_file = os.path.join(output_file[0], output_file[1])
        #print(output_file)

        #Convert the DBC to DBF with same name
        convert.convert(input_file, output_file)
        pass
        
        pass
    pass

else:
    pass
