from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"}
]

# GET /api/items
@app.route("/api/items", methods=["GET"])
def get_items():
    return jsonify(data)

# GET /api/items/<id>
@app.route("/api/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((item for item in data if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

# POST /api/items
@app.route("/api/items", methods=["POST"])
def create_item():
    new_item = request.get_json()
    new_item["id"] = len(data) + 1
    data.append(new_item)
    return jsonify(new_item), 201

# PUT /api/items/<id>
@app.route("/api/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = next((item for item in data if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    updated_data = request.get_json()
    item.update(updated_data)
    return jsonify(item)

# DELETE /api/items/<id>
@app.route("/api/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global data
    data = [item for item in data if item["id"] != item_id]
    return jsonify({"message": "Item deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
