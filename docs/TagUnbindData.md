# TagUnbindData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matched** | **int** | How many of the submitted memories the operation matched. Matching is not the same as changing: re-binding a tag an item already carries matches without modifying it. | [optional] [default to 0]
**requested** | **int** | How many ids were submitted. &#x60;matched&#x60; below &#x60;requested&#x60; means some ids were not found — deleted, another tenant&#39;s, or (for bind) already at the per-memory tag limit. | [optional] [default to 0]

## Example

```python
from everos_cloud.models.tag_unbind_data import TagUnbindData

# TODO update the JSON string below
json = "{}"
# create an instance of TagUnbindData from a JSON string
tag_unbind_data_instance = TagUnbindData.from_json(json)
# print the JSON string representation of the object
print(TagUnbindData.to_json())

# convert the object into a dict
tag_unbind_data_dict = tag_unbind_data_instance.to_dict()
# create an instance of TagUnbindData from a dict
tag_unbind_data_from_dict = TagUnbindData.from_dict(tag_unbind_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


