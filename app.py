from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from main import generate_music, save_music

app = Flask(__name__)

# Route for serving the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for generating music
@app.route('/generate-music', methods=['POST'])
def generate_music_route():
    data = request.get_json()
    text_input = data['text']

    if not text_input:
        return jsonify({'error': 'No text provided'}), 400

    # Generate music based on the input
    try:
        prompts = [text_input]
        generated_audio = generate_music(prompts)
        output_path = f"generated_music_{text_input[:10].replace(' ', '_')}.wav"
        save_music(output_path, generated_audio)

        # Return a response with the download URL
        return jsonify({'downloadUrl': f"/download/{output_path}"})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to download generated music
@app.route('/download/<filename>')
def download_music(filename):
    return send_from_directory(os.getcwd(), filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)