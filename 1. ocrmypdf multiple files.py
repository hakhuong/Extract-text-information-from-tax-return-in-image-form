"""
Purpose: Run orcmypdf on all pdf file in the directory folder

Output:
1. A pdf file with added "new-" in the beginning of the name
2. A text file (.txt), name kept as it is. 
"""

import logging
import os
import subprocess
import sys

script_dir = os.path.dirname(os.path.realpath(__file__))
print(script_dir + '/ocr-tree.py: Start')

if len(sys.argv) > 1:
    start_dir = sys.argv[1]
else:
    start_dir = '.'

if len(sys.argv) > 2:
    log_file = sys.argv[2]
else:
    log_file = script_dir + '/ocr-tree.log'

logging.basicConfig(
                level=logging.INFO, format='%(asctime)s %(message)s',
                filename=log_file, filemode='w')

for dir_name, subdirs, file_list in os.walk(start_dir):
    logging.info('\n')
    logging.info(dir_name + '\n')
    os.chdir(dir_name)
    for filename in file_list:
        file_ext = os.path.splitext(filename)[1]
        file_name = os.path.splitext(filename)[0]
        if file_ext == '.pdf':
            full_path = dir_name + '/' + filename
            print(full_path)
            newTextFile = str(file_name)+str(".txt")
            newPDFfile = "new-" + str(file_name)+".pdf"
            cmd = ["ocrmypdf",  "--sidecar", newTextFile, filename, newPDFfile]
            logging.info(cmd)
            proc = subprocess.run(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            result = proc.stdout
            if proc.returncode == 6:
                print("Skipped document because it already contained text")
            elif proc.returncode == 0:
                print("OCR complete")
            logging.info(result)