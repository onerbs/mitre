from operator import add, sub


class Side:
    def __init__(self, o: int, x: int):
        self.o = o
        self.x = x

    def is_valid(self):
        if 0 < self.o < self.x:
            return False
        return self.o >= 0 and self.x >= 0

    def __str__(self):
        return 'O' * self.o + 'X' * self.x


class State:
    T = tuple[int, int]
    MOVES = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    def __init__(self, left: T, right: T, _phase=True, pid=''):
        self.ls = Side(*left)
        self.rs = Side(*right)
        self._phase = _phase
        self.pid = pid

    def step(self):
        lop = [add, sub][self._phase]
        rop = [sub, add][self._phase]
        moves = [State(
            (lop(self.ls.o, move[0]), lop(self.ls.x, move[1])),
            (rop(self.rs.o, move[0]), rop(self.rs.x, move[1])),
            not self._phase, self.sid()
        ) for move in State.MOVES]
        return [mv for mv in moves if (
            mv.sid() != '[OOOXXX:]'  # todo: save ref? ╮(￣_￣')╭
            and mv.sid() != self.pid
            and mv.is_valid())]

    def is_valid(self):
        return self.ls.is_valid() and self.rs.is_valid()

    def sid(self):
        return f'[{self.ls}:{self.rs}]'
