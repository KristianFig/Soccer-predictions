from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_team_names')
def get_team_names():
    response = jsonify({
        'teams': util.get_team_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_winner', methods=['GET', 'POST'])
def predict_winner():
    if request.method == 'POST':
        team_1 = request.form.get('team_1')
        team_2 = request.form.get('team_2')
    else:
        team_1 = request.args.get('team_1')
        team_2 = request.args.get('team_2')

    if not team_1 or not team_2:
        return jsonify({'error': 'Please provide both team_1 and team_2'}), 400

    try:
        winner = util.get_winner_team(team_1, team_2)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    response = jsonify({
        'winner_of_match': winner
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Team Prediction...")
    util.load_saved_artifacts()
    app.run()