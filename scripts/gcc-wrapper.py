#!/usr/bin/env python3

import sys
import subprocess

# Simple wrapper that just passes through to the real compiler
# without any warning filtering
if __name__ == '__main__':
    # Get the real compiler from the first argument
    args = sys.argv[1:]
    
    try:
        result = subprocess.call(args)
    except OSError as e:
        print(f"Error executing {args[0]}: {e}")
        result = 1
    
    sys.exit(result)
