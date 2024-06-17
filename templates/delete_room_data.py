import os

def delete_room_data(filename):
    # 檢查檔案是否存在於當前本地端
    if filename.endswith('.jpg') and os.path.exists(filename):
        # 檔案存在，進行刪除操作
        os.remove(filename)
        print(f"Delete data {filename} successfully.")
    else:
        # 檔案不存在或者不是 .jpg 檔，印出錯誤訊息
        print(f"The .jpg file named {filename} couldn't be found.")

if __name__ == "__main__":
    # 讓使用者輸入要刪除的資料名稱(來自fk資料夾)
    filename = input("Please enter the filename you want to delete (.jpg): ")
    delete_room_data(filename)