spin = input()
charge = input()

particles = ["Strange", "Charm", "Electron", "Muon", "Photon"]
strange = ["Quark", "1/2", "-1/3"]
charm = ["Quark", "1/2", "2/3"]
electron = ["Lepton", "1/2", "-1"]
muon = ["Lepton", "1/2", "0"]
photon = ["Boson", "1", "0"]

if spin in strange and charge in strange:
    print("Strange Quark")
elif spin in charm and charge in charm:
    print("Charm Quark")
elif spin in electron and charge in electron:
    print("Electron Lepton")
elif spin in muon and charge in muon:
    print("Muon Lepton")
elif spin in photon and charge in photon:
    print("Photon Boson")