import matplotlib.pyplot as plt
from io import StringIO
import os
import tensorflow.keras as tf
import numpy as np
from .forms import LinearRegressionForm
from django.shortcuts import render
from django.core.files.storage import default_storage
from sklearn.linear_model import LinearRegression

def index(request):
    return render(request, 'index.html')

def classify_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES['image']
        temp_image_path = default_storage.save('temp_image.jpg', image_file)
        model = tf.models.load_model('CatsVsDogs.h5')
        img = tf.utils.load_img(os.path.join('media', temp_image_path), target_size=(128, 128))
        x = tf.utils.img_to_array(img)
        x /= 255
        x = np.expand_dims(x, axis=0)
        images = np.vstack([x])
        pred = model.predict(images)
        output = "It is a dog" if pred[0] > 0.5 else "It is a cat"
        return render(request, 'results.html', {'predictions': output, 'uploaded_image': os.path.join('media', temp_image_path)})
    return render(request, 'classification.html')

def linear_regression(request):
    if request.method == 'POST':
        form = LinearRegressionForm(request.POST)
        if form.is_valid():
            input_values = [
                form.cleaned_data['input1'],
                form.cleaned_data['input2'],
                form.cleaned_data['input3'],
                form.cleaned_data['input4'],
                form.cleaned_data['input5']
            ]
            output_values = [
                form.cleaned_data['output1'],
                form.cleaned_data['output2'],
                form.cleaned_data['output3'],
                form.cleaned_data['output4'],
                form.cleaned_data['output5']
            ]
            X = np.array(input_values).reshape(-1, 1)
            y = np.array(output_values)
            model = LinearRegression()
            model.fit(X, y)
            slope = model.coef_[0]
            intercept = model.intercept_
            input_number = form.cleaned_data['input_number']
            prediction = model.predict([[input_number]])

            return render(request, 'linreg_res.html', {'slope': float("{:.2f}".format(slope)), 'intercept': float("{:.2f}".format(intercept)), 'prediction': float("{:.2f}".format(prediction[0])), 'form': form, 'graph': return_graph(input_values, output_values, model.predict(X))})
    else:
        form = LinearRegressionForm()

    return render(request, 'linreg.html', {'form': form})

def return_graph(ip, op, pred_op):
    fig = plt.figure()
    plt.scatter(ip, op, color='blue', label='Data Points')
    plt.plot(ip, pred_op, color='red', label='Linear Regression')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Linear Regression Model')
    plt.legend()
    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data