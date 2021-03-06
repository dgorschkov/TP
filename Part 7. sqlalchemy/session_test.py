from flask import Flask, request, make_response, session
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=30)


def main():
    app.run()


@app.route("/session_test/")
def session_test():
    visits_count = session.get('visits_count', 0)
    session['visits_count'] = visits_count + 1
    return make_response(f"Вы пришли на эту страницу {visits_count + 1} раз")


if __name__ == '__main__':
    main()
