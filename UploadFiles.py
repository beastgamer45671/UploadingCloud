import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
  def _init_(self, access_token):
    self.access_token = access_token
    
  def upload_file(self, file_form, file_to):
    dbx = dropbox.Dropbox(self.access_token)
    
    for root, dirs, files in os.walk(file_from):
      for filename in files
      local_path = os.path.join(root, filename)
      
      relative_path = os.path.relpath(local, file_from)
      dropbox_path = os.path.join(file_to, relative_path)
      
      with open(local_path, 'rb') as f:
        dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))
        
  def main():
    access_token = "9876tyhGFTYUJIKUJHGBVcfrtyHJIuyhgvFRTYHJIuyhgfdertyHJMoi876t"
    transferData = TransferData(access_token)
    
    file_from = str(input("Enter the folder path to transfer: ")
    file_to = input("Enter the full path to upload to dropbox: ")
                    TransferData.upload_file(file_from, file_to)
                    print("Your file have been moved")
                    main()
