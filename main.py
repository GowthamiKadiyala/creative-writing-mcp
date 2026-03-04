from fastapi import FastAPI, HTTPException
from schemas import (
    StoryRequest,
    CharacterRequest,
    TwistRequest,
    EmotionalAnalysisRequest
)
from tools import (
    generate_plot_outline,
    create_character_arc,
    inject_plot_twist,
    analyze_emotional_flow
)

app = FastAPI()


TOOLS = [
    {
        "name": "generate_plot_outline",
        "description": "Generates structured plot outline",
    },
    {
        "name": "create_character_arc",
        "description": "Creates character development arc",
    },
    {
        "name": "inject_plot_twist",
        "description": "Adds an unexpected plot twist",
    },
    { 
        "name": "analyze_emotional_flow",
        "description": "Analyzes emotional pacing",
    }
]

@app.get("/")
def home():
    return {"message": "Creative Writing MCP Server Running"}

@app.get("/tools")
def list_tools():
    return TOOLS


@app.post("/tools/generate_plot_outline")
async def call_plot(request: StoryRequest):
    return await generate_plot_outline(
        request.genre,
        request.theme,
        request.tone
    )


@app.post("/tools/create_character_arc")
async def call_arc(request: CharacterRequest):
    return await create_character_arc(
        request.character_name,
        request.genre,
        request.theme
    )


@app.post("/tools/inject_plot_twist")
async def call_twist(request: TwistRequest):
    return await inject_plot_twist(request.current_plot)


@app.post("/tools/analyze_emotional_flow")
async def call_emotion(request: EmotionalAnalysisRequest):
    return await analyze_emotional_flow(request.story_text)