import os

def modify_user(username, new_password):
    user_id = 1

    # 檢查所有已存在的使用者帳密
    while os.path.exists(f'user{user_id}.txt'):
        # 打開當前使用者檔案並讀取username
        with open(f'user{user_id}.txt', 'r') as f:
            lines = f.readlines()

            # 若username與欲修改的使用者名稱相符
            if lines[0].strip() == username:
                # 確保lines列表至少有兩行
                if len(lines) < 2:
                    lines.append(new_password + '\n')
                else:
                    lines[1] = new_password + '\n'  # 更新password

                with open(f'user{user_id}.txt', 'w') as wf: # 寫入新密碼
                    wf.writelines(lines)

                print(f"Password for user {username} is modified successfully.")
                return  # 修改成功後返回
        user_id += 1    # 檢查下一個使用者檔案
    
    # 若檢查完所有使用者檔案還未找到名稱相符的檔案，則顯示以下訊息
    print(f"User {username} not found.")

if __name__ == '__main__':
    # 獲取欲修改的使用者名稱與新密碼，進行修改(密碼)操作
    username = input("Enter username to modify: ")
    new_password = input("Enter the new password: ")
    modify_user(username, new_password)