class FlashcardDAL:
    def __init__(self, session):
        self.session = session

    async def list(self): ...
