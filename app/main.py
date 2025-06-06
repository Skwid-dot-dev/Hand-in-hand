from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    scenario_title = "How to Make a Cup of Tea"
    steps = [
        "Boil water.",
        "Put a tea bag in a cup.",
        "Pour the hot water into the cup.",
        "Let the tea steep for 3-5 minutes.",
        "Remove the tea bag.",
        "Add milk or sugar if desired."
    ]
    return render_template('index.html', scenario_title=scenario_title, steps=steps)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
