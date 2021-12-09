'''Update the tag of the values file'''
import yaml
import sys

def update_tag(input_file, new_value):
    with open(input_file) as f:
        doc = yaml.safe_load(f)

    doc['image']['tag'] = new_value

    with open(input_file, 'w') as f:
        yaml.dump(doc,f)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        update_tag(sys.argv[1],sys.argv[2])
    else:
        print(f"This script needs two argument, you gave {len(sys.argv) -1}")
        print(f"Usage: {sys.argv[0]} input_file newtag ")