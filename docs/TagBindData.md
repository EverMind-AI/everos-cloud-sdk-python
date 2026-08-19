# TagBindData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matched** | **int** |  | [optional] [default to 0]
**requested** | **int** |  | [optional] [default to 0]

## Example

```python
from everos_cloud.models.tag_bind_data import TagBindData

# TODO update the JSON string below
json = "{}"
# create an instance of TagBindData from a JSON string
tag_bind_data_instance = TagBindData.from_json(json)
# print the JSON string representation of the object
print(TagBindData.to_json())

# convert the object into a dict
tag_bind_data_dict = tag_bind_data_instance.to_dict()
# create an instance of TagBindData from a dict
tag_bind_data_from_dict = TagBindData.from_dict(tag_bind_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


