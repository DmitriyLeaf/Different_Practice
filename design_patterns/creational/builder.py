class Director:
    def __init__(self):
        self.builder = None

    def constructHouse(self, builder):
        self.builder = builder
        self.builder.foundation()
        self.builder.floor()
        self.builder.walls()
        self.builder.roof()

#Abstract interface for creating parts of a Product object
class Builder:
    def __init__(self):
        self.product = Product()

    def foundation(self):
        raise NotImplementedError()

    def floor(self):
        raise NotImplementedError()
    
    def walls(self):
        raise NotImplementedError()
    
    def roof(self):
        raise NotImplementedError()

class BigHouseBuilder(Builder):
    def foundation(self):
        print "The foundation is ready"

    def floor(self):
        print "The floor is ready"

    def walls(self):
        print "The walls is ready"

    def roof(self):
        print "The roof is redy"

class Product:
    raise NotImplementedError()

big_house_builder = BigHouseBuilder()
director = Director()
director.constructHouse(big_house_builder)
product = big_house_builder.product