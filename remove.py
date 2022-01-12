import os
import shutil
import time
def main():
    deletedFolderCount=0
    deletedFilesCount=0
    path="/PATH_TO_DELETE"
    days=1
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):