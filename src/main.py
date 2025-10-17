from agents.recommendation_agent import RecommendationAgent
from models.user import User
from core.config import Config

def main():
    config = Config()

    agent = RecommendationAgent()
    
    test_user = User(
        id="1",
        name="Test User",
        age=30,
        weight=75.0,
        height=180.0,
        goals=["weight_loss", "muscle_gain"],
        activity_level="moderate"
    )
    
    workout_plan = agent.generate_workout_plan(test_user)
    nutrition_plan = agent.generate_nutrition_plan(test_user)

if __name__ == "__main__":
    main()
