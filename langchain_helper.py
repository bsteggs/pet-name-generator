from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def generate_pet_names(
    animal_type: str,
    pet_color: str,
    style: str,
    personality: str,
    count: int,
) -> str:

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.8,
    )

    prompt = ChatPromptTemplate.from_template(
        """You are a creative pet naming assistant.

Pet type: {animal_type}
Pet color: {pet_color}
Name style: {style}
Personality traits: {personality}

Return EXACTLY {count} names as a numbered list.

Rules:
- Names must match the personality
- 1–2 words max
- No explanations
- No blank lines
"""
    )

    chain = prompt | llm | StrOutputParser()

    return chain.invoke(
        {
            "animal_type": animal_type,
            "pet_color": pet_color,
            "style": style,
            "personality": personality,
            "count": count,
        }
    )