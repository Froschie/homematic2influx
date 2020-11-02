# Homematic States which will be ignored and not written to Influx DB
ignore_states = []
ignore_states.append('ACTIVE_PROFILE')
ignore_states.append('ACTUAL_TEMPERATURE_STATUS')
ignore_states.append('AVERAGE_ILLUMINATION_STATUS')

# Homematic Devices which will be ignored and not written to Influx DB
ignore_devices = []
ignore_devices.append('HM-CC-RT-DN')
ignore_devices.append('HmIP-RCV-50')
ignore_devices.append('HM-WDS10-TH-O')