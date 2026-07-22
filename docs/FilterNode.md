# FilterNode

One Filters DSL node — recursive ``AND`` / ``OR`` arrays plus arbitrary scalar field conditions at the same level.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[FilterNode]**](FilterNode.md) |  | [optional] 
**var_or** | [**List[FilterNode]**](FilterNode.md) |  | [optional] 

## Example

```python
from everos_cloud_sdk.models.filter_node import FilterNode

# TODO update the JSON string below
json = "{}"
# create an instance of FilterNode from a JSON string
filter_node_instance = FilterNode.from_json(json)
# print the JSON string representation of the object
print(FilterNode.to_json())

# convert the object into a dict
filter_node_dict = filter_node_instance.to_dict()
# create an instance of FilterNode from a dict
filter_node_from_dict = FilterNode.from_dict(filter_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


