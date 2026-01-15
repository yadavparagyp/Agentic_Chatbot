from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
    Basci chatbot login implementation
    """
    def __init__(self,model):
        self.llm=model

    def process(self,state:State)->dict :
        """
        Process a input state and generate a chatbot response
        """
        return {"messages":self.llm.invoke(state['messages'])}
