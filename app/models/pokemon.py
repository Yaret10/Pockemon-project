class Pokemon:
    def __init__(self, _id, name, weight, height, base_experience, order) -> None:
        self._id = _id
        self.name = name
        self.weight = weight
        self.height = height
        self.base_experience = base_experience
        self.order = order

    def to_json(self):
        json = {
            "_id": self._id,
            "name": self.name,
            "weight": self.weight,
            "height": self.height,
            "base_experience": self.base_experience,
            "order": self.order
        }

        return json