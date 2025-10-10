from fastapi import FastAPI
from pydantic import BaseModel
from models.agent import SportAI
from config.config import Config

app = FastAPI()
config = Config()
agent = SportAI(config)

class PredictionRequest(BaseModel):
    data: dict

class TrainingSession(BaseModel):
    user_id: str
    exercise_type: str
    duration: int
    intensity: str

@app.post("/api/predict")
async def predict(request: PredictionRequest):
    result = agent.predict(request.data)
    return {"prediction": result}

@app.get("/api/training/recommend")
async def recommend_training(user_id: str):
    recommendations = agent.get_recommendations(user_id)
    return {"recommendations": recommendations}

@app.post("/api/training/log")
async def log_training(training: TrainingSession):
    agent.log_training_session(training.dict())
    return {"status": "success"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
