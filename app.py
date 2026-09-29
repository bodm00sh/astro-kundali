from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    name = request.form.get("name", "").strip()
    dob = request.form.get("dob", "").strip()
    birth_time = request.form.get("birth_time", "").strip()
    birth_place = request.form.get("birth_place", "").strip()
    question = request.form.get("question", "").strip()

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

    # Simple dynamic logic based on user's inputs
    name = name if name else "You"
    birth_place = birth_place if birth_place else "your birthplace"
    question = question if question else "your future"

    # Create a simple number from DOB
    dob_digits = "".join(c for c in dob if c.isdigit())

    if dob_digits:
        birth_number = sum(int(digit) for digit in dob_digits)

        while birth_number > 9:
            birth_number = sum(int(digit) for digit in str(birth_number))
    else:
        birth_number = 5

    personality_readings = {
        1: "You may have an independent nature and often prefer taking initiative rather than waiting for others.",
        2: "You may value cooperation, patience and emotional understanding in your interactions with others.",
        3: "You may have a creative side and enjoy expressing ideas through communication, learning or new experiences.",
        4: "You may prefer structure, consistency and practical approaches when working toward your goals.",
        5: "You may enjoy variety, exploration and learning through different experiences.",
        6: "You may place importance on relationships, responsibility and maintaining harmony with people around you.",
        7: "You may be naturally curious and interested in understanding things more deeply before making decisions.",
        8: "You may be strongly focused on achievement, progress and building something meaningful over time.",
        9: "You may have a broad outlook and may be drawn toward experiences that involve helping, learning or personal growth."
    }

    career_readings = {
        1: "Your career theme can be explored through leadership, independent projects and taking responsibility.",
        2: "Work involving teamwork, coordination and communication may suit your interests.",
        3: "Creative, communication and technology-related areas may provide interesting opportunities to explore.",
        4: "Technical, analytical and structured fields may be worth exploring as you develop your skills.",
        5: "You may enjoy careers that offer variety, technology, communication or opportunities to learn new things.",
        6: "People-oriented work, management, design or service-related areas may be interesting to explore.",
        7: "Research, analysis, technology and areas requiring deeper thinking may appeal to you.",
        8: "Business, management, technology and goal-oriented professional paths may interest you.",
        9: "Fields involving communication, creativity, social impact or broad experiences may appeal to you."
    }

    question_lower = question.lower()

    if any(word in question_lower for word in ["career", "job", "work", "study", "college"]):
        question_response = (
            f"Regarding your question about career or studies, {name}, "
            f"your reading suggests focusing on consistent skill development "
            f"and making decisions based on your actual interests and opportunities."
        )

    elif any(word in question_lower for word in ["love", "relationship", "marriage"]):
        question_response = (
            f"Regarding your relationship question, {name}, "
            f"communication, mutual respect and understanding are important "
            f"factors to consider. Your circumstances and choices will shape "
            f"how relationships develop."
        )

    elif any(word in question_lower for word in ["money", "finance", "wealth", "business"]):
        question_response = (
            f"Regarding your financial question, {name}, "
            f"the reading points toward gradual development through planning, "
            f"learning and responsible decisions rather than relying only on luck."
        )

    else:
        question_response = (
            f"Regarding your question, '{question}', "
            f"this astrology-style reading suggests looking at the situation "
            f"with patience and considering both opportunities and practical circumstances."
        )

    return {
        "personality": (
            f"{name}, based on the birth details you entered "
            f"({dob}, {birth_time}, {birth_place}), your astrology-style "
            f"personality reading suggests: {personality_readings[birth_number]}"
        ),

        "past": (
            f"Your past reading suggests that experiences connected with "
            f"learning, changing interests and personal development may have "
            f"played an important role in shaping your current outlook."
        ),

        "career": career_readings[birth_number],

        "relationships": (
            f"For relationships, {name}, open communication and mutual "
            f"understanding can be important. Different stages of life may "
            f"bring changes in your social connections."
        ),

        "future": (
            f"Your future reading suggests a period of gradual development. "
            f"New opportunities may come through learning and experience, "
            f"but the actual outcome will depend on your decisions, effort "
            f"and circumstances."
        ),

        "question": question_response
    }


if __name__ == "__main__":
    app.run(debug=True)