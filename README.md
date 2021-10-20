# py-helium-console-client
An __unofficial__ Python Client library for the [Helium Console API](https://docs.helium.com/use-the-network/console/api/). Please see the [API Specification](https://docs.helium.com/api/console/) for full details.

## Installation
The package can be installed via `pip`:

`pip install py_helium_console_client`

## Usage
To use the Console API, you will first need to generate an API Key from the 'My Account' tab in the [Helium Console](https://console.helium.com/profile) web interface. Use this key to initialize the `ConsoleClient` class. This wrapper exposes any of the methods in the specification (at the time of writing), which includes programmatic access for creating, querying, and deleting devices and labels. 

Some example commands are shown below. See [`examples.py`](examples.py) for full usage.

```python
from py_helium_console_client.client import ConsoleClient

API_KEY = 'PASTE_API_KEY_HERE'

client = ConsoleClient(API_KEY)

# list devices on account
devices = client.get_devices()

# search for a device by uuid
uuid_device = client.get_device_by_uuid(devices[0].id)

# get device events
events = client.get_device_events(devices[0].id)

# create device
created_device = client.create_device(name='python-client-test-device',
                              app_key='850AFDC6F1CF2397D3FEAB8C1850E6E1',
                              app_eui='B21C36EBBDC0D75F',
                              dev_eui='ABA47D469E1021AF')

# list labels
labels = client.get_labels()

# create label
created_label = client.create_label('python-client-test-label')

# search for label by id
queried_label = client.search_for_label(created_label.id)

# add label to device
add_label_result = client.add_device_label(created_device.id, created_label.id)

# remove label from device
remove_label_result = client.remove_device_label(created_device.id, created_label.id)

# delete device
deleted_device_result = client.delete_device(created_device.id)

# delete label
deleted_label_result = client.delete_label(created_label.id)
```

## Contributing
This is a small project that I use for developing my own applications on the Helium Network. Please feel free to submit an [issue](https://github.com/evandiewald/py-helium-console-client/issues) or a [PR](https://github.com/evandiewald/py-helium-console-client/pulls) if you find bugs or have suggestions!