from flask import Flask, redirect, render_template, request


app = Flask(__name__)


colors = {
    0: "#ff00ff",
    1: "#ff921e",
    2: "#00ff00",
    3: "#00ffff",
}


@app.route("/")
def main():
    return render_template("index.html", colors=colors)


@app.route("/picker")
def picker():
    square = int(request.args.get("square", 0))
    return render_template("picker.html", square=square, colors=colors)


@app.route("/update_color", methods=["POST"])
def update():
    square = int(request.form.get("square"))
    color = request.form.get("color")
    colors[square] = color

    return redirect("/")


if __name__ == "__main__":
    app.run()
