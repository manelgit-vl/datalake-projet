from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    try:
        df = pd.read_parquet('../Data_lake/gold/final_dataset')
        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
