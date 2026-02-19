from flask import Flask, request, jsonify

def create_app():
    app = Flask(__name__)

    students = []

    @app.route("/")
    def home():
        return {"message": "Backend Server is running"}

    @app.route("/students", methods=["GET"])
    def get_students():
        return jsonify(students)

    @app.route("/students", methods=["POST"])
    def add_student():
        data = request.get_json()
        students.append(data)
        return jsonify({"message": "Student added"}), 201

    return app

app = create_app()
