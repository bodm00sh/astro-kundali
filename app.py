from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    name = request.form.get("name")
    dob = request.form.get("dob")
    birth_time = request.form.get("birth_time")
    birth_place = request.form.get("birth_place")
    question = request.form.get("question")

    # Basic astrology-style reading
    reading = generate_reading(
        name,
        dob,
        birth_time,
        birth_place,
        question
    )

    return render_template(
        "index.html",
        result=reading,
        name=name
    )


def generate_reading(name, dob, birth_time, birth_place, question):

    return {
        "personality": (
            f"{name}, your birth details suggest an astrology-style "
            "personality reading focused on curiosity, learning and "
            "personal development. You may experience different phases "
            "where your priorities change significantly."
        ),

        "past": (
            "Your past reading indicates that your earlier years may "
            "have included periods of learning, adjustment and changes "
            "in your interests. Some experiences may have influenced "
            "the way you approach your future decisions."
        ),

        "career": (
            "Your career theme points toward continuous learning and "
            "developing practical skills. Fields involving technology, "
            "analysis, communication or problem solving may be interesting "
            "areas to explore."
        ),

        "relationships": (
            "Relationships may become more meaningful when there is "
            "honest communication and mutual understanding. Different "
            "phases of life can bring changes in social connections."
        ),

        "future": (
            "The coming period can be viewed as a phase of exploration "
            "and gradual development. New opportunities may appear, but "
            "their outcome will depend heavily on your own decisions, "
            "effort and circumstances."
        ),

        "question": question
    }


if __name__ == "__main__":
    app.run(debug=True)