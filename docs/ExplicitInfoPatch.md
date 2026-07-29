# ExplicitInfoPatch

``data`` payload for ``update explicit_info`` — partial; at least one of ``category`` / ``description`` (non-empty if present); others pass through.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from everos_cloud.models.explicit_info_patch import ExplicitInfoPatch

# TODO update the JSON string below
json = "{}"
# create an instance of ExplicitInfoPatch from a JSON string
explicit_info_patch_instance = ExplicitInfoPatch.from_json(json)
# print the JSON string representation of the object
print(ExplicitInfoPatch.to_json())

# convert the object into a dict
explicit_info_patch_dict = explicit_info_patch_instance.to_dict()
# create an instance of ExplicitInfoPatch from a dict
explicit_info_patch_from_dict = ExplicitInfoPatch.from_dict(explicit_info_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


