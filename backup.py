import os
import zlib
import glob
import shutil
import zipfile
import datetime

class MakeBackup():

    def __init__(self, dir_file_copy, dir_file_paste):
        self.dir_file_copy = dir_file_copy
        self.dir_file_paste = dir_file_paste

    def list_to_zip(self):

        os.chdir(self.dir_file_copy)
        curr_date = datetime.datetime.now().date()
        curr_list = []    

        for f in glob.glob('*.bak'):
            created_date = datetime.datetime.fromtimestamp(os.stat(f).st_mtime)

            if created_date.date() == curr_date:
                curr_list.append(f)
        
        return curr_list

    def zip_list(self):
        
        if self.list_to_zip():

            zf = zipfile.ZipFile(f'backup{ datetime.datetime.now().strftime("%d%m%Y") }.zip', mode='w')

            try:
                for f in self.list_to_zip():
                    zf.write(f, compress_type= zipfile.ZIP_DEFLATED)
                    print(f'ziped {f}')
            finally:
                zf.close()

    def zip_move(self):
        for zp in glob.glob('*.zip'):
            shutil.move(os.path.relpath(zp), self.dir_file_paste)
            print(f'moved {zp}')

backup = MakeBackup("C:/", "C:/Users/Vaio/Desktop")
print(backup.list_to_zip())
backup.zip_list()
backup.zip_move()