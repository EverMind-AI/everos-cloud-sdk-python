# FlushData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | \&quot;extracted\&quot; when the flush distilled new memories, \&quot;no_extraction\&quot; when there was nothing to extract — including the case of an async add still queued. | 

## Example

```python
from everos_cloud.models.flush_data import FlushData

# TODO update the JSON string below
json = "{}"
# create an instance of FlushData from a JSON string
flush_data_instance = FlushData.from_json(json)
# print the JSON string representation of the object
print(FlushData.to_json())

# convert the object into a dict
flush_data_dict = flush_data_instance.to_dict()
# create an instance of FlushData from a dict
flush_data_from_dict = FlushData.from_dict(flush_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


