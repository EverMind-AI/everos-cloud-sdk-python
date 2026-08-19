# AddInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | [optional] [default to 'default']
**project_id** | **str** |  | [optional] [default to 'default']
**session_id** | **str** |  | 
**messages** | [**List[MessageItem]**](MessageItem.md) |  | 
**async_mode** | **bool** | Selects the write path. true (default): validated and enqueued asynchronously → HTTP 202 with status \&quot;queued\&quot;. false: forwarded synchronously to the engine, returning its 200 result and surfacing write errors directly. Extraction is always asynchronous (flush-triggered). | [optional] [default to True]

## Example

```python
from everos_cloud.models.add_input import AddInput

# TODO update the JSON string below
json = "{}"
# create an instance of AddInput from a JSON string
add_input_instance = AddInput.from_json(json)
# print the JSON string representation of the object
print(AddInput.to_json())

# convert the object into a dict
add_input_dict = add_input_instance.to_dict()
# create an instance of AddInput from a dict
add_input_from_dict = AddInput.from_dict(add_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


