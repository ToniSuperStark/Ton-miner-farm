#!/bin/bash
cd /opt/render/project/src
python -m http.server 8000 --directory static
