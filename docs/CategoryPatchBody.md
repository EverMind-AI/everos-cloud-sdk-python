# CategoryPatchBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from everos_cloud.models.category_patch_body import CategoryPatchBody

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryPatchBody from a JSON string
category_patch_body_instance = CategoryPatchBody.from_json(json)
# print the JSON string representation of the object
print(CategoryPatchBody.to_json())

# convert the object into a dict
category_patch_body_dict = category_patch_body_instance.to_dict()
# create an instance of CategoryPatchBody from a dict
category_patch_body_from_dict = CategoryPatchBody.from_dict(category_patch_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


