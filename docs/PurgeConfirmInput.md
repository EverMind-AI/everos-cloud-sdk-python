# PurgeConfirmInput

Step 2: confirm. The scope is the one bound to the nonce.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nonce** | **str** |  | 

## Example

```python
from everos_cloud.models.purge_confirm_input import PurgeConfirmInput

# TODO update the JSON string below
json = "{}"
# create an instance of PurgeConfirmInput from a JSON string
purge_confirm_input_instance = PurgeConfirmInput.from_json(json)
# print the JSON string representation of the object
print(PurgeConfirmInput.to_json())

# convert the object into a dict
purge_confirm_input_dict = purge_confirm_input_instance.to_dict()
# create an instance of PurgeConfirmInput from a dict
purge_confirm_input_from_dict = PurgeConfirmInput.from_dict(purge_confirm_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


