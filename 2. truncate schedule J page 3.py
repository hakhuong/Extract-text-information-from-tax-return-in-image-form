"""
Purpose: Truncate schedule J page 3 
Output: New .txt file with name begins by "filter-"
"""
import logging
import os
import sys
import re 

script_dir = os.path.dirname(os.path.realpath(__file__))
print(script_dir + '/truncate-text-tree.py: Start')

if len(sys.argv) > 1:
    start_dir = sys.argv[1]
else:
    start_dir = '.'

if len(sys.argv) > 2:
    log_file = sys.argv[2]
else:
    log_file = script_dir + '/truncate-text-tree.log'

logging.basicConfig(
                level=logging.INFO, format='%(asctime)s %(message)s',
                filename=log_file, filemode='w')

for dir_name, subdirs, file_list in os.walk(start_dir):
    logging.info('\n')
    logging.info(dir_name + '\n')
    os.chdir(dir_name)

    for filename in file_list:
        linesList = []
        file_name = os.path.splitext(filename)[0]
        file_ext = os.path.splitext(filename)[1]
        if file_ext == '.txt':
            full_path = dir_name + '/' + filename
            print(full_path)

            f = open(filename, 'r')

            newfile = open("filter-"+str(file_name)+".txt",'w')

            inRecordingMode = False

#Read EDN
            for line in f:
                EDN = re.match(r"\d{2}-\d{7}", line)
                if EDN is not None:
                    EDN = EDN.group(0)
                    print(EDN)
                    newfile.write("EDN: " + EDN)
                    break

#Read Schedule J Page 3     
            for line in f:
                if not inRecordingMode:
                    if line.startswith('nse Supplemental Information'):
                        print(line)
                        inRecordingMode = True

                elif line.startswith('Schedule J (Form 990) 2011') and inRecordingMode:
                    break

                if inRecordingMode:
                    linesList.append(line)

            linesList = linesList[1:]
            
            for item in linesList:
                newfile.write(item)

            print("done making text file")

            newfile.close()

        


            
            