from models.agent import SportAI
from config.config import Config

def main():
    config = Config()
    agent = SportAI(config)
    agent.start()

if __name__ == "__main__":
    main()
