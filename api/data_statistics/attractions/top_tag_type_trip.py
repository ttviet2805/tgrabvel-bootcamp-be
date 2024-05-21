import json
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

# Hàm để đọc tệp JSON
def read_json_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found.")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return []

# Hàm để tính toán tổng score cho mỗi type_trip của tag "Spas"
def calculate_scores_by_trip_type_for_spas(data):
    trip_type_scores = {}
    for attraction in data:
        if "Spas" in attraction['tag_split']:
            for review in attraction['review']:
                trip_type = review['type_trip'].strip()
                if trip_type:
                    if trip_type not in trip_type_scores:
                        trip_type_scores[trip_type] = 0
                    score = review['score'] - 50
                    trip_type_scores[trip_type] += score
    return trip_type_scores

# Hàm để vẽ biểu đồ tròn
def plot_pie_chart(trip_type_scores, title):
    trip_types = list(trip_type_scores.keys())
    scores = list(trip_type_scores.values())
    colors = plt.cm.tab20(np.linspace(0, 1, len(trip_types)))

    fig, ax = plt.subplots(figsize=(12, 8))
    wedges, texts, autotexts = ax.pie(scores, labels=trip_types, autopct='%1.1f%%', startangle=140, colors=colors)

    # Create legend
    ax.legend(wedges, trip_types, title="Trip Types", loc="center left", bbox_to_anchor=(1, 0.5))

    plt.setp(autotexts, size=10, weight="bold")
    ax.set_title(title)

    plt.show()

# Main execution
data = read_json_file('score_reviews.json')

# Calculate scores by trip type for tag "Spas"
trip_type_scores = calculate_scores_by_trip_type_for_spas(data)

# Plot pie chart for trip types for tag "Spas"
plot_pie_chart(trip_type_scores, 'Trip Type Distribution for Spas')
