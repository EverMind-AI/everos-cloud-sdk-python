# AddInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | Business-semantic scope for this write, defaulting to \&quot;default\&quot;. Reads must use the same app_id / project_id pair to see what was written under it. Note this is a partition, not the security boundary — that is the tenant resolved from your API key. | [optional] [default to 'default']
**project_id** | **str** | Second half of the business-semantic scope, defaulting to \&quot;default\&quot;. See &#x60;app_id&#x60;. | [optional] [default to 'default']
**session_id** | **str** | The conversation these messages belong to (1–128 characters). It is the unit extraction works on: /api/v2/memory/flush takes this id, and a session boundary is what triggers extraction on its own. | 
**messages** | [**List[MessageItem]**](MessageItem.md) | The turns to append, in order — 1 to 500 per call. Each carries its own sender and timestamp, so one call can hold a whole exchange. | 
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


