from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    table = []

    if request.method == "POST":
        number = int(request.form["number"])

        for i in range(1, 11):
            table.append(f"{number} x {i} = {number * i}")

    return render_template("index.html", table=table)

if __name__ == "__main__":
    app.run(debug=True)