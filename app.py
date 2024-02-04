from flask import Flask, request, render_template, jsonify, session
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ABC'
boggle_game = Boggle()

@app.route('/')
def homepage():
    board = boggle_game.make_board()
    session['board'] = board
    return render_template('index.html', board=board)

@app.route('/check-word')
def check_word():
    word = request.args.get('word', '')
    board = session.get('board', [])
    result = boggle_game.check_valid_word(board, word)
    return jsonify({'result': result})

@app.route('/post-score', methods=["POST"])
def post_score():
    score = request.json.get('score', 0)
    return jsonify({'result': 'success'})

if __name__ == "__main__":
    app.run(debug=True)
