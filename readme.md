## Configuration Generator
### Multi Template
---

For this example we'll use two templates to render two different configuration files to extend a VRF from a core site to a remote customer. If you're not a networking professional this may not make too much sense but I will try to apply the concepts as generally as possible.

Like before we're going to start by adding two devices to our `inventory.txt` file and adding two `.json` files matching our inventory entries.
```
<!-- inventory.txt -->
ce
pe

<!-- hosts folder -->
hosts
    ce.json
    pe.json
```
Let's talk about our `main.json` file for a second. With this template we're going to flip our logic a bit from the single template example. Instead of having specific host variables, we're going to define all of our variables in `main.json`. The reason we are doing this is because most of the variables we are going to use will be shared between the two configuration templates.

Our host files will be pretty slim, we'll just define the template that we want to use for each device.
```
<!-- ce.json -->
{
    "template": "ce.j2"
}

<!-- pe.json -->
{
    "template": "pe.j2"
}
```
There are two Jinja2 templates in the templates folder, one for each item in our inventory. I won't dive too deep into the specifics of the templates themselves but at a high level each template represents a specific device configuration (ce for Cisco IOS and pe for Cisco Nexus). They contain templates for routing protocol information, interface and IP address configuration, and VRF definitions.

We've now got everything we need to run the script.

Same process as last time, run `python3 generate_config.py generate-configs`, and we should have two files in our `_generated` folder, `ce.cfg` and `pe.cfg`.

Let me know if this example is not clear enough or needs further explanation. I realize this may not have been the easiest example to visualize however, this is my most used 'multi template' script. Another good/similar use case for mulit templates would be if you were needing to configure multiple devices that perform different functions ex. routers and switches, or devices that contain the same basic variables but require different configuration syntax ex. multiple switches from different vendors.