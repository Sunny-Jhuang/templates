from flask import Flask, request, redirect, url_for, render_template_string, session
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from main_control_panel import MainWindow
import sys
import requests
import threading
import traceback
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # 設置密鑰以便使用session

def load_accounts():
    accounts = []
    for i in range(1, 11):  # 使用者帳密數量上限為10組
        filename = f'user{i}.txt'
        if os.path.exists(filename):    # 讀取本地資料夾內的每個使用者帳密檔，檔案名稱皆為user(數字).txt
            with open(filename, 'r') as f:
                username = f.readline().strip()
                password = f.readline().strip()
                accounts.append({'username': username, 'password': password})
    return accounts # 回存至accounts陣列

@app.route('/login', methods=['GET', 'POST'])
def login():
    accounts = load_accounts()  # 接收已存在的(accounts)使用者帳密

    # 讀取使用者輸入的帳密
    if request.method == 'POST':
        username = request.form['un']
        password = request.form['pwd']

        # 使用者登入成功
        for account in accounts:
            if account['username'] == username and account['password'] == password:
                session['logged_in'] = True
                return redirect(url_for('success'))
        
        # 使用者登入失敗頁面
        return render_template_string('''
            <h1>Login Failed</h1>
            <a href="{{url_for('login')}}">Try Again</a>
        ''', url_for=url_for)
    
    # 登入失敗，重回登入頁面
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="zh_tw">
    <head>
        <meta charset="utf-8">
        <title>login page</title>
        <style>
            body{
                font-family: Arial, sans-serif;
            }

            .container{
                width: 300px;
                margin: 0 auto;
                padding: 20px;
                border: 1px solid #ccc;
                border-radius: 5px;
                background-color: #f9f9f9;
            }

            input[type="text"],
            input[type="password"],
            input[type="submit"]{
                width: 100%;
                padding: 10px;
                margin: 5px 0;
                box-sizing: border-box;
            }

            input[type="submit"]{
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Login</h1>
            <form enctype="multipart/form-data" method="post" action="{{url_for('login')}}">
                Username:<br/>
                <input type="text" name="un" required/><br/>
                Password:<br/>
                <input type="password" name="pwd" required/><br/>
                <input type="submit" name="sub" value="Login"/>
            </form>
        </div>
    </body>
    </html>
    ''')

# 登入成功頁面(返回一個簡單的"成功登入"頁面即可)
@app.route('/success')
def success():
    if 'logged_in' in session and session['logged_in']:
        app = QtWidgets.QApplication(sys.argv)
        window = MainWindow()
        window.show()

        # 發送GET請求檢查用戶是否已登入
        try:
            response = requests.get('http://127.0.0.1:5000/success')
            if response.status_code == 200:
                window.show_main_control_panel()
            else:
                login()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            login()

        sys.exit(app.exec_())
    else:
        return redirect(url_for('login'))   # 若未登入則重新導回login頁面

# 從Main Control Panel登出(按下"Logout"鍵)
@app.route('/logout')
def logout():
    session.pop('logged_in', None)  # 確保註銷登入狀態
    return redirect(url_for('login'))   # 回到登入頁面

@app.errorhandler(Exception)
def handler_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e
    
    # how you're handling non-HTTP exceptions only
    return render_template_string('''
        <h1>Internal Server Error</h1>
        <p>{{error}}</p>
        <pre>{{traceback}}</pre>
    ''', error=str(e), traceback=traceback.format_exc()), 500

def run_flask():
    app.run(debug=True, use_reloader=False)

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
