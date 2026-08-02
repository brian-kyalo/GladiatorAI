"""
GladiatorAI Notebook Bootstrap

This file allows every notebook to automatically
find the project modules.
"""

import os
import sys

# Project Root
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Add project root to Python Path
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

print("✅ GladiatorAI Environment Ready")
print("Project Root:", PROJECT_ROOT)