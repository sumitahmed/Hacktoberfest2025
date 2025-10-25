
import json
def pretty_print(json_string):
    parsed = json.loads(json_string)
    return json.dumps(parsed, indent=4, sort_keys=True)

if __name__ == "__main__":
    sample = '{"name":"Sumit","age":21,"skills":["Java","Cybersec"]}'
    print(pretty_print(sample))
