# data_utils.py

import json
import csv


def write_to_csv(normalized_data):
    with open("../static/normalised_data.csv", 'w', newline='') as csvfile:
        fieldnames = ['index', 'id', 'title', 'danceability', 'energy', 'mode', 'acousticness', 'tempo', 'duration_ms',
                      'num_sections', 'num_segments']  # Add more fieldnames as needed
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(normalized_data)
    print("file written")

def normalize_data(json_file = "C:/Users/damin/PycharmProjects/VIVPRO_PROJECT/static/songs.json"):
    with open(json_file, 'r') as file:
        data = json.load(file)

    normalized_data = []
    for i, song_id in data['id'].items():
        song = {
            'index': i,
            'id': song_id,
            'title': data['title'][i],  # Assuming 'title' is the attribute name for the song title
            'danceability': data['danceability'][i],
            'energy': data['energy'][i],
            'mode': data['mode'][i],
            'acousticness': data['acousticness'][i],
            'tempo': data['tempo'][i],
            'duration_ms': data['duration_ms'][i],
            'num_sections': data['num_sections'][i],
            'num_segments': data['num_segments'][i],
            'rating': None

        }
        normalized_data.append(song)
    # write_to_csv(normalized_data)

    return normalized_data
if __name__== "__main__":
    print("hi")
    normalize_data(json_file = "C:/Users/damin/PycharmProjects/VIVPRO_PROJECT/static/songs.json")
    print("done")