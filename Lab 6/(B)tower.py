def tower_of_hanoi(n, source, destination, temporary, step_count):
    """
    Parameters:
    - n: The number of disks to move.
    - source: The peg from which to move the disks.
    - destination: The peg to which to move the disks.
    - temporary: The peg to use as a temporary holding area.
    - step_count: The number of steps taken so far.

    Returns:
    - The number of steps taken to solve the problem.
    """
    if n == 1:
        step_count += 1
        print(f"{step_count}. Move disk 1 from {source} to {destination}")
        return step_count
    else:
        step_count = tower_of_hanoi(n - 1, source, temporary, destination, step_count)
        step_count += 1
        print(f"{step_count}. Move disk {n} from {source} to {destination}")
        step_count = tower_of_hanoi(n - 1, temporary, destination, source, step_count)
        return step_count


step_count = 0
step_count = tower_of_hanoi(3, "A", "C", "B", step_count)
print(f"Total number of steps: {step_count}")
