from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/crop-health', methods=['GET'])
def get_crop_health():
    # logic to fetch crop health status
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True)
