from app.models import Recommendation

class SongRecommendation:
    def recommend(self, emotion):
        if emotion == "Happy":
            return Recommendation(emotion="Happy", song_recommendation={"title": "Somos instantes",
                                                                        "artist": "Caloncho",
                                                                        "album": "Buen Pez",
                                                                        "cover_url": "https://udiscover.mx/cdn/shop/files/602445931200_Caloncho.jpg?v=1724956456&width=1200",
                                                                        "media_url": "https://open.spotify.com/track/4eWC4PIRnCAiSo028OWh62?si=6946bf5245bd4ab1"})  
        elif emotion == "Sad":
            return Recommendation(emotion="Sad", song_recommendation={"title": "The Night We Met",  
                                                                     "artist": "Lord Huron",
                                                                     "album": "Strange Trails",
                                                                     "cover_url": "https://upload.wikimedia.org/wikipedia/en/e/e5/Strange_Trails_cover.jpg",
                                                                     "media_url": "https://open.spotify.com/track/3hRV0jL3vUpRrcy398teAU?si=c53283aef05c4984"})