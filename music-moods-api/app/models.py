from pydantic import BaseModel

class Song(BaseModel):
    title: str
    artist: str
    album: str
    cover_url: str
    media_url: str

class Recommendation(BaseModel):
    emotion: str
    song_recommendation: Song 