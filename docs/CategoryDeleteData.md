# CategoryDeleteData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Deleted category id | 
**deleted** | **bool** | True if a live category was soft-deleted; False if absent | 

## Example

```python
from everos_cloud.models.category_delete_data import CategoryDeleteData

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryDeleteData from a JSON string
category_delete_data_instance = CategoryDeleteData.from_json(json)
# print the JSON string representation of the object
print(CategoryDeleteData.to_json())

# convert the object into a dict
category_delete_data_dict = category_delete_data_instance.to_dict()
# create an instance of CategoryDeleteData from a dict
category_delete_data_from_dict = CategoryDeleteData.from_dict(category_delete_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


