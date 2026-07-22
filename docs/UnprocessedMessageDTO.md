# UnprocessedMessageDTO

Buffered raw message not yet extracted (no owner — inference happens after boundary detection). Returned by /search only when ``filters.session_id`` is a top-level eq scalar (spec §4 / appendix E).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**app_id** | **str** |  | 
**project_id** | **str** |  | 
**session_id** | **str** |  | 
**sender_id** | **str** |  | 
**sender_name** | **str** |  | [optional] 
**role** | **str** |  | 
**content** | [**Content**](Content.md) |  | 
**timestamp** | **datetime** |  | 
**tool_calls** | [**List[ToolCall]**](ToolCall.md) |  | [optional] 
**tool_call_id** | **str** |  | [optional] 

## Example

```python
from everos_cloud_sdk.models.unprocessed_message_dto import UnprocessedMessageDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UnprocessedMessageDTO from a JSON string
unprocessed_message_dto_instance = UnprocessedMessageDTO.from_json(json)
# print the JSON string representation of the object
print(UnprocessedMessageDTO.to_json())

# convert the object into a dict
unprocessed_message_dto_dict = unprocessed_message_dto_instance.to_dict()
# create an instance of UnprocessedMessageDTO from a dict
unprocessed_message_dto_from_dict = UnprocessedMessageDTO.from_dict(unprocessed_message_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


