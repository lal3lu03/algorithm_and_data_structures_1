from typing import List, Tuple

# Using constants might make this more readable.
START = 'S'
EXIT = 'X'
VISITED = '.'
OBSTACLE = '#'
PATH = ' '


class Maze:
    """Maze object, used for demonstrating recursive algorithms."""

    def __init__(self, maze_str: str):
        """Initialize Maze.

        Args:
            maze_str (str): Maze represented by a string, 
            where rows are separated by newlines (\\n).

        Raises:
            ValueError, if maze_str is invalid, i.e. if it is not the correct type, 
            if any of its dimensions is less than three, or if it contains 
            characters besides {'\\n', ' ', '#'}.
        """
        val = ["\n", " ", "#"]
        for character in maze_str:
            if character not in val:
                raise ValueError("abc")

        # We internally treat this as a List[List[str]], as it makes indexing easier.
        self._maze = list(list(row) for row in maze_str.splitlines())

        if len(self._maze) < 3 or len(self._maze[0]) < 3:
            raise ValueError("bce")

        self._exits: List[Tuple[int, int]] = []
        self._max_recursion_depth = 0

    def find_exits(self, start_x: int, start_y: int, depth: int = 0):
        """Find and save all exits into `self._exits` using recursion, save 
        the maximum recursion depth into 'self._max_recursion_depth' and mark the maze.

        An exit is an accessible from S empty cell on the outer rims of the maze.

        Args:
            start_x (int): x-coordinate to start from. 0 represents the topmost cell.
            start_y (int): y-coordinate to start from; 0 represents the leftmost cell.
            depth (int): Depth of current iteration.

        Raises:
            ValueError: If the starting position is out of range or not walkable path.
        """
        if self._maze[start_x][start_y] == OBSTACLE:
            raise ValueError("You are in a Wall")

        if not (0 <= start_x < len(self._maze) or 0 <= start_y < len(self._maze[0])):
            raise ValueError('Out of range')

        if self._maze[start_x][start_y] == START or self._maze[start_x][start_y] == VISITED or self._maze[start_x][
            start_y] == EXIT:
            return

        if start_x == 0 or start_x == len(self._maze) - 1 or start_y == 0 or start_y == len(self._maze[0]) - 1:
            self._maze[start_x][start_y] = EXIT
            self._exits.append((start_x, start_y))
            if depth > 0:
                return

        if depth > 0 and self._maze[start_x][start_y] != START and self._maze[start_x][start_y] != EXIT:
            self._maze[start_x][start_y] = VISITED

        if depth == 0:
            self._maze[start_x][start_y] = START

        if depth > self._max_recursion_depth:
            self._max_recursion_depth = depth

        walk = [(0, 1), (1, 0), (1, 1), (-1, -1), (-1, 0), (0, -1), (1, -1), (-1, 1)]
        for i in walk:
            try:
                self.find_exits(start_x + i[0], start_y + i[1], depth + 1)
            except ValueError:
                pass

    @property
    def exits(self) -> List[Tuple[int, int]]:
        """List of tuples of (x, y)-coordinates of currently found exits."""
        return self._exits

    @property
    def max_recursion_depth(self) -> int:
        """Return the maximum recursion depth after executing find_exits()."""
        return self._max_recursion_depth

    def __str__(self) -> str:
        return '\n'.join(''.join(row) for row in self._maze)

    __repr__ = __str__
