class Automaton(object):

    automat = {
        'q1': {
            '0': 'q1',
            '1': 'q2',
        },
        'q2': {
            '0': 'q3',
            '1': 'q2',
        },
        'q3': {
            '0': 'q2',
            '1': 'q3',
        },
    }
    
    def __init__(self):
        self.states = []

    def read_commands(self, commands, state='q1'):
        return self.read_commands(commands[1:], state=self.automat[state][commands[0]]) if commands else state == 'q2'

my_automaton = Automaton()

