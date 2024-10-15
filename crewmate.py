'''
    Python file to implement the class CrewMate
'''
import heap


class CrewMate:
    '''
    Class to implement a crewmate
    '''

    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''

        # Write your code here
        self.t_list = []
        self.total_load = 0

    # Add more methods if required

    def assign_treasure(self, treasure, current_time):
        self.t_list.append(treasure)
        self.total_load += treasure.t_size()

    def remaining_load(self):
        return self.total_load

    def get_treasures(self):
        return self.t_list