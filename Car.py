# Creating a Car class that can be used to instantiate vehicles namely: Honda, GM, Opel, General etc
# It accepts various arguments namely model, name of vehicle etc as long as they have already been set

class Car(object):


    def __init__(self, name='General', model='GM' ,car_type='saloon' ):
        self.car_type = car_type
        self.model = model
        self.name = name
        self.speed = 0

        if name == 'Porshe' or name == 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if car_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4
        
    def drive(self, moving_man):
        return moving_man

    def drive(self, spd):
        if self.car_type == 'trailer':
            self.speed = 77
        else:
            self.speed = 10 ** spd

        return self

    def doors(self, num_of_doors):
        pass

    def wheels(self, num_of_wheels):
        return num_of_wheels

    def is_saloon(self):
        if self.car_type ==  'trailer':
            return False
        else:
          return True