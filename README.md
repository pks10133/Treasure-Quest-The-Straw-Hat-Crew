#Straw Hat Treasure Management System


---

# Straw Hat Treasure Management System

**Project Overview**  
The Straw Hat pirates, led by their fearless captain, are on a relentless quest for adventure and treasure. As the crew's Treasurer, you are responsible for managing an extensive collection of treasures they have gathered. Your mission is to ensure that every piece of treasure is efficiently organized and processed by the crewmates, allowing the crew to stay organized on their journey to the One Piece.

## 1. Background  
The Straw Hat pirates have accumulated a wide array of treasures during their adventures. Each member of the crew volunteers to manage these treasures, but they can only tackle one treasure pile at a time. Your goal is to lead your crewmates in managing the workload effectively, ensuring that no treasure is overlooked, especially since treasures arrive at different times and sizes.

## 2. Modeling  
The management of treasures collected by the Straw Hat pirates is modeled as a scheduling problem with multiple crewmates. Below are the key elements defined in this model:

### 2.1 Definitions
- **m**: The number of crewmates available to manage the treasure.
- Each piece of treasure \( j \) is characterized by:
  - **Treasure ID** \( id_j \): A unique positive integer for identifying each piece of treasure.
  - **Treasure Size** \( size_j \): The time (a positive integer) required to process the treasure.
  - **Arrival Time** \( arrival_j \): The time (a positive integer) at which the treasure becomes available for processing.

### 2.2 State of the System  
At any given time \( t \):
- Each crewmate maintains a list of treasure pieces assigned to them.
- The **Remaining Size** of a treasure piece \( j \) is given by:
  \[
  \text{Remaining Size} = \text{Original Size}(size_j) - \text{Processed Time}
  \]
- The **load** on a crewmate is defined as the total remaining size of the treasures in their queue. Each crewmate can only process one treasure at a time.

### 2.3 Scheduling Policy  
When a new piece of treasure arrives, the following scheduling policies are applied:
- **Treasure Assignment**: The newly arrived treasure is assigned to the crewmate with the least current load. If there are multiple crewmates with the same load, the treasure can be assigned to any one of them.
- **Treasure Processing**: Each crewmate processes the treasure \( j \) that maximizes the following priority:
  \[
  \text{Priority}(j) = (\text{Wait Time}(j) - \text{Remaining Size}(j))
  \]
  Where:
  \[
  \text{Wait Time}(j) = t - arrival_j
  \]

### 2.4 Example  
Consider a scenario where there are 3 crewmates managing 4 pieces of treasure. A flow diagram could represent the processing states at different times, showing which treasure is currently being worked on.

## 3. Requirements  
You are expected to implement the following classes and functionalities:

### 3.1 Heap  
You need to implement a heap from scratch that accommodates any general comparison function. It should be a min-heap based on the comparison function, maintaining the following specifications:
- **init**: Time complexity of \( O(n) \) for initializing the heap using the provided array.
- **insert**: Time complexity of \( O(\log n) \) for adding a new element.
- **extract**: Time complexity of \( O(\log n) \) for removing and returning the top element.
- **top**: Time complexity of \( O(1) \) for returning the top element without removing it.

### 3.2 StrawHatTreasury  
You are required to implement the class `StrawHatTreasury` with the following specifications:
- **init**: Time complexity of at most \( O(m) \) for initializing the treasury and crewmates.
- **add_treasure**: Time complexity of at most \( O(\log n + \log m) \) for adding a treasure and scheduling its processing.
- **get_completion_time**: Time complexity of \( O(n(\log n + \log m)) \) for returning a list of treasures sorted by their IDs after updating completion times.

## 4. Clarifications  
1. Cross imports between the provided files are allowed, but no additional libraries may be imported.
2. Avoid using hash-based data structures such as dictionaries and sets; implement all structures using arrays.
3. Ensure the time complexity of your algorithms is not dependent on the size of the treasure or arrival time.
4. Functions must return output instead of printing it directly.
5. Inputs will always be valid; no validity checks are needed.
6. You may use Python's built-in sort function only for sorting in `get_completion_time`.
7. No additional files can be created; use the provided `custom.py` for any additional functions or classes.
8. The recursion limit will be adjusted in the autograder, so focus on achieving the expected time complexity.

---

