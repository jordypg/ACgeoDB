#!/bin/bash
npm run build
sudo chmod o+r /home/hwarrich23/ACgeoDB/geo_react/build/index.html
cd /home/hwarrich23/ACgeoDB/geo_react
chmod -R 755 build/