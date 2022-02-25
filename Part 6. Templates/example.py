from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)



@app.route('/')
def index0():
    return render_template('tmp.html', title='Title', username='USER')



@app.route('/index/')
def index():
    data = {
        'title': 'Title',
        'username': 'USER',
    }
    return render_template('tmp2.html', **data)





@app.route('/odd_even/')
def odd_even():
    return render_template('odd_even.html', number=10)





@app.route('/news/')
def news():
    news_list = {
                "news": [
                    {
                        "title": "Сегодня хорошая погода",
                        "content": "Невероятно, сегодня хорошая погода"
                    },
                    {
                        "title": "Завтра хорошая погода",
                        "content": "С ума сойти, и завтра хорошая погода"
                    },
                    {
                        "title": "Послезавтра дождь",
                        "content": "Все вошло в норму"
                    }
                ]
            }
    # print(news_list)
    return render_template('news.html', news=news_list)




@app.route('/test_page/<title>/')
@app.route('/test_page/')
# test_page(title='Заголовок')
def tst_page(title='Заголовок'):
    return render_template('test_page.html', title=title)


@app.route('/base/')
# test_page(title='Заголовок')
def base_page():
    return render_template('base.html', title='Базовый заголовок')




from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email


app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
        print(form.remember_me.data)
        return redirect('/success/')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success/')
def success():
    return '<h1>Авторизация прошла успешно</h1>'

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')