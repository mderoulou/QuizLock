#!/bin/bash
pip3 install pygame python-xlib &> /dev/null
(cd QuizLock && python3 script.py) || python3 script.py