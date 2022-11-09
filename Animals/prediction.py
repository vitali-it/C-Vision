import warnings
import cv2 as cv
import tensorflow as tf
import utils
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('SVG')

PLOT_PNG = '_plot.png'
COLOR_TITLE = 'maroon'
FONT_SIZE = 20
FIG_SIZE = 7

warnings.simplefilter(action='ignore', category=FutureWarning)

path = 'static/animals'
path_gen = 'static/generated/'
categories, img_size, norm = utils.init_data(path)

seq_model = tf.keras.models.load_model('static/models/model-20.model', compile=False)


def show_category_probability(predictions, animal_predicted):
    colors = ['magenta', 'turquoise', 'yellow']  # Cat, Dog, Panda respectively
    explode = (0.03, 0.03, 0.03)
    percentage = [predictions[0][0], predictions[0][1], predictions[0][2]]
    plt.figure(figsize=[FIG_SIZE, FIG_SIZE])
    plt.title('Animal Probability', fontsize=FONT_SIZE, color=COLOR_TITLE)
    plt.pie(percentage, labels=categories, autopct='%1.4f%%', explode=explode,
            shadow=False, startangle=90, colors=colors)
    gen_name = path_gen + animal_predicted + '_pie' + PLOT_PNG
    plt.savefig(gen_name)
    return gen_name


def animal_title(predictions):
    percentage = [predictions[0][0], predictions[0][1], predictions[0][2]]
    temp = 0
    animal_predicted = None
    animal_predicted_percent = None
    for i, v in enumerate(percentage):
        if (v * 100).round(2) > temp:
            temp = (v * 100).round(2)
            animal_predicted = categories[i] + str(temp)
            animal_predicted_percent = categories[i] + ' ' + str(temp) + '%'

    return [animal_predicted, animal_predicted_percent]


def check_img(name):
    image = cv.imread(name)
    image = cv.resize(image, (img_size, img_size), 3)
    image = image.astype('float') / norm
    return image.reshape((1, img_size, img_size, 3))


def plt_show(animal_predicted, animal_predicted_percent, img):
    plt.figure(figsize=(FIG_SIZE, FIG_SIZE))
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.title(animal_predicted_percent, fontsize=FONT_SIZE, color=COLOR_TITLE)
    gen_name = path_gen + animal_predicted + PLOT_PNG
    plt.savefig(gen_name)
    return gen_name


def produce_result(img_name):
    image = check_img(img_name)
    predictions = seq_model.predict(image)
    animal_predicted, animal_predicted_percent = animal_title(predictions)
    image = cv.imread(img_name)
    img_plot = plt_show(animal_predicted, animal_predicted_percent, image)
    pie_plot = show_category_probability(predictions, animal_predicted)
    plt.show()
    return img_plot, pie_plot
