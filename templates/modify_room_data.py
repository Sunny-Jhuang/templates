import os

def modify_room_data(filename, new_filename):
    # 檢查檔案是否存在於當前本地端
    if filename.endswith('.jpg') and os.path.exists(filename):
        # 確保新的檔案名是以 .jpg 為結尾
        if not new_filename.endswith('.jpg'):
            new_filename += '.jpg'
        
        # 執行檔名修改
        os.rename(filename, new_filename)
        print(f"Data {filename} is renamed {new_filename}.")
    else:
        # 檔案不存在或者不是 .jpg 檔，印出錯誤訊息
        print(f"The .jpg file named {filename} couldn't be found.")

if __name__ == "__main__":
    # 讓使用者輸入要修改的資料名稱(來自fk資料夾)
    filename = input("Please enter the filename you want to modify (.jpg): ")
    # 讓使用者輸入新檔名
    new_filename = input("Please enter the new filename (.jpg): ")
    modify_room_data(filename, new_filename)