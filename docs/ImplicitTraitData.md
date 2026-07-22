# ImplicitTraitData

``data`` payload for ``add implicit_traits`` — ``trait`` + ``description`` required (non-empty); other fields (``basis``, ``evidence``, ``sources``, …) pass through.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trait** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from everos_cloud_sdk.models.implicit_trait_data import ImplicitTraitData

# TODO update the JSON string below
json = "{}"
# create an instance of ImplicitTraitData from a JSON string
implicit_trait_data_instance = ImplicitTraitData.from_json(json)
# print the JSON string representation of the object
print(ImplicitTraitData.to_json())

# convert the object into a dict
implicit_trait_data_dict = implicit_trait_data_instance.to_dict()
# create an instance of ImplicitTraitData from a dict
implicit_trait_data_from_dict = ImplicitTraitData.from_dict(implicit_trait_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


