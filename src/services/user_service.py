from typing import Dict, Optional

class UserService:
    def __init__(self):
        self.users: Dict[str, dict] = {}

    def create_user(self, user_id: str, user_data: dict) -> bool:
        if user_id in self.users:
            return False
        self.users[user_id] = user_data
        return True

    def get_user(self, user_id: str) -> Optional[dict]:
        return self.users.get(user_id)

    def update_user(self, user_id: str, user_data: dict) -> bool:
        if user_id not in self.users:
            return False
        self.users[user_id].update(user_data)
        return True

    def delete_user(self, user_id: str) -> bool:
        if user_id not in self.users:
            return False
        del self.users[user_id]
        return True
