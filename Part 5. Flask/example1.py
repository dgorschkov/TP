from flask import Flask, url_for, request

app = Flask(__name__)






@app.route('/')
@app.route('/index/')
def index():
    return "<h1>Привет, Яндекс!</h1><br>\n<h1>Привет, Яндекс!</h1>"













@app.route('/countdown/')
def countdown():
    countdown_list = [str(x) for x in range(10, 0, -1)]
    countdown_list.append('Пуск!')
    return '\n<br>\n'.join(countdown_list)


@app.route('/image_sample/')
def image():
    return f'''<img src="{url_for('static', filename='img/riana.jpg')}" alt="здесь изображена сова Рианна">'''

@app.route('/sample_page/')
def return_sample_page():
    return f'''
<!doctype html>
<html lang="ru">
  <head>
    <meta charset="utf-8">
    <title>Привет, Яндекс!</title>
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
  </head>
  <body>
    <h1>Первая HTML-страница</h1>
  </body>
</html>
'''


@app.route('/bootstrap_sample/')
def bootstrap():
    return f'''
<!doctype html>
<html lang="ru">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" 
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
        crossorigin="anonymous">
        <title>Привет, Яндекс!</title>
    </head>
    <body>
        <h1>Привет, Яндекс!</h1>
        <div class="alert alert-primary" role="alert">
            А мы тут компонентами Bootstrap балуемся
        </div>
    </body>
</html>'''


i = 0
@app.route('/i/')
def show_i():
    global i
    i += 1
    return str(i)



# @app.route('/greeting/<username>')
@app.route('/greeting/<username>/')
@app.route('/greeting/')
def greeting(username='anonymus'):
    return f'''<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Привет, {username}</title>
                  </head>
                  <body>
                    <h1>Привет, {username}!</h1>
                  </body>
                </html>'''


@app.route('/two_params/<username>/<int:number>/')
# @app.route('/two_params/<username>')
@app.route('/two_params/<username>/')
def two_params(username, number=1):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" 
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
        crossorigin="anonymous">
                    <title>Пример с несколькими параметрами</title>
                  </head>
                  <body>
                    <h2>{username}</h2>
                    <div>Это первый параметр и его тип: {str(type(username))[1:-1]}</div>
                    <h2>{number}</h2>
                    <div>Это второй параметр и его тип: {str(type(number))[1:-1]}</div>
                  </body>
                </html>'''




@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''
<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" 
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
        crossorigin="anonymous">
<link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
<title>Пример формы</title>
</head>
<body>
<h1>Форма для регистрации в суперсекретной системе</h1>
<div>
    <form class="login_form" method="post">
        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
        <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
        <div class="form-group">
            <label for="classSelect">В каком вы классе</label>
            <select class="form-control" id="classSelect" name="class">
              <option>7</option>
              <option>8</option>
              <option>9</option>
              <option>10</option>
              <option>11</option>
            </select>
         </div>
        <div class="form-group">
            <label for="about">Немного о себе</label>
            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
        </div>
        <div class="form-group">
            <label for="photo">Приложите фотографию</label>
            <input type="file" class="form-control-file" id="photo" name="file">
        </div>
        <div class="form-group">
            <label for="form-check">Укажите пол</label>
            <div class="form-check" id="form-check">
              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
              <label class="form-check-label" for="male">
                Мужской
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
              <label class="form-check-label" for="female">
                Женский
              </label>
            </div>
        </div>
        <div class="form-group form-check">
            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
            <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
        </div>
        <button type="submit" class="btn btn-primary">Записаться</button>
    </form>
</div>
</body>
</html>
'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        if 'accept' in request.form:
            print(request.form['accept'])
        print(request.form['sex'])
        return "<h1>Форма отправлена</h1>"

@app.route('/sample_file_upload', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример загрузки файла</title>
                          </head>
                          <body>
                            <h1>Загрузим файл</h1>
                            <form method="post" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="photo">Выберите файл</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        print(f.read())
        return "Форма отправлена"










if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
