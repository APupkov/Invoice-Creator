from Owner import Owner


class OwnerList:
    '''
    Создает и содержит список всех собственников
    '''

    def __init__(self, owners: tuple):

        self.owners = []
        for owner in owners:
            house = owner[0]
            room = owner[1]
            try:
                email = owner[2]
            except(IndexError):
                email = None
            self.owners.append(Owner(house, room, email))

    def __iter__(self):
        return OwnerIterator(self.owners)


class OwnerIterator:

    def __init__(self, owners: list[Owner]):

        self.owners = owners
        self.count = 0
        self.maxcount = len(self.owners)

    def __iter__(self):
        return self

    def __next__(self) -> Owner:
        if self.count < self.maxcount:
            result = self.owners[self.count]
            self.count += 1
            return result

        raise StopIteration
