import argparse
from core.crew_initializer import initialize_trip_crew
from utils.logger import get_logger

logger = get_logger()

def main(destination: str, days: int):
    logger.info(f"Planning a trip to {destination} for {days} days...")
    crew = initialize_trip_crew(destination, days)
    result = crew.kickoff()
    logger.info("Trip planning completed!\n")
    print(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Trip Planner using CrewAI")
    parser.add_argument('--destination', type=str, default='Tokyo', help='Destination city')
    parser.add_argument('--days', type=int, default=5, help='Trip duration in days')
    args = parser.parse_args()
    
    main(args.destination, args.days)
