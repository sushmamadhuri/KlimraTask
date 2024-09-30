from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 
records = []

@app.route('/record', methods=['POST'])
def post_record():
    data = request.json
    record = data.get('record')
    
    if record:
        records.append(record)
        return jsonify({"message": "Record added successfully!"})
    else:
        return jsonify({"error": "No record provided"})




@app.route('/record', methods=['GET'])
def get_record():
    if records:
        return jsonify({"last_record": records[-1]})
    else:
        return jsonify({"message": "No records found"})



if __name__ == '__main__':
    app.run(debug=True)
