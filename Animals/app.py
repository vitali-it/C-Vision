from flask import Flask, request, jsonify
from flask_cors import CORS
import prediction
import base64

app = Flask(__name__)
CORS(app)


@app.route('/upload', methods=['GET', 'POST'])
def upload_img():
    if request.method.__eq__('POST'):
        if request.files:
            full_name = save_img()
            img_plot, pie_plot = prediction.produce_result(full_name)
            img_plot, pie_plot = code_imgs(img_plot, pie_plot)

            response = jsonify(img_plot=img_plot, pie_plot=pie_plot)
            return response

    return {}


def code_imgs(img_plot, pie_plot):
    with open(img_plot, "rb") as img_file:
        img_plot = base64.encodebytes(img_file.read()).decode('utf8')
    with open(pie_plot, "rb") as img_file:
        pie_plot = base64.encodebytes(img_file.read()).decode('utf8')
    return img_plot, pie_plot


def save_img():
    path_load = 'static/load/'
    image = request.files['image']
    image_name = image.filename
    full_name = path_load + image_name
    image.save(full_name)
    return full_name


if __name__ == '__main__':
    app.run()
