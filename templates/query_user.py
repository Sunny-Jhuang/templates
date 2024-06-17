import os

def query_user(username):
    user_id = 1

    # 檢查所有已存在的使用者帳密
    while os.path.exists(f'user{user_id}.txt'):
        # 打開當前使用者檔案並讀取username
        with open(f'user{user_id}.txt', 'r') as f:
            # 若username與欲查詢的使用者名稱相符
            if f.readline().strip() == username:
                print(f"User {username} is found.") # 顯示已找到的訊息
                return  # 查詢成功後返回
        user_id += 1    # 檢查下一個使用者檔案
    
    # 若檢查完所有使用者檔案還未找到名稱相符的檔案，則顯示以下訊息
    print(f"User {username} not found.")

if __name__ == '__main__':
    # 獲取欲查詢的使用者名稱，進行查詢操作
    username = input("Enter username to query: ")
    query_user(username)