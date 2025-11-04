from random import choice
import time


def returnStage() -> str:
    # time.sleep(2.5)
    print(choice(['awake', 'N1', 'N2', 'N3', 'REM']))
    return choice(['awake', 'N1', 'N2', 'N3', 'REM'])

# time.sleep(2.5)
# print(choice(['awake', 'N1', 'N2', 'N3', 'REM']))
# return choice(['awake', 'N1', 'N2', 'N3', 'REM'])