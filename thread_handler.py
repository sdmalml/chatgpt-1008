import streamlit as st

def save_thread(thread_id, messages):
    """대화 쓰레드를 저장한다."""
    st.session_state[f"thread_{thread_id}"] = messages

def load_thread(thread_id):
    """저장된 대화 쓰레드를 불러온다."""
    return st.session_state.get(f"thread_{thread_id}", [])

def list_threads():
    """저장된 대화 쓰레드 목록을 반환한다."""
    return [key for key in st.session_state.keys() if key.startswith("thread_")]

