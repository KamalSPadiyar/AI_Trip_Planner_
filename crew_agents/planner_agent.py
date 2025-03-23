from crewai import Agent

def get_itinerary_planner_agent():
    return Agent(
        role='Itinerary Planner',
        goal='Create the ultimate travel plan using the inputs from other agents',
        backstory='A master travel planner, you compile all the details into an ideal itinerary.',
        verbose=True
    )
