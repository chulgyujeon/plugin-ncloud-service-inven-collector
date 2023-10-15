from schematics.types import ModelType, PolyModelType, StringType
from spaceone.inventory.libs.schema.resource import CloudServiceMeta, CloudServiceResource, CloudServiceResponse
from spaceone.inventory.libs.schema.dynamic_field import TextDyField, DateTimeDyField, EnumDyField, ListDyField, \
    SizeField
from spaceone.inventory.libs.schema.dynamic_layout import ItemDynamicLayout, SimpleTableDynamicLayout, \
    TableDynamicLayout

# TAB
details = ItemDynamicLayout.set_fields('Details', fields=[
    EnumDyField.data_source('Status', 'data.server_instance_status_name',
                            default_state={
                                'safe': ['running'],
                                'available': ['init', 'creating', 'booting', 'setting up', 'changingSpec'],
                                'warning': ['warning', 'rebooting', 'hard rebooting', 'shutting down',
                                            'hard shutting down', 'terminating', 'copying', 'repairing', ],
                                'disable': ['stopped']}),
    TextDyField.data_source('Public IP', 'data.public_ip'),
    TextDyField.data_source('Private IP', 'data.private_ip'),
    TextDyField.data_source('vCore', 'data.cpu_count'),
    SizeField.data_source('Memory', 'data.memory_size', type="size",
                          options={"source_unit": "BYTES", "display_unit": "GB"}),
    TextDyField.data_source('Instance Type', 'data.server_instance_type.code_name'),
    TextDyField.data_source('Image', 'data.server_image_name'),
    TextDyField.data_source('Zone', 'data.zone.zone_code'),
    TextDyField.data_source('Region', 'data.region_code'),
    DateTimeDyField.data_source("Created", "data.create_date"),
    TextDyField.data_source('Login Key', 'data.login_key_name'),
    EnumDyField.data_source('Protect Server Termination', 'data.is_protect_server_termination', default_badge={
        'indigo.500': ['true'], 'coral.600': ['false']
    }),
    EnumDyField.data_source('Fee Charging Monitoring', 'data.is_fee_charging_monitoring', default_badge={
        'indigo.500': ['true'], 'coral.600': ['false']
    }),
    TextDyField.data_source('Base Storage Disk Type', 'data.base_block_storage_disk_detail_type.code_name'),
    SizeField.data_source('Base Storage Disk Size', 'data.base_block_storage_size', type="size",
                          options={"source_unit": "BYTES", "display_unit": "GB"}),
])

port_forwarding = ItemDynamicLayout.set_fields('Port Forwarding', fields=[
    TextDyField.data_source('Public IP', 'data.port_forwarding_public_ip'),
    TextDyField.data_source('External Port', 'data.port_forwarding_external_port'),
    TextDyField.data_source('Internal Port', 'data.port_forwarding_internal_port'),
])

disk = TableDynamicLayout.set_fields('Disk', root_path='data.disks', fields=[
    TextDyField.data_source('Name', 'block_storage_name'),
    SizeField.data_source('Size(GB)', 'block_storage_size', options={
        'display_unit': 'GB',
        'source_unit': 'Byte'
    }),
    TextDyField.data_source('Status', 'block_storage_instance_status_name'),
    TextDyField.data_source('Volume ID', 'block_storage_instance_no'),
    TextDyField.data_source('Volume Type', 'block_storage_type.code'),
    TextDyField.data_source('Dick Type', 'disk_detail_type.code'),
    TextDyField.data_source('MAX IOPS', 'max_iops_throughput'),
    TextDyField.data_source('Device', 'device_name')
])

nic = TableDynamicLayout.set_fields('NIC', root_path='data.nics', fields=[
    TextDyField.data_source('Name', 'network_interface_name'),
    TextDyField.data_source('IP Addresses', 'network_interface_ip'),
    TextDyField.data_source('Status', 'status_code')
])

security_groups = TableDynamicLayout.set_fields('Security Groups', root_path='data.security_groups', fields=[
    TextDyField.data_source('Name', 'access_control_group_name'),
    EnumDyField.data_source('Protocol', 'protocol_type.code', default_outline_badge=['ALL', 'TCP', 'UDP', 'ICMP']),
    TextDyField.data_source('Source', 'source_ip'),
    TextDyField.data_source('DST Port', 'destination_port'),
    TextDyField.data_source('Description', 'access_control_rule_description'),
])

SERVICE_DETAILS = CloudServiceMeta.set_layouts([details, port_forwarding, nic, disk, security_groups])