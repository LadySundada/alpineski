import xlrd
from flask import Flask, request, url_for, redirect
from flask import render_template
from flask import jsonify

app = Flask(__name__)

def calc_info(player):
    laps = 59
    xl = xlrd.open_workbook(r'times.xlsx')
    table = xl.sheets()[0]
    start = (player - 1) * laps + 1
    end = start + laps
    col1 = table.col_values(1, start, end)
    col2 = [round(i, 3) for i in table.col_values(4, start, end)]
    xydata = {"xData": col1, "yData": col2}

    movies = []
    for i in range(laps):
        name = "rank" + str(player) + "_" + str(i + 1)
        ball = {'file': name + '.mp4', 'title': "第" + str(i + 1) + "圈：\t" + str(col2[i]) + "s"}
        movies.append(ball)

    xl = xlrd.open_workbook(r'information.xls')
    table = xl.sheets()[0]
    names = table.col_values(1)
    genders = table.col_values(2)
    fiscodes = table.col_values(3)
    ages = table.col_values(5)
    nations = table.col_values(6)
    pictures = table.col_values(7)
    info = {'name': names[player], 'gender': str(genders[player]), 'fiscode': int(fiscodes[player]),
            'age': int(ages[player]), 'nation': str(nations[player]),
            'picture': str(pictures[player]), "rank": int(player - 1)}
    return movies, xydata, info

@app.route('/', methods=['GET', 'POST'])
def movie_list():
    movies, xydata, info = calc_info(1)
    return render_template("index.html", movies=movies, xydata=xydata, info=info)


@app.route('/<int:player>', methods=['GET', 'POST'])
def player(player):
    movies, xydata, info = calc_info(player)
    return render_template("index.html", movies=movies, xydata=xydata, info=info)




if __name__=='__main__':
  app.run()