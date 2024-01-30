#!/usr/bin/env python3

import os
import numpy as np

def main():
    print("Changed files", os.environ.get("CHANGED_FILES"))
    a = np.arange(15).reshape(3, 5)
    print("array", a)

if __name__ == "__main__":
    main()
