# filter_plugins/custom_filters.py

def extract_member_status(member, pool_name, stats):
    device_name = member['subPath'].split(':')[0]
    stat_path = f"https://localhost/mgmt/tm/gtm/pool/a/~Common~{pool_name}/members/~Common~{member['name']}:~Common~{device_name}/stats"
    stat = stats.get(stat_path, {}).get('nestedStats', {}).get('entries', {})
    return {
        'name': member['name'],
        'device_name': device_name,
        'availability': stat.get('status.availabilityState', {}).get('description', 'unknown'),
        'enabled': stat.get('status.enabledState', {}).get('description', 'unknown')
    }

class FilterModule(object):
    def filters(self):
        return {
            'extract_member_status': extract_member_status
        }
