class Owner:
    '''
    Класс собственника помещения
    '''

    def __init__(self, house: int, room: int, email=None):
        self.house = house
        self.room = room
        self.email = email

    def __str__(self):
        return f'Собственник дом № {self.house}, квартира № {self.room}'
