from crewai import Agent
from crewai import Agent, LLM
from .tools import file_read_tool, pdf_tool, search_tool

# Set up Ollama LLM
ollama_llm1 = LLM(model="ollama/openhermes:latest", base_url="http://localhost:11434")
ollama_llm2 = LLM(model="ollama/gemma3:latest", base_url="http://localhost:11434")

# Define Agents
researcher = Agent(
    role='Market Researcher',
    goal='To research the product and its market to provide a comprehensive analysis of the product and its positioning.',
    backstory='An experienced market researcher with a deep understanding of product design and marketing. Skilled in identifying market trends and consumer needs.',
    verbose=True,
    allow_delegation=False,
    llm=ollama_llm1,
    tools=[file_read_tool, pdf_tool, search_tool]
)

analyst = Agent(
    role='Sales Analyst',
    goal='To analyze the product from a sales perspective, identifying key selling points and potential customer objections.',
    backstory='A seasoned sales representative who understands the end-user and can articulate the product\'s value proposition effectively.',
    verbose=True,
    allow_delegation=False,
    llm=ollama_llm2,
    tools=[file_read_tool, pdf_tool]
)

media_relations = Agent(
    role='Media Relations Specialist',
    goal='To craft a compelling narrative for the product and create engaging marketing copy.',
    backstory='A communications expert with a knack for storytelling and a deep understanding of how to generate positive media attention.',
    verbose=True,
    allow_delegation=False,
    llm=ollama_llm1,
    tools=[file_read_tool, pdf_tool]
)

sales_deck_writer = Agent(
    role='Master Sales Deck Writer',
    goal='To create a persuasive and visually appealing sales deck that effectively communicates the product\'s value proposition.',
    backstory='A master storyteller and presentation designer who can synthesize complex information into a clear and compelling narrative.',
    verbose=True,
    allow_delegation=True,
    llm=ollama_llm2,
    tools=[file_read_tool, pdf_tool]
)
