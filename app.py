from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='DJproject')

# 허가된 사용자 목록 (예시)
AUTHORIZED_USERS = {'K': '1234', 'J': '1234', 'S': '1234', 'L': '1234'}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in AUTHORIZED_USERS and AUTHORIZED_USERS[username] == password:
            return render_template('dataindex.html', username=username)
        else:
            return render_template('index.html', error='인증 실패. 다시 시도해주세요.')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
