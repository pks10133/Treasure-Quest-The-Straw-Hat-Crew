'''
    Python file to implement the Treasure class
'''


class Treasure:
    '''
    Class to implement a treasure
    '''

    def __init__(self, id, size, arrival_time):
        '''
        Arguments:
            id : int : The id of the treasure (unique positive integer for each treasure)
            size : int : The size of the treasure (positive integer)
            arrival_time : int : The arrival time of the treasure (non-negative integer)
        Returns:
            None
        Description:
            Initializes the treasure
        '''

        # DO NOT EDIT THE __init__ method
        self.id = id
        self.size = size
        self.arrival_time = arrival_time
        self.completion_time = None

    # You can add more methods if required

    def t_size(self):
        return self.size

    def set_completion_time(self, time):
        self.completion_time = time

    def get_completion_time(self):
        return self.completion_time

    def get_id(self):
        return self.id

    def helper_weight(self, current_time, arg1):
        return current_time - self.arrival_time - arg1