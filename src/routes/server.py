from flask import Flask, request, jsonify
from models.agent import SportAI
from utils.config import Config

app = Flask(__name__)
config = Config()
agent = SportAI(config)

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    result = agent.predict(data)
    return jsonify({"prediction": result})

@app.route('/api/training/recommend', methods=['GET'])
def recommend_training():
    user_id = request.args.get('user_id')
    recommendations = agent.get_recommendations(user_id)
    return jsonify({"recommendations": recommendations})

@app.route('/api/training/log', methods=['POST'])
def log_training():
    training_data = request.json
    agent.log_training_session(training_data)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
