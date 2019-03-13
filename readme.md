## Configuration Generator

This is a Python script built to model the way you can build configuration files in Ansible. I found myself creating too many scripts to perform 
different configuration tasks so I decided to condense those into a single and more modular codebase.

* Built on Python 3+.
* Uses Jinja2 for templating and is the only dependency for now. Run `pip install -r requirements.txt` to install it.


#### ** This project in a nutshell **
The script looks for device names in the `inventory.txt` file and each device should be on it's own line.

For every device listed in inventory, there needs to be a coresponding *.json* file in the hosts folder with the same name. 

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
* Single template
* Multi template

