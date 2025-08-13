import yaml

def validate_yaml(yaml_str):
    try:
        yaml.safe_load(yaml_str)
        return {"valid": True, "error": None}
    except yaml.YAMLError as e:
        return {"valid": False, "error": str(e)}
