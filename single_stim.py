from neuron import h
from neuron.units import ms, mV, μM
import matplotlib.pyplot as plt
h.load_file('stdrun.hoc')

soma = h.Section(name = "Soma")
soma.L = soma.diam = 20
soma.insert("hh") # hodgkin-huxley; derivation needed

stim = h.IClamp(soma(0.5)) #pulse
stim.delay, stim.dur, stim.amp = 5, 1, 0.5
# ^^ 5 sec delay before 0.5A pulse lasting 1s

v = h.Vector().record(soma(0.5)._ref_v)
t = h.Vector().record(h._ref_t)

h.finitialize(-65) #resting potential -65mV
h.continuerun(40)
print(f"peak V: {max(v)} mV")

plt.plot(t, v)
plt.xlabel("time (ms)")
plt.ylabel("mV")
plt.show()
