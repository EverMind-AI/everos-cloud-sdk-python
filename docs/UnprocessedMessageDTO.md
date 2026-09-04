# UnprocessedMessageDTO

Buffered raw message not yet extracted (no owner — inference happens after boundary detection). Returned by /search only when ``filters.session_id`` is a top-level eq scalar (spec §4 / appendix E).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Buffered-message id. | 
**app_id** | **str** | The business-semantic scope the message was written under. | 
**project_id** | **str** | Second half of that scope. | 
**session_id** | **str** | The session the message is buffered under. | 
**sender_id** | **str** | Who sent it. | 
**sender_name** | **str** |  | [optional] 
**role** | **str** | \&quot;user\&quot;, \&quot;assistant\&quot; or \&quot;tool\&quot;, as submitted. | 
**content** | [**Content1**](Content1.md) |  | 
**timestamp** | **datetime** | When the message was produced (ISO 8601). | 
**tool_calls** | [**List[ToolCall]**](ToolCall.md) |  | [optional] 
**tool_call_id** | **str** |  | [optional] 

## Example

```python
from everos_cloud.models.unprocessed_message_dto import UnprocessedMessageDTO

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


