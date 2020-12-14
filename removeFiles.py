import os
import shutil
import time

path    =   input("/Enter the name of the to be deleted :")
days    =   30

seconds =   time.time() -   (days   *   24  *   60  *   60)

if os.path.exists(path):
    for file in os.walk(path):
        if seconds  >= get_file_or_folder_age(root_folder):
            remove_folder(root_folder)
            deleted_folder_count    +=  1
            
            break

            else:
                for folders in folders:
                    folder_path = os.path.join(root_folder, folder)
                    
                    if seconds  >=  get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deleted_files_count += 1
                        
            else:
                if seconds >= get_file_or_folder_age(path):

				remove_file(path)
				deleted_files_count += 1 
    
            else:
               print(f'"{path}" is not found') 
               deleted_files_count  +=  1
               
               print(f"Total folders deleted: {deleted_folders_count}")
	           print(f"Total files deleted: {deleted_files_count}")

def remove_folder(path):
        if not shutil.rmtree(path):
            
        print(f"{path} is removed successfully")
        
        else:
          print(f"Unable to remove {path}")
          
def remove_file(path):
        if not os.remove(path):
            
        print(f"{path} is removed successfully")
        
        else:
          print(f"Unable to remove {path}")    
        
        
                
def get_file_or_folder_age(path):

	
	ctime = os.stat(path).st_ctime

	
	return ctime


if __name__ == '__main__':
	main()