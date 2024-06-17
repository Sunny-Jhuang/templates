import os

def add_user(username, password):
    user_id = 1
    user_account = 0
    user_exists = False

    # 檢查user(1~10).txt是否存在，並計算已存在的使用者帳密數量
    while user_id <= 10:
        if os.path.exists(f'user{user_id}.txt'):
            user_account += 1   # 儲存已存在的使用者帳密數量

            # 檢查username是否已存在
            with open(f'user{user_id}.txt', 'r') as f:
                existing_username = f.readline().strip()
                if existing_username == username:
                    user_exists = True
                    break
        else:
            break   # 若找不到，則中斷迴圈
        user_id += 1    # 檢查下一個使用者檔案
    
    # 若此username已存在，則顯示無法新增
    if user_exists:
        print(f"Cannot add user: username '{username}' already exists.")
    # 若已存在的使用者帳密數量超過10支(上限)，則顯示無法再新增
    elif user_account >= 10:
        print("Cannot add user: the number is upper limit reached.")
    else:
        # 創建新使用者檔案，並寫入其帳密
        with open(f'user{user_id}.txt', 'w') as f:
            f.write(f"{username}\n{password}")
        print(f"User {username} added successfully.")

if __name__ == '__main__':
    # 獲取欲新增的使用者帳密組，進行新增操作
    username = input("Enter username: ")
    password = input("Enter password: ")
    add_user(username, password)