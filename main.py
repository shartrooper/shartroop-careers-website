from flask import Flask, render_template

app = Flask(__name__)

GAMES = [
    {
        "home_team.name": "Mavericks",
        "visitor_team.name": "Spurs",
        "period": 4,
        "home_team_score": 117,
        "visitor_team_score": 138,
        "time": "Final",
        "status": "Final",
        "season": 2022,
        "id": 858571,
    },
    {
        "home_team.name": "Nuggets",
        "visitor_team.name": "Kings",
        "period": 4,
        "home_team_score": 109,
        "visitor_team_score": 95,
        "time": "Final",
        "status": "Final",
        "season": 2022,
        "id": 858581,
    },
    {
        "home_team.name": "Timberwolves",
        "visitor_team.name": "Pelicans",
        "period": 4,
        "home_team_score": 113,
        "visitor_team_score": 108,
        "time": "Final",
        "status": "Final",
        "season": 2022,
        "id": 858578,
    },
    {
        "home_team.name": "Suns",
        "visitor_team.name": "Clippers",
        "period": 4,
        "home_team_score": 114,
        "visitor_team_score": 119,
        "time": "Final",
        "status": "Final",
        "season": 2022,
        "id": 858584,
    },
]


@app.route("/")
def hello_world():
    return render_template('home.html', games=GAMES)


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
