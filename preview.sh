#!/bin/bash

cd /home/jonathan/www/jrobb.org-pelican/
pelican content/
cd output
firefox localhost:8000
python -m SimpleHTTPServer
