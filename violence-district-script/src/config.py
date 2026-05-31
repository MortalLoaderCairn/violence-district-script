class Config:
    def __init__(self):
        self.scripts = {
            "violence_district": "scripts/violence_district.lua",
            "test_script": "scripts/test.lua"
        }
        self.timeout = 30
        self.retry_count = 3

    def get_script_path(self, name: str) -> str:
        return self.scripts.get(name, "")