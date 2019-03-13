def createGroupedDict(group_params, host_params):
    merged = group_params.copy()
    merged.update(host_params)
    return merged

def handleMissingDevice(device):
    print("Cannot find file %s.json..." % device)
    print("Skipping device...")
