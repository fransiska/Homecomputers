#!/usr/bin/env python3

from datetime import datetime
import os
import numpy as np

def main():
    print("Changed files", os.environ.get("CHANGED_FILES"))
    a = np.arange(15).reshape(3, 5)
    print("array", a)
    with open("converted.txt", "w") as f:
        f.write(datetime.now().isoformat())
        f.write(os.environ.get("CHANGED_FILES"))

if __name__ == "__main__":
    main()
