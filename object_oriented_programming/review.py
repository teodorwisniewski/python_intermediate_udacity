
class Review:

    def __init__(self, description):
        self.description = description

    def __str__(self):
        return f"Review({self.description})"