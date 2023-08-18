import streamlit as st
#import pickle
#import joblib
from sklearn.externals import joblib

# Function to load the selected model
def load_model(model_name):
    model_path = f'{model_name}.pkl'
    with open(model_path, 'rb') as file:
        model = joblib.load(file)
    return model

# Mapping for decoding encoded features
status_mapping = {
                    0: 'Employment Programme',
                    1: 'Other',
                    2: 'Self-Employed',
                    3: 'Wage Employed',
                    4: 'Unemployed',
                    5: 'Wage and Self-Employed',
                    6: 'Employed'
                    }
geography_mapping = {0.0: 'Rural',
                     1.0: 'Suburb',
                     2.0:'Urban'}
higher_education_mapping = {0.0: 'No',
                            1.0: 'Yes'}
schoolquintile_mapping = {
                            0.0: 'No',
                            1.0: 'Yes',
                            # 2.0: 'Q3',
                            # 3.0: 'Q4',
                            # 4.0: 'Q5',
                            # 5.0: 'Q6'
                            }
gender_mapping = {0.0: 'Male',
                  1.0: 'Female'}

def main():
    # Title of the web app
    st.title('Youth Employment Prediction')

    # Subheader
    st.subheader('Welcome! Select a model and input features for prediction.')
    
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url('https://re-imagine.eu/wp-content/uploads/2021/09/shutterstock_1845592183-scaled-e1632468832252-1920x1305.jpg');
        background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Dropdown to select the model
    model_options = ['RidgeClassifier', 'DecisionTreeClassifier', 'RandomForestClassifier']
    selected_model = st.selectbox('Select Model', model_options)

    # Load the selected model
    model = load_model(selected_model)

    # User input for features
    st.header('Feature Input')
    feature1 = st.selectbox('Status', options=list(status_mapping.values()))
    feature1_encoded = [k for k, v in status_mapping.items() if v == feature1][0]

    feature2 = st.selectbox('Geography', options=list(geography_mapping.values()))
    feature2_encoded = [k for k, v in geography_mapping.items() if v == feature2][0]

    feature3 = st.selectbox('Higher Education', options=list(higher_education_mapping.values()))
    feature3_encoded = [k for k, v in higher_education_mapping.items() if v == feature3][0]

    feature4 = st.selectbox('Matric', options=list(schoolquintile_mapping.values()))
    feature4_encoded = [k for k, v in schoolquintile_mapping.items() if v == feature4][0]

    feature5 = st.selectbox('Gender', options=list(gender_mapping.values()))
    feature5_encoded = [k for k, v in gender_mapping.items() if v == feature5][0]

    # Mapping for prediction labels
    prediction_mapping = {
    0: 'Not employable',
    1: 'Employable'
    }

    # Button for predictions
    clicked = st.button('Get Predictions')

    # Perform predictions when the button is clicked
    if clicked:
        # Perform predictions using the selected model
        prediction = model.predict([[feature1_encoded, feature2_encoded, feature3_encoded, feature4_encoded, feature5_encoded]])
        
        # Map the prediction to human-readable label
        prediction_label = prediction_mapping[prediction[0]]

        # Display the prediction result
        st.header('Prediction')
        st.write(f'Employement Status: {prediction_label}')

if __name__ == '__main__':
    main()
