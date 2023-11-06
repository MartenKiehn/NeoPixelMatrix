from flask import Flask, request, render_template

app = Flask("LED Matrix")

# Eine globale Variable, um die LED-Matrix-Daten zu speichern
led_matrix_data = []


# Routen zur Anzeige der HTML-Seite und zum Empfangen der JSON-Daten
@app.route('/')
def index():
    return render_template('index2.html')


@app.route('/receive_matrix', methods=['POST'])
def receive_matrix():
    try:
        matrix_json = request.get_json()
        # Überprüfen, ob die empfangenen Daten gültig sind, bevor sie gespeichert werden
        if isinstance(matrix_json, list):
            global led_matrix_data
            led_matrix_data = matrix_json
            print(led_matrix_data)
            return "LED Matrix data received successfully", 200
        else:
            return "Invalid LED Matrix data", 400
    except Exception as e:
        return str(e), 500


if __name__ == '__main__':
    app.run(debug=True)
