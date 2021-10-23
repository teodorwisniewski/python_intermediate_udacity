"""Module that defines the QuoteModel object."""


class QuoteModel:
    """Quote model class that contains quote data."""

    def __init__(self, body: str, author:str):
        """Create a new QuoteModel object.

        @param body: content of a quote
        @param author: author's name
        """
        self.body = body
        self.author = author

    def __repr__(self) -> str:
        """Representation of the QuoteModel object.

        @return: string object that represents a quote and its author.
        """
        return f'"{self.body}" - {self.author}'
