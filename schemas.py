from pydantic import BaseModel


class StoryRequest(BaseModel):
    genre: str
    theme: str
    tone: str


class CharacterRequest(BaseModel):
    character_name: str
    genre: str
    theme: str


class TwistRequest(BaseModel):
    current_plot: str


class EmotionalAnalysisRequest(BaseModel):
    story_text: str