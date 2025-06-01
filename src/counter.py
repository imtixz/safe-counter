import os
from filelock import FileLock

COUNTERS_DIR = 'counters'

class Counter:    
    @classmethod
    def _create(cls, name: str, x:int):
        os.makedirs(COUNTERS_DIR, exist_ok=True)
        Counter._append(name, x)

    @classmethod
    def _append(cls, name: str, x: int):
        with open(f'{COUNTERS_DIR}/{name}.txt', 'a') as f:
            f.write(f"INCREMENT {x}\n")

    @classmethod
    def _read(cls, name: str):
        total = 0

        filepath = os.path.join(COUNTERS_DIR, f"{name}.txt")
        if not os.path.exists(filepath):
            return 0
        
        # this ensures another thread cannot access this file while its being edited
        lock = FileLock(f'{filepath}.lock')

        with lock:
            with open(os.path.join(COUNTERS_DIR, f'{name}.txt'), 'r') as f:
                for line in f:
                    if not line.startswith('INCREMENT'):
                        continue
                    try:
                        _, value = line.strip().split()
                        total += int(value)
                    except ValueError:
                        continue

        return total
        
    def __init__(self):
        self.count: dict[str, int] = {}

        if not os.path.exists(COUNTERS_DIR):
            return

        for filename in os.listdir(COUNTERS_DIR):
            if not filename.endswith('.txt'):
                continue

            counter_name = filename[:-4]
            
            total = Counter._read(counter_name)
            self.count[counter_name] = total

    def increment(self, name: str, x: int):

        if name not in self.count:
            Counter._create(name, x)
            self.count[name] = x

        else:
            Counter._append(name, x)
            self.count[name] += x

    def read(self, name: str):
        if name not in self.count:
            return 0
        return self.count[name]