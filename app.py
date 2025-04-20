# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from summary_generator import SummaryGenerator

app = Flask(__name__)
CORS(app)  # Enable CORS to allow communication with React frontend

# Initialize the summarizer
summarizer = SummaryGenerator("best_model.pt")

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text', '')
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    try:
        summary = summarizer.summarize(text)
        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)