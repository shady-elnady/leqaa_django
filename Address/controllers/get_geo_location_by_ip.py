from django.conf import settings
import requests


def get_geo_location_by_ip(ip: str):
    url = "https://ipgeolocation.abstractapi.com/v1"
    querystring = {
        "api_key": settings.ABSTRACT_API_KEY,
        "ip_address": ip,
        "fields": "",
    }

    response = requests.request("GET", url, params=querystring)

    return response.text


"""
    {
        "ip_address": "166.171.248.255",
        "city": "San Jose",
        "city_geoname_id": 5392171,
        "region": "California",
        "region_iso_code": "CA",
        "region_geoname_id": 5332921,
        "postal_code": "95141",
        "country": "United States",
        "country_code": "US",
        "country_geoname_id": 6252001,
        "country_is_eu": false,
        "continent": "North America",
        "continent_code": "NA",
        "continent_geoname_id": 6255149,
        "longitude": -121.7714,
        "latitude": 37.1835,
        "security": {
            "is_vpn": false
        },
        "timezone": {
            "name": "America/Los_Angeles",
            "abbreviation": "PDT",
            "gmt_offset": -7,
            "current_time": "06:37:41",
            "is_dst": true
        },
        "flag": {
            "emoji": "🇺🇸",
            "unicode": "U+1F1FA U+1F1F8",
            "png": "https://static.abstractapi.com/country-flags/US_flag.png",
            "svg": "https://static.abstractapi.com/country-flags/US_flag.svg"
        },
        "currency": {
            "currency_name": "USD",
            "currency_code": "USD"
        },
        "connection": {
            "autonomous_system_number": 20057,
            "autonomous_system_organization": "ATT-MOBILITY-LLC-AS20057",
            "connection_type": "Cellular",
            "isp_name": "AT&T Mobility LLC",
            "organization_name": "Service Provider Corporation"
        }
    }

"""
