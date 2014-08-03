#!/bin/bash

pelican content/
cd output
firefox localhost:8000
python -m SimpleHTTPServer
