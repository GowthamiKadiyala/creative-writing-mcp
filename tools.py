from llm import generate_text


async def generate_plot_outline(genre, theme, tone):
    prompt = f"""
    Create a structured 5-act plot outline.
    Genre: {genre}
    Theme: {theme}
    Tone: {tone}
    """

    result = await generate_text(prompt)

    return {
        "genre": genre,
        "theme": theme,
        "outline": result
    }


async def create_character_arc(character_name, genre, theme):
    prompt = f"""
    Create a full character arc for:
    Name: {character_name}
    Genre: {genre}
    Theme: {theme}
    """

    result = await generate_text(prompt)

    return {
        "character": character_name,
        "arc": result
    }


async def inject_plot_twist(current_plot):
    prompt = f"""
    Inject an unexpected but logical plot twist into:
    {current_plot}
    """

    result = await generate_text(prompt)

    return {
        "twist": result
    }


async def analyze_emotional_flow(story_text):
    prompt = f"""
    Analyze the emotional pacing of this story:
    {story_text}
    """

    result = await generate_text(prompt)

    return {
        "analysis": result
    }