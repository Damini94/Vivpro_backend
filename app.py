from flask import Flask, jsonify, request
from utils import data_utils
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# Sample normalized data (you can replace this with your actual data)
normalized_data = data_utils.normalize_data()


@app.route('/api/songs', methods=['GET'])
def get_all_songs():
    page = int(request.args.get('page', 1))  # Get page number from query parameters (default to 1)
    page_size = int(request.args.get('page_size', 10))  # Get page size from query parameters (default to 10)

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    paginated_data = normalized_data[start_index:end_index]

    return jsonify(paginated_data)


@app.route('/api/songs/<title>', methods=['GET'])
def get_song_by_title(title):
    # Find a song by title
    for song in normalized_data:
        if song['title'] == title:
            return jsonify(song)
    return jsonify({'error': 'Song not found'}), 404


@app.route('/api/songs/<song_id>/rate', methods=['POST'])
def rate_song(song_id):
    rating = request.json.get('rating')  # Assuming the client sends the rating in JSON format

    for song in normalized_data:
        if song['id'] == song_id:
            song['rating'] = rating
            return jsonify({'message': 'Rating updated successfully'}), 200

    return jsonify({'error': 'Song not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
