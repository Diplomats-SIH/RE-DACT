# script.py
import sys

def main(arg):
    print(f"Hello from Python! Argument received: {arg}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main("No argument")
