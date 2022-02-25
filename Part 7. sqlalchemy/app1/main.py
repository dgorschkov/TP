# noinspection PyUnresolvedReferences
from data.news import News
# noinspection PyUnresolvedReferences
from data.users import User
# noinspection PyUnresolvedReferences
from data import db_session


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()

    user = User()
    user.name = "Пользователь 1"
    user.about = "биография пользователя 1"
    user.email = "email9999@email.ru"
    db_sess.add(user)

    user2 = User()
    user2.name = "Пользователь 2"
    user2.about = "биография пользователя 2"
    user2.email = "email2@email.ru"
    db_sess.add(user2)

    user3 = User()
    user3.name = "Пользователь 3"
    user3.about = "биография пользователя 3"
    user3.email = "333@email.ru"
    db_sess.add(user3)

    db_sess.commit()
    print(user.id)


    user = db_sess.query(User).first()
    print(user.name)
    print()
    for user in db_sess.query(User).all():
        print(user)
    print()
    for user in db_sess.query(User).filter(User.id > 1, User.email.notilike("%1%")):
        print(user)
    print()
    db_sess.query(User).filter(User.id >= 2).delete()
    db_sess.commit()

    user = db_sess.query(User).first()
    user.name = 'Суперпользователь'
    db_sess.merge(user)
    db_sess.commit()



    news = News(title="Первая новость", content="Привет блог!", user_id=1, is_private=False)
    db_sess.add(news)
    db_sess.commit()

    user = db_sess.query(User).filter(User.id == 1).first()
    news = News(title="Вторая новость", content="Уже вторая запись!", user=user, is_private=False)
    db_sess.add(news)
    db_sess.commit()

    news = News(title="Третья новость", content="Уже третья запись!", is_private=False)
    user.news.append(news)
    db_sess.merge(user)
    db_sess.commit()


    for news in user.news:
        print(news)


if __name__ == '__main__':
    main()
