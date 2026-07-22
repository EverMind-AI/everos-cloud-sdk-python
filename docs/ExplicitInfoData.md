# ExplicitInfoData

``data`` payload for ``add explicit_info`` — ``category`` + ``description`` required (non-empty); other fields (``evidence``, ``sources``, …) pass through.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from everos_cloud_sdk.models.explicit_info_data import ExplicitInfoData

# TODO update the JSON string below
json = "{}"
# create an instance of ExplicitInfoData from a JSON string
explicit_info_data_instance = ExplicitInfoData.from_json(json)
# print the JSON string representation of the object
print(ExplicitInfoData.to_json())

# convert the object into a dict
explicit_info_data_dict = explicit_info_data_instance.to_dict()
# create an instance of ExplicitInfoData from a dict
explicit_info_data_from_dict = ExplicitInfoData.from_dict(explicit_info_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


