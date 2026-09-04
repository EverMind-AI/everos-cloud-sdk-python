# CategoryData

A category as returned to clients. ``id`` is the system-generated stable key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Category id (system-generated, stable) | 
**name** | **str** | The category&#39;s display name. | 
**description** | **str** | What belongs in this category. The classifier matches documents against this text, so it is functional, not decorative. | [optional] [default to '']
**document_count** | **int** | How many documents are filed under it. | [optional] [default to 0]
**scope** | **str** | &#39;kb&#39; &#x3D; user-created in this kb; &#39;tenant&#39; &#x3D; global preset (read-only) | [optional] [default to 'kb']
**editable** | **bool** | False for tenant-global preset categories (read-only) | [optional] [default to True]

## Example

```python
from everos_cloud.models.category_data import CategoryData

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryData from a JSON string
category_data_instance = CategoryData.from_json(json)
# print the JSON string representation of the object
print(CategoryData.to_json())

# convert the object into a dict
category_data_dict = category_data_instance.to_dict()
# create an instance of CategoryData from a dict
category_data_from_dict = CategoryData.from_dict(category_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


