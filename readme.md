# Configuration Generator

This is a Python script built to model the way you can build configuration files in Ansible. I found myself creating too many scripts to perform 
different configuration tasks so I decided to condense those into a single and more modular codebase.

* Built on Python 3+.
* Uses Jinja2 for templating and is the only dependency for now. Run `pip install -r requirements.txt` to install it.

## Updates
 - Both Single and Multiple template examples have been commited and linked at the bottom of the readme.
 - Added functionality to generate host files from the inventory list. This cuts down on some of the time needed to create each `.json` file to match what is in the inventory list.
 - The group variables `main.json` file can now be broken up into multiple files if desired. All `.json` files in the groups folder will be used to build the group variables object.
 - Added click library to allow for usage of CLI commands.


###  This project in a nutshell
--- 
The script looks for device names in the `inventory.txt` file and each device should be on it's own line.

For every device listed in inventory, there needs to be a coresponding *.json* file in the hosts folder with the same name. You can create these individually or you can run `python3 generate_config.py create-hosts` and your host files will be generated for you based on your inventory file.

The hosts files are json objects that hold variables specific to each device listed in the inventory. These could be variables such as IP addresses, VLANs, device hostnames, etc. 
* **FYI**, the device name used in the inventory file can be accessed in the templates with the variable name `inv_host`.

The groups folder contains `main.json` which can contain variables that need to be shared between all devices in the inventory. 

A big part of this process is defining your templates. The script is looking for *.j2* files in the templates folder and will be applying both the hosts and group variables to create the config files. There are two ways you can define which template to use: 
1. If you need to apply the same template to all the devices in inventory, define a template variable in the `groups/main.json` file.
2. If you need a specific template for each device, define the template variable in each `hosts/*device*.json` file.

As stated before, Jinja2 is being used to render templates so if you are unfamiliar I'd reccomend starting [here](http://jinja.pocoo.org/docs/2.10/). I will also be adding example branches to this repo so be sure to check the bottom of this page for the links to those. 

Finally, `_generated` is the default ouput location once the configuration files have been generated. If this folder does not exist, it will be created before the files are built.

---
Examples:
* [Single template](https://github.com/Philip-Owen/config_generator/tree/single-template)
* [Multi template](https://github.com/Philip-Owen/config_generator/tree/multi-template)

