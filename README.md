Creative Writing MCP Server

A lightweight AI-powered creative writing tool server built with FastAPI and OpenAI.
This project exposes multiple writing tools that can be used by applications, agents, or MCP-style tool orchestration systems to assist with storytelling.

The server provides endpoints for:

Generating structured story outlines

Creating character development arcs

Injecting plot twists

Analyzing emotional pacing of stories

This project demonstrates how to build modular AI tools and expose them through an API, a common pattern used in modern LLM agent architectures and MCP-style tool servers.

Features

AI-powered story generation

Modular tool architecture

Async OpenAI API integration

FastAPI REST interface

Automatic API documentation (Swagger)

Easy integration with AI agents or apps

Project Architecture
Client / Agent
      │
      ▼
FastAPI Server
      │
      ▼
Tool Layer
      │
      ▼
LLM Wrapper (OpenAI)

The architecture separates responsibilities into:

Layer	Responsibility
API Layer	FastAPI endpoints
Schemas	Input validation using Pydantic
Tools	Writing utilities
LLM Wrapper	OpenAI integration
Project Structure
creative-writing-mcp
│
├── main.py           # FastAPI server
├── schemas.py        # Request schemas
├── tools.py          # Writing tool implementations
├── llm.py            # OpenAI wrapper
├── requirements.txt
├── README.md
└── .env              # Environment variables
Installation
1. Clone the repository
git clone <your_repo_url>
cd creative-writing-mcp
2. Create a virtual environment
python -m venv venv
source venv/bin/activate

Windows

venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
Environment Setup

Create a .env file in the project root.

OPENAI_API_KEY=your_openai_api_key

The server loads environment variables using python-dotenv.

Running the Server

Start the FastAPI server using Uvicorn:

uvicorn main:app --reload

Server will start at:

http://127.0.0.1:8000
API Documentation

FastAPI automatically provides interactive documentation.

Open:

http://127.0.0.1:8000/docs

This Swagger UI allows you to test all endpoints directly from the browser.

Available Tools
Generate Plot Outline

Creates a structured five-act story outline.

Endpoint

POST /tools/generate_plot_outline

Request Example

{
  "genre": "Sci-Fi",
  "theme": "AI rebellion",
  "tone": "dark"
}
Create Character Arc

Generates a character development arc.

Endpoint

POST /tools/create_character_arc

Request Example

{
  "character_name": "Aria",
  "genre": "Fantasy",
  "theme": "destiny vs free will"
}
Inject Plot Twist

Adds an unexpected but logical twist to an existing story plot.

Endpoint

POST /tools/inject_plot_twist

Request Example

{
  "current_plot": "A detective hunts a serial killer in a futuristic city."
}
Analyze Emotional Flow

Analyzes emotional pacing and structure of a story.

Endpoint

POST /tools/analyze_emotional_flow

Request Example

{
  "story_text": "The hero loses everything but slowly regains hope."
}
Example Curl Request
curl -X POST http://127.0.0.1:8000/tools/generate_plot_outline \
-H "Content-Type: application/json" \
-d '{
  "genre": "Fantasy",
  "theme": "good vs evil",
  "tone": "epic"
}'
Technologies Used

Python

FastAPI

OpenAI API

Pydantic

Uvicorn

python-dotenv
