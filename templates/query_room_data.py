import os
import subprocess
import re

def query_room_data(choice):
    # 讀取所有本地端 .jpg 檔案名稱(來自fk)
    fk_files = [file for file in os.listdir('./') if file.endswith('.jpg')]
    
    # 印出所有 .jpg 檔案名稱供使用者參考
    print("files add to local place:")
    for idx, file in enumerate(fk_files, start=1):
        print(f"{idx}.{file}")

    try:
        # 判斷使用者輸入的是編號還是名稱
        if choice.isdigit() and 1 <= int(choice) <= len(fk_files):
            file_to_open = fk_files[int(choice) - 1]
        elif choice in fk_files:
            file_to_open = choice
        else:
            raise ValueError("The index or filename entered is invalid.")

        # 使用命令開啟圖片(windows)
        subprocess.run(['start', os.path.join('./', file_to_open)], shell=True)
    
    except ValueError as e:
        print(f"Error: {e}")

def isdigit(s):
    return bool(re.match(r'^\d+$', s))
    
if __name__ == "__main__":
    # 讓使用者輸入要查詢並開啟的資料名稱(來自fk資料夾)
    choice = input("Please enter the filename you want to query (.jpg): ")
    query_room_data(choice)