from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
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
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="study_level">
                                          <option>Начальное</option>
                                          <option>Основное</option>
                                          <option>Среднее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее образование</option>
                                        </select>
                                     </div>
                                     <div class="form-group">
                                        <label for="form-check">Какие у Вас есть профессии?</label>
                                        <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="hz">
                                        <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                                        </div>
                                        <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="hz">
                                        <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
                                        </div>
                                        <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="hz">
                                        <label class="form-check-label" for="acceptRules">Пилот</label>
                                        </div>
                                        <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="hz">
                                        <label class="form-check-label" for="acceptRules">Метеоролог</label>
                                        </div>
                                        <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="hz">
                                        <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечению</label>
                                        </div>
                                        <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="hz">
                                        <label class="form-check-label" for="acceptRules">Инженер по радиоционной защите</label>
                                        </div>
                                        <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="hz">
                                        <label class="form-check-label" for="acceptRules">Врач</label>
                                        </div>
                                        <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="hz">
                                        <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="Юлия Викторовна" value="Юлия Викторовна">
                                          <label class="form-check-label" for="Юлия Викторовна">
                                            Юлия Викторовна
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="Я ещё не определилось" value="ещё не определилось с полом" checked>
                                          <label class="form-check-label" for="ещё не определилось с полом">
                                            Я ещё не определилось
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="мужчина" value="мужчина">
                                          <label class="form-check-label" for="мужчина">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="женщина" value="женщина">
                                          <label class="form-check-label" for="женщина">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="why" rows="4" name="why"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                      <div class="form-group">
                                        <label for="form-check">Готовы остаться на Марсе?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="готовы" id="готовы" value="готовы">
                                          <label class="form-check-label" for="готовы">
                                            готовы
                                          </label>
                                        </div>
                                     </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>

                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['study_level'] + 'образование')
        if request.form['hz'] == 'on':
            print('какая-то профессия есть')
        print(request.form['sex'])
        print(request.form['why'])
        print(request.form['готовы!!!'])
        print(request.form['file'])
        return "Форма отправлена Фираюшкеее"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')