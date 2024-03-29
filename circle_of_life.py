from animal import Animal

def print_TOO(todo):
    print(f'<<<NOT IMPLEMENTED: {todo}>>>')

class CircleOfLife:
    def __init__(self,world_size,num_zebras,num_lions):
        self.occupancy = [[False for _ in range(world_size)]
                          for _ in range(world_size)]
        print_TOO('get random empty coordinates')
        self.zebras = [Animal(0,0) for _ in range(num_zebras)]
        self.lions = [Animal(0,0) for _ in range(num_lions)]
        print('Welcome to AIE Safari!!')
        print(f'\tworld size = {world_size}')
        print(f'\tnumber of zebras = {len(self.zebras)}')
        print(f'\tnumber of lines = {len(self.lions)}')

    def display(self):
        print(f'clock: {self.timestep}')
        print_TOO('display')
        key = input('enter [q] to quit:')
        if key == 'q':
            exit()

    def step_move(self):
        print_TODO('step_move()')
        for zebra in self.zebras:
            print_TODO('get empty neighbor')
            direction = 'left'
            zebra.move(direction)
        for lion in self.lions:
            print_TODO('get neighboring zebra')
            print_TODO('move to zebra if found, else move to empty')
            print_TODO('get empty neighbor')
            direction = 'left'
            lion.move(direction)

    def step_breed(self):
        print_TODO('step_breed()')
        for animal in self.zebras +self.lions:
            print_TODO('get empty neighbor')
            x, y = 0, 0
            animal.breed(x, y)
    
    def run(self, num_timesteps=100):
        self.display()
        for _ in range(num_timesteps):
            self.timestep += 1
            self.step_move()
            self.display()
            self.step_breed()
            self.display()

if __name__ == '__main__':
    safari = CircleOfLife(5,5,2)
