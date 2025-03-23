from crewai import Agent

def get_local_guide_agent():
    return Agent(
        role='Local Guide',
        goal='Provide insights about local attractions, culture, and hidden gems',
        backstory='You are a knowledgeable local guide with expertise in showcasing unique travel experiences.',
        verbose=True
    )
