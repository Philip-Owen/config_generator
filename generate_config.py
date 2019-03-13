from helpers import handleMissingDevice, createGroupedDict
from pathlib import Path
import jinja2
import json
import os

def read_inventory(inv_file):
    f = open(inv_file)
    inventory = f.readlines()
    return inventory

def compile_params(inventory, env):
    for device in inventory:
        group_params = json.load(open("./groups/main.json"))
        device = device.rstrip()
        host_path = Path("./hosts/" + device + ".json")
        if host_path.is_file():
            host_params = json.load(open(host_path))
            grouped_dict = createGroupedDict(group_params, host_params)
            grouped_dict['inv_host'] = device
            template = env.get_template('./templates/%s' % grouped_dict["template"])
            result = template.render(grouped_dict)
            if not os.path.exists('./_generated/'):
                os.mkdir('./_generated/')
            f = open(os.path.join('./_generated/', device+".cfg"), "w")
            f.write(result)
            f.close()    
        else:
            handleMissingDevice(device)

def main():
    # Create Jinja2 env
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="."), trim_blocks=True, lstrip_blocks=True)
    # Open and collect inventory
    inventory = read_inventory('inventory.txt')
    # Build configuration files
    compile_params(inventory, env)



if __name__ == '__main__':
    main()




    