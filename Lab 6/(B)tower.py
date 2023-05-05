# def tower_of_hanoi(n, source, destination, auxiliary):
#     """
#     A recursive function to solve the Tower of Hanoi problem.

#     Parameters:
#     - n: The number of disks to move.
#     - source: The peg from which to move the disks.
#     - destination: The peg to which to move the disks.
#     - auxiliary: The peg to use as a temporary holding area.

#     Returns:
#     - None. The function prints the moves needed to solve the problem.
#     """

#     if n == 1:
#         print(f"Move disk 1 from {source} to {destination}")
#     else:
#         tower_of_hanoi(n - 1, source, auxiliary, destination)
#         print(f"Move disk {n} from {source} to {destination}")
#         tower_of_hanoi(n - 1, auxiliary, destination, source)


# # Example usage:
# tower_of_hanoi(6, "A", "C", "B")


def tower_of_hanoi(n, source, destination, auxiliary, step_count):
    """
    A recursive function to solve the Tower of Hanoi problem.

    Parameters:
    - n: The number of disks to move.
    - source: The peg from which to move the disks.
    - destination: The peg to which to move the disks.
    - auxiliary: The peg to use as a temporary holding area.
    - step_count: The number of steps taken so far.

    Returns:
    - The number of steps taken to solve the problem.
    """
    if n == 1:
        step_count += 1
        print(f"{step_count}. Move disk 1 from {source} to {destination}")
        return step_count
    else:
        step_count = tower_of_hanoi(n - 1, source, auxiliary, destination, step_count)
        step_count += 1
        print(f"{step_count}. Move disk {n} from {source} to {destination}")
        step_count = tower_of_hanoi(n - 1, auxiliary, destination, source, step_count)
        return step_count


# Example usage:
step_count = 0
step_count = tower_of_hanoi(6, "A", "C", "B", step_count)
print(f"Total number of steps: {step_count}")
