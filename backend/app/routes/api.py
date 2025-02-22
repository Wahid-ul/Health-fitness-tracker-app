from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required  # ✅ Import this
from app.modules.rust_ai import run_rust_ai

api_bp = Blueprint("api", __name__)

@api_bp.route("/api/predict", methods=["OPTIONS"])
@cross_origin()
def handle_options():
    return jsonify({"message": "CORS preflight successful"}), 200

@api_bp.route("/api/predict", methods=["POST"])
@jwt_required()  # ✅ Requires authentication
@cross_origin()
def predict():
    try:
        input_data = request.json
        result = run_rust_ai(input_data)
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_bp.route("/api/user", methods=["GET"])
@jwt_required()  # ✅ Requires authentication
def get_user():
    try:
        # Get the user ID from the JWT token
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        if not user:
            return jsonify({"error": "User not found"}), 404

        # Return user details (excluding password)
        return jsonify({
            "id": user.id,
            "name": user.name,
            "email": user.email
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500