from flask import Flask, render_template, request
import prediction
app = Flask(__name__)


@app.route('/')
def land_page():
    return render_template('landing.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_img():
    if request.method.__eq__('POST'):

        if request.files:
            full_name = save_img()
            img_plot, pie_plot = prediction.produce_result(full_name)
            return render_template('load.html', img_plot=img_plot, pie_plot=pie_plot)

    return render_template('load.html')


def save_img():
    path_load = 'static/load/'
    image = request.files['image']
    image_name = image.filename
    full_name = path_load + image_name
    image.save(full_name)
    return full_name


if __name__ == '__main__':
    app.run()
