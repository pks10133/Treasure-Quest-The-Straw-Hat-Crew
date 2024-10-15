'''
    This file contains the class definition for the StrawHat class.
'''

import crewmate
import heap
import treasure

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''

    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''

        # Write your code here
        self.heap = heap.Heap(lambda x, y: x.remaining_load() < y.remaining_load(), [])
        self.c_list = []
        for _ in range(m):
            c = crewmate.CrewMate()
            self.heap.insert(c)
            self.c_list.append(c)
        self.current_time = 0
        self.treasure_list = []
        self.m = m

    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''

        # Write your code here
        self.current_time = max(self.current_time, treasure.arrival_time)
        best_crewmate = self.heap.extract()
        best_crewmate.assign_treasure(treasure, self.current_time)
        self.heap.insert(best_crewmate)
        self.treasure_list.append(treasure)

    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''

        # Write your code here
        t_list = []
        for c in self.c_list:
            ct_list = c.get_treasures()
            ct_list.sort(key=lambda x:x.arrival_time)
            ct_heap = heap.Heap(lambda x, y: x[0].helper_weight(self.current_time, x[1]) > y[0].helper_weight(self.current_time, y[1]) or (x[0].helper_weight(self.current_time, x[1]) == y[0].helper_weight(self.current_time, y[1]) and x[0].get_id() < y[0].get_id()),[])
            for i in range(len(ct_list)):
                t = ct_list[i]
                ct_heap.insert((t,t.t_size()))
                curr_time = t.arrival_time
                if i != len(ct_list) - 1:
                    while curr_time < ct_list[i+1].arrival_time and ct_heap.top() != None:
                        t1 = ct_heap.extract()
                        if ct_list[i+1].arrival_time - curr_time >= t1[1]:
                            curr_time += t1[1]
                            t1[0].set_completion_time(curr_time)
                            t_list.append(t1[0])
                        else:
                            ct_heap.insert((t1[0], t1[1]-(ct_list[i+1].arrival_time - curr_time)))
                            curr_time = ct_list[i+1].arrival_time
                else:
                    while ct_heap.top() != None:
                        t1 = ct_heap.extract()
                        curr_time += t1[1]
                        t1[0].set_completion_time(curr_time)
                        t_list.append(t1[0])
        t_list.sort(key=lambda x:x.get_id())
        return t_list

    # You can add more methods if required