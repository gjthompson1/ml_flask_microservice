#!/bin/bash
cd /opt/server/models/
python train_seniority.py
cd /opt/server/
gunicorn -b 0.0.0.0:5000 -w 4 api:app
