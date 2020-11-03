# Homematic States which will be ignored and not written to Influx DB
ignore_states = []
ignore_states.append('ACTIVE_PROFILE')
ignore_states.append('ACTUAL_HUMIDITY')
ignore_states.append('ACTUAL_TEMPERATURE_STATUS')
ignore_states.append('AVERAGE_ILLUMINATION_STATUS')
ignore_states.append('BOOST_MODE')
ignore_states.append('BOOST_STATE')
ignore_states.append('BOOST_TIME')
ignore_states.append('COMMUNICATION_REPORTING')
ignore_states.append('CONTROL_MODE')
ignore_states.append('CURRENT_ILLUMINATION_STATUS')
ignore_states.append('DECISION_VALUE')
ignore_states.append('DEVICE_IN_BOOTLOADER')
ignore_states.append('HIGHEST_ILLUMINATION_STATUS')
ignore_states.append('LOWEST_ILLUMINATION_STATUS')
ignore_states.append('HUMIDITY_STATUS')
ignore_states.append('LEVEL_REAL')
ignore_states.append('OPERATING_VOLTAGE_STATUS')
ignore_states.append('PARTY_MODE')
ignore_states.append('PARTY_START_DAY')
ignore_states.append('PARTY_START_MONTH')
ignore_states.append('PARTY_START_TIME')
ignore_states.append('PARTY_START_YEAR')
ignore_states.append('PARTY_STOP_DAY')
ignore_states.append('PARTY_STOP_MONTH')
ignore_states.append('PARTY_STOP_TIME')
ignore_states.append('PARTY_STOP_YEAR')
ignore_states.append('PARTY_TEMPERATURE')
ignore_states.append('SET_TEMPERATURE')
ignore_states.append('SET_POINT_MODE')
ignore_states.append('SET_POINT_TEMPERATURE')
ignore_states.append('FROST_PROTECTION')
ignore_states.append('WINDOW_OPEN_REPORTING')


# Homematic Devices which will be ignored and not written to Influx DB
ignore_devices = []
ignore_devices.append('HM-CC-RT-DN')
ignore_devices.append('HmIP-RCV-50')
ignore_devices.append('HM-WDS10-TH-O')


# special handle of Homematic States
meas_config = {}
#meas_config['ACTIVE_PROFILE'] = {}
#meas_config['ACTUAL_HUMIDITY'] = { 'meas_remap': 'HUMIDITY', 'field_remap': {'ACTUAL_HUMIDITY_2': 'HUMIDITY_1'}}
meas_config['ACTUAL_TEMPERATURE'] = {}
#meas_config['ACTUAL_TEMPERATURE_STATUS'] = {}
meas_config['AVERAGE_ILLUMINATION'] = {}
#meas_config['AVERAGE_ILLUMINATION_STATUS'] = {}
meas_config['BATTERY_STATE'] = {}
#meas_config['BOOST_MODE'] = {}
#meas_config['BOOST_STATE'] = {}
#meas_config['BOOST_TIME'] = {}
meas_config['BRIGHTNESS'] = {}
#meas_config['COMMUNICATION_REPORTING'] = {}
meas_config['CONFIG_PENDING'] = {}
#meas_config['CONTROL_MODE'] = {}
meas_config['CURRENT'] = {}
meas_config['CURRENT_ILLUMINATION'] = {}
#meas_config['CURRENT_ILLUMINATION_STATUS'] = {}
#meas_config['DECISION_VALUE'] = {}
#meas_config['DEVICE_IN_BOOTLOADER'] = {}
meas_config['DUTYCYCLE'] = {}
meas_config['DUTY_CYCLE'] = {}
meas_config['ENERGY_COUNTER'] = {}
meas_config['ERROR'] = {}
meas_config['ERROR_CODE'] = {}
meas_config['ERROR_OVERHEAT'] = {}
meas_config['ERROR_OVERLOAD'] = {}
meas_config['ERROR_REDUCED'] = {}
meas_config['FREQUENCY'] = {}
#meas_config['FROST_PROTECTION'] = {}
meas_config['HEATING_COOLING'] = {}
meas_config['HIGHEST_ILLUMINATION'] = {}
#meas_config['HIGHEST_ILLUMINATION_STATUS'] = {}
meas_config['HUMIDITY'] = {}
#meas_config['HUMIDITY_STATUS'] = {}
meas_config['LEVEL'] = {}
#meas_config['LEVEL_REAL'] = {}
meas_config['LOWBAT'] = {}
meas_config['LOWBAT_REPORTING'] = {}
meas_config['LOWEST_ILLUMINATION'] = {}
#meas_config['LOWEST_ILLUMINATION_STATUS'] = {}
meas_config['LOW_BAT'] = {}
meas_config['MOTION'] = {}
meas_config['OPERATING_VOLTAGE'] = {}
#meas_config['OPERATING_VOLTAGE_STATUS'] = {}
#meas_config['PARTY_MODE'] = {}
#meas_config['PARTY_START_DAY'] = {}
#meas_config['PARTY_START_MONTH'] = {}
#meas_config['PARTY_START_TIME'] = {}
#meas_config['PARTY_START_YEAR'] = {}
#meas_config['PARTY_STOP_DAY'] = {}
#meas_config['PARTY_STOP_MONTH'] = {}
#meas_config['PARTY_STOP_TIME'] = {}
#meas_config['PARTY_STOP_YEAR'] = {}
#meas_config['PARTY_TEMPERATURE'] = {}
meas_config['POWER'] = {}
meas_config['PRESS_LONG'] = {}
meas_config['PRESS_SHORT'] = {}
meas_config['QUICK_VETO_TIME'] = {}
meas_config['RSSI_DEVICE'] = {}
meas_config['RSSI_PEER'] = {}
meas_config['SABOTAGE'] = {}
#meas_config['SET_POINT_MODE'] = {}
#meas_config['SET_POINT_TEMPERATURE'] = {}
#meas_config['SET_TEMPERATURE'] = {}
meas_config['STATE'] = {}
meas_config['STICKY_UNREACH'] = {}
meas_config['SWITCH_POINT_OCCURED'] = {}
meas_config['TEMPERATURE'] = {}
meas_config['TEMPERATURE_OUT_OF_RANGE'] = {}
meas_config['UNREACH'] = {}
meas_config['UPDATE_PENDING'] = {}
meas_config['VOLTAGE'] = {}
#meas_config['WINDOW_OPEN_REPORTING'] = {}
meas_config['WINDOW_STATE'] = {}