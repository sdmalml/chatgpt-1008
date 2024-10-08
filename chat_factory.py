from chat_model import ChatModel
from chat_history import ChatHistory
from chat_app import ChatApp

class AppFactory:
    """애플리케이션 초기화를 위한 팩토리 클래스"""
    
    @staticmethod
    def create_chat_app(system_prompt=None):
        """Chat 애플리케이션을 생성한다."""
        CLAUDE_HAIKU_ID = 'anthropic.claude-3-haiku-20240307-v1:0'
        chat_model = ChatModel(CLAUDE_HAIKU_ID, system_prompt=system_prompt)
        chat_history = ChatHistory()
        return ChatApp(chat_model, chat_history)
