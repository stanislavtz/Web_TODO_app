import streamlit as st
from modules import functions

FILE_PATH = "files/todos.txt"

# Which todo is currently selected for editing (None = no todo selected)
if "editing" not in st.session_state:
    st.session_state.editing = None


def clear_selection():
    """ Unchecks the selected todo and empties the input field. """
    selected = st.session_state.editing
    if selected is not None:
        st.session_state.pop(selected, None)
    st.session_state.editing = None
    st.session_state.new_todo = ""


def add_new_todo():
    # While a todo is being edited, the input is used by the Edit button, not for adding
    if st.session_state.editing is not None:
        return

    new_todo = st.session_state.new_todo.strip()

    if not new_todo:
        return

    functions.add_todo(FILE_PATH, new_todo + "\n")
    st.session_state.new_todo = ""


def select_todo(todo):
    """ Called when a checkbox is checked/unchecked. Loads the todo into the input field. """
    if st.session_state[todo]:
        # Only one todo can be selected at a time - uncheck the previous one
        previous = st.session_state.editing
        if previous is not None and previous != todo:
            st.session_state[previous] = False
        st.session_state.editing = todo
        st.session_state.new_todo = todo.strip()
    else:
        st.session_state.editing = None
        st.session_state.new_todo = ""


def edit_todo(todo):
    new_value = st.session_state.new_todo.strip()
    if not new_value:
        return
    todos = functions.get_todos(FILE_PATH)
    if todo in todos:
        todos[todos.index(todo)] = new_value.capitalize() + "\n"
        functions.save_todos(FILE_PATH, todos)
    clear_selection()


def complete_todo(todo):
    todos = functions.get_todos(FILE_PATH)
    if todo in todos:
        todos.remove(todo)
        functions.save_todos(FILE_PATH, todos)
    if st.session_state.editing == todo:
        clear_selection()
    else:
        st.session_state.pop(todo, None)


st.title("Todos Web App")
st.markdown("Here you can organise your todos.")
st.text_input(label=" ", placeholder="Enter your todo", key="new_todo", on_change=add_new_todo)

todos = functions.get_todos(FILE_PATH)

for todo in todos:
    col_todo, col_edit, col_complete = st.columns([6, 1, 1.4])
    with col_todo:
        st.checkbox(todo, key=todo, on_change=select_todo, args=(todo,))
    with col_edit:
        st.button("Edit", key=f"edit_{todo}", on_click=edit_todo, args=(todo,),
                  disabled=st.session_state.editing != todo)
    with col_complete:
        st.button("Complete", key=f"complete_{todo}", on_click=complete_todo, args=(todo,))
