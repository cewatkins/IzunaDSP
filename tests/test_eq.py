# IzunaDSP
from izunadsp.core.manager import Manager
from izunadsp.parts.apply_eq import ApplyEQ

man = Manager()
eq = ApplyEQ()
eq.set_eq([2, 2, 0, 1.1, 0.5])

man.register_part(eq)

man.passthrough("dubstep.wav", "dubstep_eq.wav")
