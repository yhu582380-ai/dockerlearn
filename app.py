"""Flask 后端：提供冒泡排序 API 并托管前端页面"""
import os
from flask import Flask, request, jsonify, send_from_directory

from maopao import bubble_sort

ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)


@app.route("/")
def index():
    return send_from_directory(os.path.join(ROOT, "templates"), "index.html")


@app.route("/api/sort", methods=["POST"])
def sort():
    data = request.get_json()
    if not data or "numbers" not in data:
        return jsonify({"error": "请提供 numbers 数组"}), 400
    nums = data["numbers"]



    if len(nums) != 10:
        return jsonify({"error": "请提供恰好 10 个数字"}), 400
    try:
        nums = [float(x) for x in nums]
    except (TypeError, ValueError):
        return jsonify({"error": "请确保全部为数字"}), 400
    result = bubble_sort(nums)
    return jsonify({"sorted": result})
#添加注释
#这是冒泡排序的实现

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
