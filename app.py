
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
        name, dob, birth_time, birth_place, question
    )

    return render_template(
        "index.html",
        result=reading,
        name=name
    )


def generate_reading(name, dob, birth_time, birth_place, question):
    name = name or "You"
    dob = dob or "Not provided"
    birth_time = birth_time or "Not provided"
    birth_place = birth_place or "Not provided"
    question = question or "your future"

    # Create a simple numerology-style number from DOB
    dob_digits = "".join(char for char in dob if char.isdigit())

    if dob_digits:
        birth_number = sum(int(digit) for digit in dob_digits)

        while birth_number > 9:
            birth_number = sum(
                int(digit) for digit in str(birth_number)
            )
    else:
        birth_number = 5

    personality_readings = {
        1: "You may be independent and enjoy taking initiative.",
        2: "You may value cooperation, patience and understanding.",
        3: "You may enjoy creativity, communication and learning.",
        4: "You may prefer structure, consistency and practical plans.",
        5: "You may enjoy variety, exploration and new experiences.",
        6: "You may value relationships, responsibility and harmony.",
        7: "You may be curious and enjoy deeper thinking.",
        8: "You may focus on achievement and long-term goals.",
        9: "You may value personal growth and helping others."
    }

    career_readings = {
        1: "Leadership and independent projects may interest you.",
        2: "Teamwork and coordination may suit your interests.",
        3: "Creative work, communication and technology may interest you.",
        4: "Technical, analytical and structured work may appeal to you.",
        5: "You may enjoy varied work and continuous learning.",
        6: "Management, design and people-focused work may interest you.",
        7: "Research, analysis and technology may appeal to you.",
        8: "Business, management and goal-oriented work may interest you.",
        9: "Communication, creativity and social impact may interest you."
    }

    question_lower = question.lower()

    if any(word in question_lower for word in [
        "career", "job", "work", "study", "college",
        "internship", "exam", "education", "placement"
    ]):
        question_response = (
            f"You asked: '{question}'. For career or studies, "
            "identify your goal, improve relevant skills, and make "
            "a realistic plan. Review your progress and explore "
            "opportunities that match your interests."
        )

    elif any(word in question_lower for word in [
        "love", "relationship", "marriage", "partner", "friend"
    ]):
        question_response = (
            f"You asked: '{question}'. In relationships, consider "
            "honest communication, mutual respect and how both "
            "people feel. Avoid assuming what someone thinks; "
            "a respectful conversation can provide clarity."
        )

    elif any(word in question_lower for word in [
        "money", "finance", "wealth", "business", "income"
    ]):
        question_response = (
            f"You asked: '{question}'. Consider your goals, budget, "
            "available options and risks. Planning and informed "
            "decisions are more dependable than predictions."
        )

    elif any(word in question_lower for word in [
        "health", "illness", "sick", "disease", "medicine"
    ]):
        question_response = (
            f"You asked: '{question}'. Astrology cannot diagnose "
            "illness or predict medical outcomes. For health "
            "concerns, consult a qualified healthcare professional."
        )

    elif any(word in question_lower for word in [
        "family", "parent", "mother", "father", "home"
    ]):
        question_response = (
            f"You asked: '{question}'. Calm communication, listening "
            "and understanding each other's perspectives may help. "
            "Focus on practical steps you can take."
        )

    elif any(word in question_lower for word in [
        "travel", "trip", "journey", "abroad"
    ]):
        question_response = (
            f"You asked: '{question}'. Consider your destination, "
            "budget, schedule, safety and travel requirements "
            "when deciding your next steps."
        )

    else:
        question_response = (
            f"You asked: '{question}'. Use this astrology-style "
            "reading for reflection, not as a guaranteed prediction. "
            "Consider what you know, what remains uncertain, and "
            "what practical step you can take next."
        )

    return {
        "personality": (
            f"{name}, based on the details you entered "
            f"({dob}, {birth_time}, {birth_place}), your "
            f"astrology-style personality reading suggests: "
            f"{personality_readings[birth_number]}"
        ),

        "past": (
            "Your past experiences may have helped shape your "
            "interests, perspective and personal development. "
            "Reflect on what you have learned from them."
        ),

        "career": career_readings[birth_number],

        "relationships": (
            "Open communication, respect and understanding can "
            "help build healthy relationships. Your choices and "
            "circumstances matter."
        ),

        "future": (
            "Your future depends on many factors, including your "
            "decisions, effort and circumstances. Learning, planning "
            "and adapting can help you prepare for opportunities."
        ),

        "question": question_response
    }


if __name__ == "__main__":
    app.run(debug=True)
