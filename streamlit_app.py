import streamlit
import pandas
streamlit.title('My parents healthy diner')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
streamlit.body('This is body of page')
