import streamlit as st
from tensorflow.keras.models import load_model
import pickle as pkl

model = load_model('models/boston.model')
dtm = pkl.load(open('models/dtm.pkl', 'rb'))
ext = pkl.load(open('models/ext.pkl', 'rb'))
grb = pkl.load(open('models/grb.pkl', 'rb'))
adb = pkl.load(open('models/adb.pkl', 'rb'))
knr = pkl.load(open('models/knr.pkl', 'rb'))

st.write("Enter values for your house")
data = [0 for i in range(13)]
data[0] = st.number_input('CRIM - per capita crime rate by town', step=0.1)

data[1] = st.number_input('ZN - proportion of residential land zoned for lots over 25,000 sq.ft.')

data[2] = st.number_input('INDUS - proportion of non-retail business acres per town.')

data[3] = st.radio("CS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)", (1, 0))

data[4] = st.number_input('NOX - nitric oxides concentration (parts per 10 million)')

data[5] = st.number_input('RM - average number of rooms per dwelling')

data[6] = st.number_input('AGE - proportion of owner-occupied units built prior to 1940')

data[7] = st.number_input('DIS - weighted distances to five Boston employment centres')

data[8] = st.number_input('RAD - index of accessibility to radial highways')

data[9] = st.number_input('TAX - full-value property-tax rate per $10,000')

data[10] = st.number_input('PTRATIO - pupil-teacher ratio by town')

data[11] = st.number_input('B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town')

data[12] = st.number_input('LSTAT - % lower status of the population')

def predict_models(name):
    if name == 'keras DL model':
        return round(model.predict([data])[0,0]*1000, 2)
    elif name == 'Deciontree ML model':
        return round(dtm.predict([data])[0]*1000, 2)
    elif name == 'ExtraTrees ML model':
        return round(ext.predict([data])[0]*1000, 2)
    elif name == 'GradientBoost ML model':
        return round(grb.predict([data])[0]*1000, 2)
    elif name == 'AdaBoost ML model':
        return round(adb.predict([data])[0]*1000, 2)
    else:
        return round(knr.predict([data])[0]*1000, 2)

options = st.multiselect(
    'Which model do you want?',
    ['keras DL model', 'Deciontree ML model', 'ExtraTrees ML model', 'GradientBoost ML model', 'AdaBoost ML model', 'KNeighbors ML model'])
if st.button('Predict price'):
    for i in range(len(options)):
        st.write(f"Your house's price with {options[i]} is ${predict_models(options[i])}")

