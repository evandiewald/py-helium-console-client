from py_helium_console_client import ConsoleClient

## See full documentation for the Console API: https://docs.helium.com/api/console/
API_KEY = 'PASTE_API_KEY_HERE'

# initialize client
client = ConsoleClient(api_key=API_KEY)

# list devices on account
devices = client.get_devices()

# search for a device by app key, app eui, dev eui
single_device = client.get_device_by_details(devices[0].app_eui, devices[0].app_key, devices[0].dev_eui)
assert devices[0].__dict__ == single_device.__dict__

# search for a device by uuid
uuid_device = client.get_device_by_uuid(devices[0].id)
assert devices[0].__dict__ == uuid_device.__dict__

# get device events
events = client.get_device_events(devices[5].id)

# get integration events
integration_events = client.get_device_integration_events(devices[5].id)

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
assert created_label.id == queried_label.id

# add label to device
add_label_result = client.add_device_label(created_device.id, created_label.id)
assert add_label_result is True

# remove label from device
remove_label_result = client.remove_device_label(created_device.id, created_label.id)
assert remove_label_result is True

# delete device
deleted_device_result = client.delete_device(created_device.id)
assert deleted_device_result is True

# delete label
deleted_label_result = client.delete_label(created_label.id)

