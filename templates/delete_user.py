import os

def delete_user(username):
    user_id = 1
    user_found = False
    user_account = 0

    # 檢查所有已存在的使用者帳密，計算總數
    while os.path.exists(f'user{user_id}.txt'):
        user_account += 1   # 計算總數
        # 檢查username是否存在
        with open(f'user{user_id}.txt', 'r') as f:
            if f.readline().strip() == username:
                user_found = True
                break
        user_id += 1    # 檢查下一個使用者檔案

    # 檢查有效的使用者帳密數量，若已達下限則顯示無法再進行刪除操作
    if user_account <= 1:
        print("Cannot delete user: the number is lower limit reached.")
        return

    if user_found:
        # 刪除使用者檔案
        os.remove(f'user{user_id}.txt')
        print(f"User {username} deleted successfully.")
        # 更新有效的使用者帳密數量
        user_account -= 1
    else:
        print(f"User {username} not found.")

if __name__ == '__main__':
    # 獲取欲刪除的使用者名稱，進行刪除操作
    username = input("Enter username to delete: ")
    delete_user(username)