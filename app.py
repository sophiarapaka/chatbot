import os
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from google.generativeai import GenerativeModel
from PIL import Image

# Configure Gemini API
genai.configure(api_key="")#yuour gemini api key

# Set up Gemini models
text_model = genai.GenerativeModel("gemini-pro")
vision_model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")  # ✅ updated here
chat_model = genai.GenerativeModel("models/gemini-1.5-flash")

# Flask setup
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_input = data["message"]

    # Get Gemini response
    full_response = chat_model.generate_content(user_input)
    
    # ✅ Get the actual text content
    response_text = full_response.text

    # ✅ Limit to first 5 lines
    response_lines = response_text.strip().split('\n')
    trimmed_response = '\n'.join(response_lines[:5])

    return jsonify({"response": trimmed_response})


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected image'}), 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    image = Image.open(filepath)
    response = vision_model.generate_content([
    "Identify the specific landmark or temple in this image. If it's an Indian temple, mention its name and location.",
    image
])

    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(debug=True)
