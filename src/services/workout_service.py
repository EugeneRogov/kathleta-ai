from typing import Dict, List, Optional
from datetime import datetime

class WorkoutService:
    """Service class for managing workout operations."""

    def __init__(self):
        """Initialize workout service with empty workout storage."""
        self.workouts: Dict[str, dict] = {}

    def create_workout(self, workout_id: str, workout_data: dict) -> bool:
        """
        Create a new workout entry.

        Args:
            workout_id: Unique identifier for the workout
            workout_data: Dictionary containing workout information

        Returns:
            bool: True if creation successful, False if workout_id already exists
        """
        if workout_id in self.workouts:
            return False
        workout_data['created_at'] = datetime.now()
        self.workouts[workout_id] = workout_data
        return True

    def get_workout(self, workout_id: str) -> Optional[dict]:
        """
        Retrieve a specific workout by ID.

        Args:
            workout_id: Unique identifier of the workout

        Returns:
            Optional[dict]: Workout data if found, None otherwise
        """
        return self.workouts.get(workout_id)

    def get_user_workouts(self, user_id: str) -> List[dict]:
        """
        Get all workouts for a specific user.

        Args:
            user_id: Unique identifier of the user

        Returns:
            List[dict]: List of workouts belonging to the user
        """
        return [
            workout for workout in self.workouts.values()
            if workout.get('user_id') == user_id
        ]

    def update_workout(self, workout_id: str, workout_data: dict) -> bool:
        """
        Update an existing workout.

        Args:
            workout_id: Unique identifier of the workout
            workout_data: New workout data to update

        Returns:
            bool: True if update successful, False if workout not found
        """
        if workout_id not in self.workouts:
            return False
        self.workouts[workout_id].update(workout_data)
        return True

    def delete_workout(self, workout_id: str) -> bool:
        """
        Delete a workout by ID.

        Args:
            workout_id: Unique identifier of the workout

        Returns:
            bool: True if deletion successful, False if workout not found
        """
        if workout_id not in self.workouts:
            return False
        del self.workouts[workout_id]
        return True
