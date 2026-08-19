# TagReplaceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matched** | **int** |  | [optional] [default to 0]
**requested** | **int** |  | [optional] [default to 0]

## Example

```python
from everos_cloud.models.tag_replace_data import TagReplaceData

# TODO update the JSON string below
json = "{}"
# create an instance of TagReplaceData from a JSON string
tag_replace_data_instance = TagReplaceData.from_json(json)
# print the JSON string representation of the object
print(TagReplaceData.to_json())

# convert the object into a dict
tag_replace_data_dict = tag_replace_data_instance.to_dict()
# create an instance of TagReplaceData from a dict
tag_replace_data_from_dict = TagReplaceData.from_dict(tag_replace_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


