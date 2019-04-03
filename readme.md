## Configuration Generator
### Single Template
---

In this example we'll use a single template to generate configuration files, containing the device hostname and a loopback interface, for multiple devices.

Let's start by defining two devices in the `inventory.txt` file.
```
<!-- inventory.txt -->

sw1
sw2
```
We will now need to add two json files to the `hosts` folder to match what we just put in the inventory, `sw1.json` and `sw2.json`. 

For each file let's add an object with a key named "loopback0". "loopback0" will contain an object with two keys, "ip" for the IP address and "snm" for the subnet mask of the network:
```
<!-- hosts/sw1.json -->

{
  "loopback0": {
    "ip": "172.25.10.1",
    "snm": "255.255.255.255"
  }
}


<!-- hosts/sw2.json -->

{
  "loopback0": {
    "ip": "172.25.10.2",
    "snm": "255.255.255.255"
  }
}

```
Now we'll need to define a template to use. Create a Jinja2 file, `interfaces.j2` in the templates folder and add the following code:
```
<!-- templates/interfaces.j2 -->

hostname {{ inv_host }}

interface loopback0
  ip address {{loopback0.ip}} {{loopback0.snm}}
end

```
`{{ inv_host }}` will grab the inventory hostname we defined in the `inventory.txt` file and `{{ loopback0.ip }}` and `{{ loopback0.snm }}` will grab the variables we defined in each host file.

So far we've defined our inventory, created our host file, and created a template. Now we'll need to let the script know what template to use. Since we want to use this template for all of our devices in the inventory we can set the templates variable in the  `groups/main.json` file.
```
<!-- groups/main.json -->

{
  "template": "interfaces.j2"
}
```
The script now has all it needs to generate the configuration files. In the terminal lets run `python3 generate_config.py generate-configs`.

We should now have two files under `_generated`
```
_generated
  sw1.cfg
  sw2.cfg
```
```
<!-- _generated/sw1.cfg -->
hostname sw1

interface loopback0
  ip address 172.25.10.1 255.255.255.255
end

<!-- _generated/sw1.cfg  -->
hostname sw2

interface loopback0
  ip address 172.25.10.2 255.255.255.255
end
```


