import streamlit as st
from chat_model import ChatModel
from chat_history import ChatHistory

class ChatApp:
    """Chat 애플리케이션 클래스는 사용자의 입력과 대화 흐름을 관리한다."""
    
    def __init__(self, model: ChatModel, history: ChatHistory):
        self.model = model
        self.history = history
    
    def display_chat(self):
        """대화 기록을 화면에 표시한다."""
        for message in self.history.get_messages():
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
    def handle_user_input(self, extracted_text=None):
        """사용자의 입력을 처리하고 응답을 표시한다."""
        prompt = st.chat_input("질문을 입력해주세요.")
        if prompt:
            # PDF에서 추출된 텍스트와 함께 프롬프트 처리
            final_prompt = prompt if not extracted_text else f"{extracted_text}\n{prompt}"
            
            self.history.add_message("user", final_prompt)
            with st.chat_message("user"):
                st.markdown(final_prompt)
            
            # 모델에 사용자 입력을 전달하고 응답을 받는다
            response = self.model.get_response(final_prompt)
            
            # 응답을 화면에 표시
            with st.chat_message("assistant"):
                st.write(response)
            
            self.history.add_message("assistant", response)
