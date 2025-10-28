from crewai import Crew, Process
from .agents import researcher, analyst, media_relations, sales_deck_writer
from .tasks import research_task, analysis_task, media_task, deck_writing_task

# Create Crew
sales_deck_crew = Crew(
    agents=[researcher, analyst, media_relations, sales_deck_writer],
    tasks=[research_task, analysis_task, media_task, deck_writing_task],
    process=Process.sequential
)

# Execute Crew
if __name__ == "__main__":
    result = sales_deck_crew.kickoff()
    print("######################")
    print(result)