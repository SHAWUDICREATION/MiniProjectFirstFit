First Fit Memory Allocation Algorithm

Description

      This project implements the First Fit Algorithm for dynamic memory allocation. The algorithm allocates processes to the first available memory block that is large enough to accommodate the process. It highlights the importance of efficient memory utilization in operating systems.

Features

  Accepts user-defined memory blocks and process sizes.

  Dynamically allocates processes to memory blocks using the First Fit Algorithm.

  Displays step-by-step memory allocation and the status of memory blocks after each allocation.

  Provides a final summary of the memory state (allocated and free blocks).

How It Works

Input:

  The user enters the number of memory blocks and their respective sizes.

  The user enters the number of processes and their sizes.

Processing:

  The First Fit Algorithm attempts to allocate each process to the first memory block large enough to accommodate it.

  Updates the size of the memory block upon allocation.

  Tracks the memory state after each allocation step.

Output:

  Initial state of memory blocks.

  Allocation details for each process.

  Step-by-step memory status updates.

  Final state of memory blocks.

Example

  Input:
  Enter the number of memory blocks: 3
      Enter the sizes of the memory blocks:
      Block 1 size (in KB): 100
      Block 2 size (in KB): 200
      Block 3 size (in KB): 300

 Enter the number of processes: 2
      Enter the sizes of the processes:
      Process A size (in KB): 150
      Process B size (in KB): 250
      
  Output:
  Initial Memory Blocks:
      Block 1: 100 KB
      Block 2: 200 KB
      Block 3: 300 KB
      
  Processes to be Allocated:
      Process A requires 150 KB
      Process B requires 250 KB
      
  Allocation Process:
      Process A is allocated to Block 2.
      Process B is allocated to Block 3.
      
   Step-by-Step Memory Status:
      After allocating Process A:
        Block 1: 100 KB
        Block 2: 50 KB
        Block 3: 300 KB
      After allocating Process B:
        Block 1: 100 KB
        Block 2: 50 KB
        Block 3: 50 KB
      
  Final Memory State:
      Block 1: 100 KB (free)
      Block 2: 50 KB (free)
      Block 3: 50 KB (free)
