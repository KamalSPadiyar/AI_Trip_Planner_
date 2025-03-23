from crewai import Agent

def get_travel_expert_agent():
    return Agent(
        role='Travel Expert',
        goal='Assist with booking flights, accommodations, and travel logistics',
        backstory='You are a seasoned travel expert, efficient in finding the best travel deals and options.',
        verbose=True
    )
