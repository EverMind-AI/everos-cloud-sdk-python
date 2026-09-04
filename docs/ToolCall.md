# ToolCall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Tool-call id; the matching \&quot;tool\&quot; message echoes it as &#x60;tool_call_id&#x60;. | 
**type** | **str** | Tool-call kind. Always \&quot;function\&quot; today. | [optional] [default to 'function']
**function** | [**ToolCallFunction**](ToolCallFunction.md) | The function invoked, with its arguments. | 

## Example

```python
from everos_cloud.models.tool_call import ToolCall

# TODO update the JSON string below
json = "{}"
# create an instance of ToolCall from a JSON string
tool_call_instance = ToolCall.from_json(json)
# print the JSON string representation of the object
print(ToolCall.to_json())

# convert the object into a dict
tool_call_dict = tool_call_instance.to_dict()
# create an instance of ToolCall from a dict
tool_call_from_dict = ToolCall.from_dict(tool_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


