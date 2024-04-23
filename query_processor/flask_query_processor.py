# flask_query_processor.py
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the index from a pickle file or initialize if not available
def load_index():
    try:
        with open('index.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {'python': {0, 1}, 'language': {0, 1}, 'great': {0, 2}}

index = load_index()

# Route to handle search queries via GET method
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    if not query:
        return jsonify({'error': 'Query parameter is missing'}), 400

    # Split the query into words and search for each word in the index
    query_words = query.lower().split()
    results = set()
    for word in query_words:
        if word in index:
            if not results:
                results.update(index[word])
            else:
                results.intersection_update(index[word])  # Returns results common to all query words
        else:
            # If one word is not found, return an empty set for that word
            return jsonify({'results': [], 'message': f'No entries found for the word: {word}'}), 404

    return jsonify({'results': list(results)})

# Route to save or update the index
@app.route('/update_index', methods=['POST'])
def update_index():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    global index
    index.update(data)
    # Save the updated index to a file
    with open('index.pkl', 'wb') as f:
        pickle.dump(index, f)
    return jsonify({'message': 'Index updated successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
