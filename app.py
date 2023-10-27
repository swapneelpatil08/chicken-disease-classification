from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.predict import PredictionPipeline

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage"
        self.classifier = PredictionPipeline(f"{self.filename}.png")
        
@app.route('/', methods=['GET'])
@cross_origin()
def index():
    return render_template('index.html')

@app.route('/train', methods=['GET', 'POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training completed successfully!!"

@app.route('/predict', methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clapp.filename)
    result = clapp.classifier.predict()
    return jsonify(result)

if __name__ == '__main__':
    clapp = ClientApp()
    app.run(host='0.0.0.0', port=9988)