from crewai import Task, Crew
from crew_agents.local_guide_agent import get_local_guide_agent
from crew_agents.travel_expert_agent import get_travel_expert_agent
from crew_agents.planner_agent import get_itinerary_planner_agent
from utils.logger import get_logger

logger = get_logger()

def initialize_trip_crew(destination="Tokyo", days=5):
    local_guide = get_local_guide_agent()
    travel_expert = get_travel_expert_agent()
    planner = get_itinerary_planner_agent()

    task1 = Task(
        description=f"Suggest must-visit places, local food, and culture in {destination}.",
        agent=local_guide
    )

    task2 = Task(
        description=f"Find best travel options and accommodations for {days} days in {destination}.",
        agent=travel_expert
    )

    task3 = Task(
        description=f"Plan a detailed {days}-day itinerary for a trip to {destination}.",
        agent=planner
    )

    crew = Crew(
        agents=[local_guide, travel_expert, planner],
        tasks=[task1, task2, task3],
        verbose=True
    )

    logger.info("Crew initialized successfully")
    return crew
