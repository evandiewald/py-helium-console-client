from .api_calls import *


class ConsoleClient:
    """HTTP Client for interacting with the Helium Console API.
    See Console API docs (https://docs.helium.com/api/console/)"""
    def __init__(self, api_key: str):
        """Authenticate the client with an API Key"""
        self.api_key = api_key

    def get_devices(self):
        """List all devices on your account"""
        return get_devices(self.api_key)

    def get_device_by_details(self, app_eui: str, app_key: str, dev_eui: str):
        """Search for a device by its AppEui, AppKey, & DevEui"""
        return get_device_by_details(self.api_key, app_eui, app_key, dev_eui)

    def get_device_by_uuid(self, device_id: str):
        """Search for a device by its UUID"""
        return get_device_by_uuid(self.api_key, device_id)

    def get_device_events(self, device_id: str):
        """Get up to 100 recent events from a device"""
        return get_device_events(self.api_key, device_id)

    def get_device_integration_events(self, device_id: str):
        """Get up to 10 recent integration events from a device"""
        return get_device_integration_events(self.api_key, device_id)

    def create_device(self, name: str, app_eui: str, app_key: str, dev_eui: str):
        """Create a new device. State may be 'Pending' for a few minutes"""
        return create_device(self.api_key, name, app_eui, app_key, dev_eui)

    def delete_device(self, device_id: str):
        """Delete a device. Returns True if successful"""
        return delete_device(self.api_key, device_id)

    def get_labels(self):
        """Lists all labels in your account"""
        return get_labels(self.api_key)

    def create_label(self, name: str):
        """Creates a new label"""
        return create_label(self.api_key, name)

    def search_for_label(self, label_id: str):
        """Search for a label by its id"""
        return search_for_label(self.api_key, label_id)

    def add_device_label(self, device_id: str, label_id: str):
        """Attach a label to a device (by UUID)"""
        return add_device_label(self.api_key, device_id, label_id)

    def remove_device_label(self, device_id: str, label_id: str):
        """Disassociate a label from a device"""
        return remove_device_label(self.api_key, device_id, label_id)

    def delete_label(self, label_id: str):
        """Delete a label by id"""
        return delete_label(self.api_key, label_id)

