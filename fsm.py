import gui
bedFrequency = 0

def go(currentStage):
    if currentStage == "awake":
        bedFrequency = 8
        gui.displayFrequency(bedFrequency)
    elif currentStage == "N1":
        bedFrequency = 7
        gui.displayFrequency(bedFrequency)
    elif currentStage == "N2":
        bedFrequency = 4
        gui.displayFrequency(bedFrequency)
    elif currentStage == "N3":
        bedFrequency = 2
        gui.displayFrequency(bedFrequency)
    elif currentStage == "REM":
        bedFrequency = 1
        gui.displayFrequency(bedFrequency)
    print(currentStage)