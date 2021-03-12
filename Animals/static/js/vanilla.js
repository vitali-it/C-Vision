document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('btn').style.visibility = 'hidden';
    document.getElementById('imgs').style.visibility = 'hidden';
    if (document.getElementById('img_plot').getAttribute('src') ||
        document.getElementById('pie_plot').getAttribute('src')) {
        document.getElementById('imgs').style.visibility = 'visible';
    }
});

function showButton() {
    document.getElementById('btn').style.visibility = 'visible';
};

function showImgs() {
    document.getElementById('imgs').style.visibility = 'visible';
}

function browse() {
    document.getElementById('image').click()
}
