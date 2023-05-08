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

    #def step_move(self):

    #def step_breed(self):
    
    def run(self, num_timesteps=100):
        self.display()
        for _ in range(num_timesteps):
            self.timestep += 1
            self.step_move()
            self.display()
            self.step_breed()
            self.display()

if __name__ == '__main__':
    safari = CircleOfLife(5,5)
