from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    tables = {}

    for num in range(2, 11):
        tables[num] = []

        for i in range(1, 11):
            tables[num].append(
                f"{num} x {i} = {num*i}"
            )

    return render_template(
        "index.html",
        tables=tables
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000
    )
