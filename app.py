from flask import Flask, redirect, render_template, request


app = Flask(__name__)


colors = {
    0: "#ff00ff",
    1: "#ffff00",
    2: "#00ff00",
    3: "#00ffff",
}


if __name__ == "__main__":
    app.run()
