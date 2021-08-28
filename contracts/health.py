import smartpy as sp

class Health(sp.Contract):
    """Health contract"""
    def __init__(self, name: str, health: int):
        """Initialize health contract"""
        super().__init__(name)
        self.health = health

    def get_health(self) -> int:
        """Get health"""
        return self.health

    def set_health(self, health: int):
        """Set health"""
        self.health = health