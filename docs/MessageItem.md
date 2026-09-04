# MessageItem

One message in an /add batch (spec §2). ``content`` accepts a plain string (shorthand for a single text ContentItem) or an explicit ContentItem list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender_id** | **str** | Who produced this message — the user id for a user turn, the agent id for an assistant turn. This is the identifier /api/v2/memory/get and /api/v2/memory/search later scope by (&#x60;user_id&#x60; / &#x60;agent_id&#x60;). | 
**sender_name** | **str** |  | [optional] 
**role** | **str** | Turn type: \&quot;user\&quot;, \&quot;assistant\&quot;, or \&quot;tool\&quot; for a tool result. An agent trajectory uses the OpenAI shape — an \&quot;assistant\&quot; message carrying &#x60;tool_calls&#x60;, followed by a \&quot;tool\&quot; message carrying &#x60;tool_call_id&#x60;. | 
**timestamp** | **int** | When the message was produced, as a UNIX timestamp in MILLISECONDS. A seconds-scale value is rejected with 422 rather than silently rescaled, because a window mixing the two would mis-order and mis-split. | 
**content** | [**Content**](Content.md) |  | 
**tool_calls** | [**List[ToolCall]**](ToolCall.md) |  | [optional] 
**tool_call_id** | **str** |  | [optional] 

## Example

```python
from everos_cloud.models.message_item import MessageItem

# TODO update the JSON string below
json = "{}"
# create an instance of MessageItem from a JSON string
message_item_instance = MessageItem.from_json(json)
# print the JSON string representation of the object
print(MessageItem.to_json())

# convert the object into a dict
message_item_dict = message_item_instance.to_dict()
# create an instance of MessageItem from a dict
message_item_from_dict = MessageItem.from_dict(message_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


