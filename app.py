from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index')
def hello():
    return "Hello, World!"


@app.route("/user/<username>")
def user_profile(username):
    return f"Trang cá nhân của {username}"

@app.route('/chia_nhom')
def chia_nhom():
    so_bai = 12
    so_nhom = 0
    if so_nhom > 0:
        return f"Mỗi nhóm làm {so_bai / so_nhom} bài"
    else:
        return "Không có nhóm nào để chia bài."


@app.route('/square/<int:number>')
def square(number):
    return f"Bình phương của {number} là {number ** 2}"

@app.route('/sum/<number>')
def total(number):
    try:
        num_list = [float(n.strip()) for n in number.split(',')]
        total = sum(num_list)
        return f"Tổng của {num_list} là {total}"
    except ValueError:
        return "404"

if __name__ == '__main__':
    app.run(debug=True)