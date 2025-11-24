from flask import Flask, redirect, render_template, request  # basic imports


app = Flask(__name__)  # flask boilerplate


## Our list of colors

colors = {
    0: "#ff00ff",
    1: "#ff921e",
    2: "#00ff00",
    3: "#00ffff",
}


@app.route("/")  # on the / route
def main():  # do this function
    return render_template(
        "index.html",  # return the index.html file in templates/
        colors=colors,  # with all instances of {{colors}} replaced with the actual colors dictionary
    )


@app.route("/picker")  # on the picker route
def picker():  # do this function
    square = int(
        request.args.get("square", 0)
    )  # get X as an integer from /picker?square=X
    return render_template(
        "picker.html", square=square, colors=colors
    )  # same thing as before, with square passed, too


@app.route(
    "/update_color", methods=["POST"]
)  # ONLY on submissions from the form at the update_color route
def update():
    square = int(
        request.form.get("square")
    )  # get the form response of the square number
    color = request.form.get("color")  # get the form response of the color
    colors[square] = color  # change the dictionary value to the new color

    return redirect("/")  # go back to the home page


if __name__ == "__main__":
    app.run()
