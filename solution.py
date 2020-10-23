from game import State


class Solver:
    def __init__(self, root: State, goal: State):
        self.root = root
        self.goal = goal
        self.branch: dict[State, Solver[State]] = {}

    def push(self, value: State):
        self.branch[value] = Solver(value, self.goal)

    def populate(self) -> None:
        for state in self.root.step():
            self.push(state)
            if state.sid() != self.goal.sid():
                self.branch[state].populate()

    def __iter__(self):
        return iter(self.branch.values())

    def __str__(self, w=2):
        value = str(self.root)
        bs = '\n'.join(' ' * w + b.__str__(w + 2) for b in self)
        return '\n'.join([value, bs]) if bs else value


def solution() -> list[str]:
    curr = State((3, 3), (0, 0))
    goal = State((0, 0), (3, 3))
    path = []
    while True:
        path.append(curr.sid())
        for branch in curr.step():
            if branch.sid() == goal.sid():
                path.append(branch.sid())
                return path
            curr = branch


if __name__ == '__main__':
    tree = Solver(
        State((3, 3), (0, 0)),
        State((0, 0), (3, 3)),
    )
    tree.populate()
    print(tree)
    print()

    [print(step) for step in solution()]
