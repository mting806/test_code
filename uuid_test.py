import uuid
test_str = "test_str"
test_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, test_str)

print(test_uuid)

print(uuid.NAMESPACE_DNS)