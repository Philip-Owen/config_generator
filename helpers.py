import json
import os
from pathlib import Path


def createGroupedDict(group_params, host_params):
    merged = group_params.copy()
    merged.update(host_params)
    return merged


def handleMissingDevice(device):
    print("Cannot find file %s.json..." % device)
    print("Skipping device...")


def gen_hosts():
	f = open('inventory.txt')
	i = f.readlines()
	for device in i:
		device = device.rstrip()
		file_path = Path('./hosts/' + device + '.json')
		if not file_path.is_file():
			file = open(file_path, 'w')
			file.close()

def loadGroupParms(path):
    group = {}
    for f in os.listdir(path):
        if '.json' in f:
            group.update(json.load(open('./groups/'+f)))
    return group
