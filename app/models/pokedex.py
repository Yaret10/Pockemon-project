class Pokedex:
    def __init__(self, _id, name, descriptions) -> None:
        self._id = _id
        self.name = name
        self.descriptions = descriptions
    
    def to_json(self):
        json = {
            "_id": self._id,
            "name": self.name,
            "descriptions": self.descriptions
        }

        return json