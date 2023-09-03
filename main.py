from flask import Flask, Markup

def fib(n):
    fib_1 = fib_2 = 1
    fib_list = [1, 1]
    for i in range(2, n):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        fib_list.append(fib_2)
    return ', '.join(map(str, fib_list))


def create_tree(n):
    picture_list = []
    base = n * 2
    trunk = '.' * (base - 1) + '|.|' + '.' * (base - 1)
    for i in range(0, n):

        picture_list.append('.' * base + (',.' if i == 0 else ',' + ',' * i * 2) + '.' * (base - 1 if i == 0 else base))
        base -= 1
    picture_list.append(trunk)
    return '<br>'.join(picture_list)




app = Flask(__name__)


@app.route('/index')
def index():
    return 'Hellow world !!!'

@app.route('/fibonachi')
@app.route('/fibonachi<num>')
def fibonachi(num = '2'):
    if not num.isdigit():
        return 'Чиселку суй брат'
    num = int(num)
    num = 2 if num <= 2 else num
    return fib(num)


@app.route('/tree')
@app.route('/tree<num>')
def tree(num='3'):
    if not num.isdigit():
        return 'Ну братик блин, тут нужна чиселка (('
    num = int(num)
    num = 3 if num <= 3 else num
    return Markup(create_tree(num))



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')