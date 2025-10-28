from crewai_tools import SerperDevTool, FileReadTool, PDFSearchTool
from langchain_ollama import OllamaLLM

file_read_tool = FileReadTool("file_source": "D:\AI Salesdeck builder\sales-deck-generator\Place product description here\Apex_ProBlend_9000_Food_Processor_Description.pdf")

pdf_tool = PDFSearchTool(pdf='D:\AI Salesdeck builder\sales-deck-generator\Place product description here\Apex_ProBlend_9000_Food_Processor_Description.pdf')

search_tool=SerperDevTool()