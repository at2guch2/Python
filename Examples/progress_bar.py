from tqdm import tqdm
#from loguru import logger
import time


#logger.add("debug.log", rotation="1 MB")
#logger.info("Imports done...")
for i in tqdm(range(300), unit="it",ncols=100, colour='green'):
    time.sleep(0.01)
#logger.info("All executions done...")

# Test

# Progress bar 1: Default settings
for i in tqdm(range(300), colour='blue',ncols=100):
    time.sleep(0.01)

# Progress bar 2: Customized bar format and color
for i in tqdm(range(300), bar_format='[{elapsed}<{remaining}] {n_fmt}/{total_fmt} | {l_bar}{bar} {rate_fmt}{postfix}',
              colour='yellow',ncols=100):
    time.sleep(0.01)

# Progress bar 3: Customized bar format and color, leave=False
for i in tqdm(range(300), bar_format='[{elapsed}<{remaining}] {n_fmt}/{total_fmt} | {l_bar}{bar} {rate_fmt}{postfix}',
              colour='red', leave=True,ncols=100):
    time.sleep(0.01)

# Progress bar 4: Customized bar format and color, leave=False
for i in tqdm(range(300),
              bar_format='|{bar}|{l_bar}{n_fmt}/{total_fmt}|{elapsed}',
              colour="#f07d0a",ncols=100):  # [#00ff00, BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]
    time.sleep(0.01)
