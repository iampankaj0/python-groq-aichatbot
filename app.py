from flask import Flask, jsonify, request, render_template
from groq import Groq
import requests
import os
import markdown

app = Flask(__name__)

# GROQ_API_KEY = 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

client = Groq(
    api_key="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",
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
        try:
            data = request.get_json()
            question = data.get('question', 'hii')
            chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI Bot created by Ritika Yadav.",
                },
                {
                    "role": "user",
                    "content": question,
                }
            ],
            model="llama3-8b-8192",
            )

            # Process the response
            answer = chat_completion.choices[0].message.content
            html_answer = markdown.markdown(answer)
            return jsonify({
                "success": True,
                "answer": html_answer
            }), 200


        except Exception as error:
            print(error)
            return jsonify({
                "success": False,
                "message": str(error)
            }), 500


if __name__ == '__main__':
    app.run(debug=True)
