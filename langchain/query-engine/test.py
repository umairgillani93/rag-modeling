class LLMWrapper(BaseSingleActionAgent):
    """Wrapper for LLM to behave like BaseSingleActionAgent."""

    def __init__(self, llm_model: Any):
        self.llm_model = llm_model
