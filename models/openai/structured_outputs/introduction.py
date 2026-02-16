from openai import OpenAI
from dotenv import load_dotenv
import os, rich
from pydantic import BaseModel

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


# represents the exact structure of the expected output
class AnimeInfo(BaseModel):
    title: str
    episodes: int
    start_year: int
    genre: str
    rating: float


# Getting the data
def get_anime_info(anime_name: str):
    response = client.responses.parse(
        model="gpt-4o-mini",
        input=[
            {"role": "system", "content": "You are an expert anime database."},
            {"role": "user", "content": f"Tell me about the anime '{anime_name}'."},
        ],
        text_format=AnimeInfo,
    )

    for output in response.output:
        if output.type != "message":
            raise Exception("Unexpected non message")
        for item in output.content:
            if item.type != "output_text":
                raise Exception("Unexpected output type")
            if not item.parsed:
                raise Exception("No parsed content found")

            anime = item.parsed

            print(f"Anime title: {anime.title}")
            print(f"Number of Episodes: {anime.episodes}")
            print(f"Start Year: {anime.start_year}")
            print(f"Genre: {anime.genre}")
            print(f"Rating: {anime.rating}")

            return anime


if __name__ == "__main__":
    anime_info = get_anime_info("Akane ga Kill!!")

# from openai import OpenAI
# from dotenv import load_dotenv
# import os
# from pydantic import BaseModel

# load_dotenv()
# api_key = os.getenv("OPENAI_API_KEY")
# client = OpenAI(api_key=api_key)


# # Represents the exact structure of the expected output
# class AnimeInfo(BaseModel):
#     title: str
#     episodes: int
#     start_year: int
#     genre: str
#     rating: float


# # Getting the data
# def get_anime_info(anime_name: str):
#     response = client.beta.chat.completions.parse(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "You are an expert anime database."},
#             {"role": "user", "content": f"Tell me about the anime '{anime_name}'."},
#         ],
#         response_format=AnimeInfo,
#     )

#     anime = response.choices[0].message.parsed

#     print(f"Anime title: {anime.title}")
#     print(f"Number of Episodes: {anime.episodes}")
#     print(f"Start Year: {anime.start_year}")
#     print(f"Genre: {anime.genre}")
#     print(f"Rating: {anime.rating}")

#     return anime


# if __name__ == "__main__":
#     anime_info = get_anime_info("solo leveling")
