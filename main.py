#!/usr/bin/env python3
"""Writes the postmortem entry to /output/entry.txt."""

# POSTMORTEM is the entry text, exactly 163 characters long.
POSTMORTEM = "Root cause: the agent hallucinated a database that never existed, migrated to it anyway, and then wrote a 40-page postmortem blaming the database for not existing."

import os

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(POSTMORTEM)
