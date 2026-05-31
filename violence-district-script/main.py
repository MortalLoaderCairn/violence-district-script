import sys
from src.script_manager import ScriptManager
from src.config import Config
from src.utils.logger import setup_logger

def main():
    logger = setup_logger("violence_district")
    logger.info("Starting Violence District Script")

    config = Config()
    manager = ScriptManager(config)

    try:
        result = manager.execute_script("violence_district")
        logger.info(f"Script executed: {result}")
    except Exception as e:
        logger.error(f"Execution failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()