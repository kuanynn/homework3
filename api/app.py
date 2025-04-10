import os
import sys
import json
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='../templates')

# 配置 Gemini
GOOGLE_API_KEY = "AIzaSyB3HePjAO-W1VfY7sjsOwRvoTV97CsEWZI"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    try:
        response = model.generate_content(user_input)
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def cli_chat():
    print("歡迎使用 AI 聊天機器人！輸入 'exit' 結束對話。")
    while True:
        user_input = input("\n你: ")
        if user_input.lower() == 'exit':
            break
        try:
            response = model.generate_content(user_input)
            print(f"\nAI: {response.text}")
        except Exception as e:
            print(f"發生錯誤: {str(e)}")

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--cli':
        cli_chat()
    else:
        app.run(debug=True, port=5005) 