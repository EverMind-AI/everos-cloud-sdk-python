# ImplicitTraitPatch

``data`` payload for ``update implicit_traits`` — partial; at least one of ``trait`` / ``description`` (non-empty if present); others pass through.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trait** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from everos_cloud.models.implicit_trait_patch import ImplicitTraitPatch

# TODO update the JSON string below
json = "{}"
# create an instance of ImplicitTraitPatch from a JSON string
implicit_trait_patch_instance = ImplicitTraitPatch.from_json(json)
# print the JSON string representation of the object
print(ImplicitTraitPatch.to_json())

# convert the object into a dict
implicit_trait_patch_dict = implicit_trait_patch_instance.to_dict()
# create an instance of ImplicitTraitPatch from a dict
implicit_trait_patch_from_dict = ImplicitTraitPatch.from_dict(implicit_trait_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


