import os
from django.conf import settings
from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("data.csv")


def data_split(data, ratio):
    np.random.seed(100)
    shuffled = np.random.permutation(len(data))
    test_data_size = int(len(data)*ratio)
    test_data_indices = shuffled[: test_data_size]
    train_data_indices = shuffled[test_data_size:]
    return data.iloc[test_data_indices], data.iloc[train_data_indices]


test_data, train_data = data_split(df, 0.30)
x_train = train_data[['Age', 'BodyTemp.', 'Fatigue', 'Cough',
                      'BodyPain', 'SoreThroat', 'BreathingDifficulty']].to_numpy()
x_test = test_data[['Age', 'BodyTemp.', 'Fatigue', 'Cough',
                    'BodyPain', 'SoreThroat', 'BreathingDifficulty']].to_numpy()
y_train = train_data[['Infected']].to_numpy().reshape(-1)
y_test = test_data[['Infected']].to_numpy().reshape(-1)

clf = LogisticRegression()
clf.fit(x_train, y_train)


def home(request):
    return render(request, 'home.html')

# def result(request):
#     return render(request, 'result.html')


def analyse(request):
    Age = int(request.POST.get('Age'))
    BodyTemp = float(request.POST.get('BodyTemp.'))
    Fatigue = int(request.POST.get('Fatigue'))
    Cough = int(request.POST.get('Cough'))
    BodyPain = int(request.POST.get('BodyPain'))
    SoreThroat = int(request.POST.get('SoreThroat'))
    BreathingDifficulty = int(request.POST.get('BreathingDifficulty'))
    infProb = clf.predict_proba(
        [[Age, BodyTemp, Fatigue, Cough, BodyPain, SoreThroat, BreathingDifficulty]])
    params = {'InfProb': round(
        infProb[0][1]*100, 2), 'Degree': round(infProb[0][1]*180, 2)}
    return render(request, 'result.html', params)

def dev(request):
    notebook_path = os.path.join(settings.BASE_DIR, 'Solution.ipynb')
    
    # Read the notebook content
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook_content = f.read()

    return render(request, 'Solution.html', {'notebook_content': notebook_content})