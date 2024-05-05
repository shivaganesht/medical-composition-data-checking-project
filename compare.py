from flask import Flask, render_template, request
from Medicine import Medicine, compare_composition

app = Flask(__name__)

# Predefined medicines with their compositions
predefined_medicines = [
    Medicine("Medicine 1", "cipla", ["paracetamol", "ibuprofen", "calcium"], ["vomiting", "rashes"], "fever",
             "50"),
    Medicine("Medicine 2", "microlabs", ["aspirin", "calcium", "paracetamol"], ["vomiting", "rashes"], "fever",
             "50"),
    Medicine("Medicine 3", "cipla", ["vitamin c", "iron"], ["vomiting", "rashes"], "fever", "50"),
    # Add more predefined medicines as needed
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    user_input = request.form['composition']
    user_composition = [x.strip().lower() for x in user_input.split(',')]
    matches = []
    for med in predefined_medicines:
        if any(comp.lower() in user_composition for comp in med.compositions):
            matches.append(med)
    return render_template('result.html', matches=matches)


if __name__ == '__main__':
    app.run(debug=True)