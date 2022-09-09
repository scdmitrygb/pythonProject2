import enum


class UserEnum(enum.Enum):
    client = ("К")
    admin = ("А")
    dealer = ("Д")

    def __init__(self, letter):
        self.letter = letter

    def can_transition(self, new_state):
        return new_state.name in self.transitions


print('Name:', UserEnum.in_progress)
print('Value:', UserEnum.in_progress.value)
print('Custom attribute:', UserEnum.in_progress.transitions)
print('Using attribute:',
      UserEnum.in_progress.can_transition(UserEnum.new))
