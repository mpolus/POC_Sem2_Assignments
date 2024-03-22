file_path = "C:\\Users\\polusmal001\\DEV\\POC_Sem2_Assignments-2\\10_Functional Programming\\03_File_Handling_2\\newfile.txt"

try:
    stream = open(file_path, 'w')
    stream.write('This is the first message!\n')
    stream.write('This is the second message!\n')
    stream.write('This is my third message!')
    stream.close()
except Exception as e:
    print('An error occurred:', e)