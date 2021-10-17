import json.decoder
import requests
from typing import List
from .models import *
from .exceptions import *


def get_request(url: str, api_key: str, data: dict = None):
    headers = {'key': api_key}
    r = requests.get(url, headers=headers, data=data)
    return check_response(r)


def post_request(url, api_key, data):
    headers = {'key': api_key}
    r = requests.post(url, headers=headers, data=data)
    return check_response(r)


def delete_request(url, api_key, data=None):
    headers = {'key': api_key}
    r = requests.delete(url, headers=headers, data=data)
    return check_response(r)


def get_devices(api_key: str) -> List[Device]:
    url = 'https://console.helium.com/api/v1/devices'
    return [Device(device) for device in get_request(url, api_key)]


def get_device_by_details(api_key: str, app_eui: str, app_key: str, dev_eui: str) -> Device:
    url = f"https://console.helium.com/api/v1/devices?app_eui={app_eui}&app_key={app_key}&dev_eui={dev_eui}"
    return Device(get_request(url, api_key))


def get_device_by_uuid(api_key: str, device_id: str) -> Device:
    url = f"https://console.helium.com/api/v1/devices/{device_id}"
    return Device(get_request(url, api_key))


def get_device_events(api_key: str, device_id: str) -> List[Event]:
    url = f"https://console.helium.com/api/v1/devices/{device_id}/events"
    return [Event(event) for event in get_request(url, api_key)]


def get_device_integration_events(api_key: str, device_id: str) -> List[IntegrationEvent]:
    url = f"https://console.helium.com/api/v1/devices/{device_id}/events?sub_category=uplink_integration_req"
    return [IntegrationEvent(event) for event in get_request(url, api_key)]


def create_device(api_key: str, name: str, app_eui: str, app_key: str, dev_eui: str) -> Device:
    url = f"https://console.helium.com/api/v1/devices"
    body = {
        'name': name,
        'app_eui': app_eui,
        'app_key': app_key,
        'dev_eui': dev_eui
    }
    return Device(post_request(url, api_key, body))


def delete_device(api_key: str, device_id: str) -> bool:
    url = f"https://console.helium.com/api/v1/devices/{device_id}"
    return delete_request(url, api_key).status_code == 200


def get_labels(api_key: str) -> List[Label]:
    url = 'https://console.helium.com/api/v1/labels'
    return [Label(label) for label in get_request(url, api_key)]


def create_label(api_key: str, name: str) -> Label:
    url = 'https://console.helium.com/api/v1/labels'
    body = {
        'name': name
    }
    return Label(post_request(url, api_key, body))


def search_for_label(api_key: str, label_id: str) -> Label:
    url = f"https://console.helium.com/api/v1/labels/{label_id}"
    return Label(get_request(url, api_key))


def add_device_label(api_key: str, device_id: str, label_id: str) -> bool:
    url = f"https://console.helium.com/api/v1/devices/{device_id}/labels"
    body = {
        'label': label_id
    }
    return post_request(url, api_key, body).status_code == 200


def remove_device_label(api_key: str, device_id: str, label_id: str) -> bool:
    url = f"https://console.helium.com/api/v1/devices/{device_id}/labels/{label_id}"
    return delete_request(url, api_key).status_code == 200


def delete_label(api_key: str, label_id) -> bool:
    url = f"https://console.helium.com/api/v1/labels/{label_id}"
    return delete_request(url, api_key).status_code == 200
