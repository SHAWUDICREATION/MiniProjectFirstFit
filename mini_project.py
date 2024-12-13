def first_fit(memory_blocks, process_sizes):
    # This function implements the First Fit memory allocation algorithm.
    # It takes a list of memory block sizes and a list of process sizes as input.
    # The function returns two results:
    # 1. allocations: A list indicating which block each process is allocated to.
    # 2. memory_status_steps: A list of memory block statuses after each allocation step.

    # Initialize allocations list with -1 (indicating no allocation)
    allocations = [-1] * len(process_sizes)

    # This list will store the status of memory blocks after each allocation step
    memory_status_steps = []

    # Iterate over each process to allocate it to the first fitting memory block
    for i, process_size in enumerate(process_sizes):
        for j, block_size in enumerate(memory_blocks):
            # Check if the block can fit the process
            if block_size >= process_size:
                allocations[i] = j + 1  # Assign block number (1-based index)
                memory_blocks[j] -= process_size  # Reduce available memory in the block
                break

        # Record the memory status after each allocation step5
        memory_status_steps.append(memory_blocks[:])

    return allocations, memory_status_steps

# Input: Number of memory blocks and their sizes
num_blocks = int(input("Enter the number of memory blocks: "))
initial_memory_blocks = []
print("Enter the sizes of the memory blocks:")
for i in range(num_blocks):
    size = int(input(f"Block {i + 1} size (in KB): "))
    initial_memory_blocks.append(size)

# Input: Number of processes and their sizes
num_processes = int(input("\nEnter the number of processes: "))
process_sizes = []
print("Enter the sizes of the processes:")
for i in range(num_processes):
    size = int(input(f"Process {chr(65 + i)} size (in KB): "))
    process_sizes.append(size)

# Call the First Fit allocation function
updated_memory_blocks = initial_memory_blocks[:]
allocations, memory_status_steps = first_fit(updated_memory_blocks, process_sizes)

# Display Initial Memory State
print("\nInitial Memory Blocks:")
for i, size in enumerate(initial_memory_blocks):
    print(f"Block {i + 1}: {size} KB")

# Display the list of processes to be allocated
print("\nProcesses to be Allocated:")
for i, process_size in enumerate(process_sizes):
    print(f"Process {chr(65 + i)} requires {process_size} KB")

# Display Allocation Results
print("\nAllocation Process:")
for i, allocation in enumerate(allocations):
    if allocation != -1:
        print(f"Process {chr(65 + i)} is allocated to Block {allocation}.")
    else:
        print(f"Process {chr(65 + i)} could not be allocated.")

# Display Step-by-Step Memory Status
print("\nStep-by-Step Memory Status:")
for step, status in enumerate(memory_status_steps):
    print(f"After allocating Process {chr(65 + step)}:")
    for i, size in enumerate(status):
        print(f"  Block {i + 1}: {size} KB")

# Display Final Memory State
print("\nFinal Memory State:")
for i, size in enumerate(updated_memory_blocks):
    status = "free" if size > 0 else "fully allocated"
    print(f"Block {i + 1}: {size} KB ({status})")
