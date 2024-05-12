from typing import List, Tuple, Any, Union
from langchain.agents.agent import BaseSingleActionAgent, AgentAction, AgentFinish, AgentType
from langchain_community.llms import Ollama

class LLMWrapper(BaseSingleActionAgent):
    """Wrapper for LLM to behave like BaseSingleActionAgent."""
    llm_model: Any

    def plan(
        self,
        intermediate_steps: List[Tuple[AgentAction, str]],
        callbacks: Any = None,
        **kwargs: Any,
    ) -> Union[AgentAction, AgentFinish]:
        # Implement your planning logic using the LLM model
        # Here, you can use llm_model to make predictions based on intermediate_steps
        # For demonstration purposes, we'll just return a dummy action
        return AgentAction(tool="dummy_tool", parameters={"param1": "value1"})

    @property
    def input_keys(self) -> List[str]:
        # Define the input keys expected by the LLM model
        # These keys should match the input format expected by the LLM model
        return ["input_feature_1", "input_feature_2"]

    #@property
    #def _agent_type(self) -> str:
    #    # Define the agent type
    #    return "LLMWrapper"

    async def aplan(
        self,
        llm_model: Any,  # Pass llm_model as an argument
        intermediate_steps: List[Tuple[AgentAction, str]],
        callbacks: Any = None,
        **kwargs: Any,
    ) -> Union[AgentAction, AgentFinish]:
        # Implement a placeholder for asynchronous planning
        # For simplicity, we'll just call the synchronous plan method
        return self.plan(intermediate_steps, callbacks, **kwargs)


# Assuming llm_model is already instantiated
if __name__ == '__main__':
    llm_model = Ollama(model = "llama2")
    print(llm_model)
    llm_wrapper = LLMWrapper(llm_model)
    

