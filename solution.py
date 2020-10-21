from game import State


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
	[print(step) for step in solution()]
