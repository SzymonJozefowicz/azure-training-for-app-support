sudo apt update
sudo apt install python3-pip
python3 -m pip install opencensus-ext-azure
python3 -m pip install opencensus-ext-flask
export FLASK_APP=application.py
flask run -h 0.0.0.0
  