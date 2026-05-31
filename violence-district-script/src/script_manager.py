import random
from .utils.logger import setup_logger

class ScriptManager:
    def __init__(self, config):
        self.config = config
        self.logger = setup_logger("ScriptManager")

    def execute_script(self, script_name: str) -> str:
        self.logger.debug(f"Executing script: {script_name}")
        
        if script_name not in self.config.scripts:
            raise ValueError(f"Script '{script_name}' not found in config")
        
        script_path = self.config.scripts[script_name]
        return self._run(script_path)

    def _run(self, path: str) -> str:
        # Simulate script execution
        success = random.choice([True, False])
        if success:
            return f"Script at {path} completed successfully"
        else:
            raise RuntimeError(f"Script at {path} encountered an error")