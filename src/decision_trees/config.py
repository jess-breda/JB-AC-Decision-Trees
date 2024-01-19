# config.py
"""
Quick scrip to set up paths for the decision tree project
Written by Jess Breda 01/19/2024
"""

from pathlib import Path

current_path = Path.cwd()

if "jess" in str(current_path):
    data_path = Path("/Users/jessbreda/Desktop/github/JB-AC-Decision-Trees/data")
    src_path = Path("/Users/jessbreda/Desktop/github/JB-AC-Decision-Trees/src")
else:
    print("User not known! add to config.py")
    # TODO
    data_path = None
    src_path = None

    # data_path = Path('/Users/XXX/Desktop/github/JB-AC-Decision-Trees/data')
    # src_path = Path('/Users/XXX/Desktop/github/JB-AC-Decision-Trees/src')
