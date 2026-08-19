# CategoryCreateBody

POST body — id is system-generated, never client-supplied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name | 
**description** | **str** | Feeds everalgo CategorySpec | [optional] [default to '']

## Example

```python
from everos_cloud.models.category_create_body import CategoryCreateBody

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryCreateBody from a JSON string
category_create_body_instance = CategoryCreateBody.from_json(json)
# print the JSON string representation of the object
print(CategoryCreateBody.to_json())

# convert the object into a dict
category_create_body_dict = category_create_body_instance.to_dict()
# create an instance of CategoryCreateBody from a dict
category_create_body_from_dict = CategoryCreateBody.from_dict(category_create_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


