
import pickle
from typing import List
from prodict import Prodict

class Ram(Prodict):
    capacity: int
    unit: str
    type: str
    clock: int


class Computer(Prodict):
    name: str
    cpu_cores: int
    rams: List[Ram]

    def total_ram(self):
        return sum([ram.capacity for ram in self.rams])

class tst(dict):
    s1: str
    s2: int


tst1 = tst(
    {
        'name':
            'My Computer',
        'cpu_cores': 4,
        'rams': [
            {'capacity': 4,
             'unit': 'GB',
             'type': 'DDR3',
             'clock': 2400}
        ]
    })



comp1 = Computer.from_dict(
    {
        'name':
            'My Computer',
        'cpu_cores': 4,
        'rams': [
            {'capacity': 4,
             'unit': 'GB',
             'type': 'DDR3',
             'clock': 2400}
        ]
    })
print(comp1.rams)  # [{'capacity': 4, 'type': 'DDR3'}]

comp1.rams.append(Ram(capacity=8, type='DDR3'))
comp1.rams.append(Ram.from_dict({'capacity': 12, 'type': 'DDR3', 'clock': 2400}))

print(type(comp1))


path1 = "C:\\Users\\XT21586\\Documents\\document\\Data Stage\\export1\\data_mapping\\"
outfilename1 = path1 + "pickle1.pk1"
output = open(outfilename1, 'wb')
pickle.dump(comp1, output)
output.close()



print(comp1.rams)
# [
#   {'capacity': 4, 'unit': 'GB', 'type': 'DDR3', 'clock': 2400},
#   {'capacity': 8, 'type': 'DDR3'},
#   {'capacity': 12, 'type': 'DDR3', 'clock': 2400}
# ]

print(type(comp1.rams))
print(type(comp1.rams[0]))
