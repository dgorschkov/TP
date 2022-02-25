from flask import Flask, redirect, abort

from data.news import News
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    app.run()



@app.route('/news_delete/<int:id>', methods=['GET', 'POST'])
def news_delete(id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.id == id).first()
    if news:
        db_sess.delete(news)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.errorhandler(404)
def page_not_found():
    return '<h1>Данной страницы нет, не было и не будет</h1>'


if __name__ == '__main__':
    main()
