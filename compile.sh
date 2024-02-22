#!/bin/bash
jb clean .
jb build .
cp notebooks/interactive_diagrams/T_v_diagrams/*.html ./_build/html/notebooks/interactive_diagrams/T_v_diagrams/
