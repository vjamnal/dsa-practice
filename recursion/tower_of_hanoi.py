# problem: Tower of Hanoi
# approach: Recursion
# time: O(2^n)
# space: O(n) for recursion stack

"""
Tower of Hanoi
Classic recursion problem - move n disks from source to destination.
"""

def tower_of_hanoi(n, source='A', destination='C', auxiliary='B', moves=None):
    """
    Recursive solution - O(2^n) time, O(n) space
    Returns list of moves
    """
    if moves is None:
        moves = []
    
    if n == 1:
        moves.append(f"Move disk 1 from {source} to {destination}")
        return moves
    
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, destination, moves)
    
    # Move nth disk from source to destination
    moves.append(f"Move disk {n} from {source} to {destination}")
    
    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, destination, source, moves)
    
    return moves


def count_moves(n):
    """
    Calculate minimum number of moves needed - O(1)
    Formula: 2^n - 1
    """
    return 2 ** n - 1


if __name__ == "__main__":
    print("Tower of Hanoi Tests:")
    n = 3
    moves = tower_of_hanoi(n)
    print(f"\nSolution for {n} disks:")
    for move in moves:
        print(move)
    print(f"\nTotal moves: {len(moves)}")
    print(f"Expected moves: {count_moves(n)}")
