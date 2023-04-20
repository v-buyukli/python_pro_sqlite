from faker import Faker


def generate_tracks(number=10):
    faker = Faker()
    tracks = [
        {
            "track_name": faker.sentence(3).replace(".", ""),
            "track_time": faker.pyint(min_value=120, max_value=500)
        }
        for _ in range(number)
    ]
    return tracks
