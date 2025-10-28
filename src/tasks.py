from crewai import Task
from .agents import researcher, analyst, media_relations, sales_deck_writer

# Define Tasks
research_task = Task(
    description='Research the product and its market. Provide a comprehensive analysis of the product, its features, benefits, and target audience.',
    agent=researcher,
    expected_output='A comprehensive analysis document detailing the product, its features, benefits, and target audience.'
)

analysis_task = Task(
    description='Analyze the product from a sales perspective. Identify key selling points, potential customer objections, and a competitive analysis.',
    agent=analyst,
    context=[research_task],
    expected_output='A sales analysis report including key selling points, potential customer objections, and a competitive analysis.'
)

media_task = Task(
    description='Craft a compelling narrative for the product. Create engaging marketing copy and a press release.',
    agent=media_relations,
    context=[analysis_task],
    expected_output='A compelling product narrative, marketing copy, and a press release.'
)

deck_writing_task = Task(
    description='Create a persuasive and visually appealing sales deck. The deck should include a title slide, problem statement, solution, product demo, and a call to action.',
    agent=sales_deck_writer,
    context=[media_task],
    expected_output='A complete sales deck presentation with a title slide, problem statement, solution, product demo, and a call to action.'
)
