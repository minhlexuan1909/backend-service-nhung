class ConfigNotFound(Exception):
    def __init__(self, key: str):
        super().__init__(f"Config key {key} not found")
