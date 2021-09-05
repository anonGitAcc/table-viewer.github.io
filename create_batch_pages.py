import json
import os
import sys
from bs4 import BeautifulSoup
# copy the template

for i in range(4, 55):
    # create folder
    folder_name = "./batch_pages/batch" + str(i) + "/"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # copy template
    src_file = "./index_as_template.html"
    dst_file = folder_name + "index.html"

    os.system("cp {} {}".format(src_file, dst_file))

    # edit div
    f = open(dst_file, "r")
    content = f.read()
    soup = BeautifulSoup(content, 'html.parser')

    batchdiv = soup.find(id="batchNumDiv")
    batchdiv.string = str(i)

    with open(dst_file, "wb") as f_o:
        f_o.write(soup.prettify("utf-8"))

    f.close()
