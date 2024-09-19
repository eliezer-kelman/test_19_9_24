from flask import Flask, jsonify, request
from repository.games_repository import find_all_2022
from controllers.home_controller import run_app, get_players_by_position
from dataclasses import asdict

app = Flask(__name__)


@app.route('/api/players', methods=['GET'])
def get_players():
    req = request.args
    flayers = get_players_by_position(req.get('position'))
    return jsonify(asdict(flayers), 200)


if __name__ == '__main__':
    run_app()
    app.run(debug=True)
