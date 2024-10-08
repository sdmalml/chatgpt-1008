from langchain_aws.chat_models import ChatBedrock

class ChatModel:
    """Chat 모델 클래스는 주어진 모델 ID와 시스템 프롬프트로 초기화하고 요청에 대한 응답을 제공합니다."""
    
    def __init__(self, model_id, system_prompt=None):
        self.chat_model = ChatBedrock(model_id=model_id)
        self.system_prompt = system_prompt
    
    def get_response(self, prompt: str):
        """모델에 시스템 프롬프트와 사용자 입력을 결합하여 요청을 보낸다."""
        if self.system_prompt:
            full_prompt = f"{self.system_prompt}\n{prompt}"
        else:
            full_prompt = prompt
        return self.chat_model.stream(full_prompt)
