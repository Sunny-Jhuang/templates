import os
import shutil

def add_room_data(filename):
    # 指定要讀取的資料夾路徑
    folder_path = './fk'

    # 讀取資料夾內的所有檔案
    files = os.listdir(folder_path)

    # 印出所有檔案名稱供使用者參考
    print("files in the folder:")
    for file in files:
        print(file)

    # 檢查使用者輸入的資料是否存在於資料夾內
    if filename in files:
        # 檔案存在，進行複製或移動等操作至本地端
        source_file = os.path.join(folder_path, filename)
        shutil.copy(source_file, './')  # 因目前fk資料夾與新增目的地位、本程式於同一路徑
        print(f"Data {filename} added successfully.")
    else:
        # 檔案不存在，印出錯誤訊息
        print(f"The data named {filename} couldn't be found in the folder.")

if __name__ == "__main__":
    # 讓使用者輸入要新增的資料名稱
    filename = input("Please enter the filename you want to add: ")
    add_room_data(filename)