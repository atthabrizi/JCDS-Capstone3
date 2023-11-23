import pickle
import numpy as np
import pandas as pd
import datetime as dt
import streamlit as st
from PIL import Image

model = pickle.load(open('final_model.sav', 'rb'))

@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

def main():
    # Load picture
    bikecover = Image.open('foto/bikecover.jpg')



    # Add option to select online or offline prediction
    add_selectbox = st.sidebar.selectbox(
        "How would you like to predict?", ("Online", "Batch"))

    # Add explanatory text and picture in the sidebar
    st.sidebar.image(bikecover)
    st.sidebar.info('This app is created to predict the demand of Bike Rental in Washington D.C.')    

    # Add title
    st.title("Bike Predicting System")
    st.markdown('''
    Input the data of current conditions that are required in the page below.
    The data you input will be used to predict the demand of Bicycle Rental using 
    a Machine Learing Algorithm. 

    You will get a predicted number of Bike and the error adjusted number to make a more conservative prediction''')



    if add_selectbox == 'Online':
        # Set up the form to fill in the required data 
        dteday = st.date_input('Date', min_value=dt.date(2011, 1, 1), max_value=dt.date(2012, 12, 31), value=dt.date(2011, 1, 1))
        
        hum = st.number_input(
            'Humidity', min_value=0, max_value=100, value=50)
        
        weathersit =  st.selectbox("Weather situation", [1,2,3,4])

        holiday = st.selectbox("Holiday Season", ['Yes','No'])
        if holiday == 'Yes':
            holiday = 1
        elif holiday == 'No':
            holiday = 0

        season = st.selectbox("Season", ['Spring','Summer','Fall','Winter'])
        if season == 'Spring':
            season = 1
        elif season == 'Summer':
            season = 2
        elif season == 'Fall':
            season = 3
        elif season == 'Winter':
            season = 4

        temp = st.number_input(
            'temperature', min_value=-8, max_value=39, value=12)

        hr = st.number_input(
            'Hour', min_value=0, max_value=23)
      
        temp_min = -16
        temp_max = 50
        # Convert form to data frame
        input_df = pd.DataFrame([
            {
                'dteday': pd.to_datetime(dteday),
                'hr': hr,
                'season': season,
                'holiday': holiday,
                'weathersit': weathersit,
                'hum': hum/100,
                'atemp' : 0,
                'temp': (temp-temp_min)/(temp_max-temp_min),
                'registered':'0',
                'casual':'0'}])
        
# Set a variable to store the output
        adjusted = ""
        bin4 = 0.10 
        bin3 = 0.11 
        bin2 = 0.15
        bin1 = 0.38

        # Make a prediction 
        if st.button("Predict"):
            output = model.predict(input_df)
            output = int(output)

            moe = np.where(output > 300, bin4, 
                               np.where(output > 200, bin3, 
                                        np.where(output > 90, bin2, bin1)))
            moe_percent = int(moe*100)
                # Calculate adjusted value

            adjust = output + (output * moe)
            adjusted = f'''
                    Bike Demand Prediction = {output} 


                    Margin of Error = {moe_percent} %


                    Adjusted Bike Demand Prediction = {int(adjust)}
                '''

        st.success(adjusted)  


    if add_selectbox == 'Batch':

        # Add a feature to upload the file to be predicted
        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])

        if file_upload is not None:
            # Convert the file to data frame
            data = pd.read_csv(file_upload, parse_dates=['dteday'])

            # Select only columns required by the model
            data = data[['dteday','hr','season','holiday','weathersit','hum','atemp','temp']]

            # Make predictions
            data['prediction'] = model.predict(data)
            data['prediction'] = data['prediction'].astype(int)


            # Show the result on page
            st.write(data)

            # Add a button to download the prediction result file 
            st.download_button(
                "Press to Download",
                convert_df(data),
                "Bike Prediction Result.csv",
                "text/csv",
                key='download-csv'
            )

    st.markdown("for more information and explanation about the Machine Learning Algorithm used for this predictor, you can acces this [link](https://github.com/atthabrizi/JCDS-Capstone3)  ")
if __name__ == '__main__':
    main()