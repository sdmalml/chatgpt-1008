from chat_model import ChatModel
from chat_history import ChatHistory
from chat_app import ChatApp

class AppFactory:
    """애플리케이션 초기화를 위한 팩토리 클래스"""

    @staticmethod
    def create_chat_app(system_prompt=None):
        """Chat 애플리케이션을 생성한다."""
        # 필요한 모델 ID를 정의 (사용자가 Claude Haiku 모델을 사용)
        CLAUDE_HAIKU_ID = 'anthropic.claude-3-haiku-20240307-v1:0'
        
        # ChatModel 인스턴스를 생성 (시스템 프롬프트 전달)
        chat_model = ChatModel(CLAUDE_HAIKU_ID, system_prompt=system_prompt)
        
        # 대화 기록 관리 객체 생성
        chat_history = ChatHistory()
        
        # ChatApp 인스턴스 반환 (모델과 대화 기록 관리 객체를 포함)
        return ChatApp(chat_model, chat_history)
