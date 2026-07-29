# MessageItem

One message in an /add batch (spec §2). ``content`` accepts a plain string (shorthand for a single text ContentItem) or an explicit ContentItem list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender_id** | **str** |  | 
**sender_name** | **str** |  | [optional] 
**role** | **str** |  | 
**timestamp** | **int** |  | 
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


