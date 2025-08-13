from fastapi import FastAPI
from utils.yaml_validator import validate_yaml
from utils.cron_parser import parse_cron
from utils.regex_tester import test_regex

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to DevOps Toolbox API"}
