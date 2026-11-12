import streamlit as st
from modules import functions

FILE_PATH = "files/todos.txt"


def add_new_todo():
    new_todo = st.session_state.new_todo
    functions.add_todo(FILE_PATH, new_todo + "\n")
    st.session_state.new_todo = ""


st.title("Todos Web App")
st.markdown("Here you can organise your todos.")
st.text_input(label=" ", placeholder="Enter your todo", key="new_todo", on_change=add_new_todo)

todos = functions.get_todos(FILE_PATH)

for todo in todos:
    st.checkbox(todo)



