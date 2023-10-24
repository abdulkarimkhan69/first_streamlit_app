import streamlit
import pandas
streamlit.title('My parents healthy diner')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect ("Pick me fruit", list(my_fruit_list.index),['Avocado','Strawberries'])


streamlit.dataframe(my_fruit_list)

