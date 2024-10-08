from chat_model import ChatModel
from chat_history import ChatHistory
from chat_app import ChatApp

class AppFactory:
    """애플리케이션 초기화를 위한 팩토리 클래스"""

    @staticmethod
    def create_chat_app(system_prompt=None, model_id=None):
        """Chat 애플리케이션을 생성한다."""
        
        # ChatModel 인스턴스를 생성 (시스템 프롬프트와 선택된 모델 ID 전달)
        chat_model = ChatModel(model_id, system_prompt=system_prompt)
        
        # 대화 기록 관리 객체 생성
        chat_history = ChatHistory()
        
        # ChatApp 인스턴스 반환 (모델과 대화 기록 관리 객체를 포함)
        return ChatApp(chat_model, chat_history)
