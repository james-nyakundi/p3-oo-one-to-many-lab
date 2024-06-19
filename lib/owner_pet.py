class Pet:
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all_pets = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type.lower()
        
        if self.pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Allowed types are {', '.join(self.PET_TYPES)}")

        self.owner = owner
        self.all_pets.append(self)

    @classmethod
    def all(cls):
        return cls.all_pets

    def set_owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception(f"{owner} is not of type Owner")
        self.owner = owner

    def __repr__(self):
        return f"Pet(name='{self.name}', pet_type='{self.pet_type}', owner='{self.owner.name if self.owner else None}')"

    pass

class Owner:
    
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception(f"{pet} is not of type Pet")
        self._pets.append(pet)
        pet.set_owner(self)

    def get_sorted_pets(self):
        sorted_pets = sorted(self._pets, key=lambda pet: pet.name)
        return sorted_pets

    pass