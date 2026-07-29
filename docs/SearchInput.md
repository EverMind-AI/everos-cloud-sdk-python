# SearchInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | [optional] [default to 'default']
**project_id** | **str** |  | [optional] [default to 'default']
**user_id** | **str** |  | [optional] 
**agent_id** | **str** |  | [optional] 
**query** | **str** |  | 
**method** | **str** |  | [optional] [default to 'hybrid']
**top_k** | **int** |  | [optional] [default to -1]
**radius** | **float** |  | [optional] 
**min_score** | **float** |  | [optional] 
**include_profile** | **bool** |  | [optional] [default to False]
**enable_llm_rerank** | **bool** |  | [optional] [default to False]
**filters** | [**FilterNode**](FilterNode.md) |  | [optional] 

## Example

```python
from everos_cloud.models.search_input import SearchInput

# TODO update the JSON string below
json = "{}"
# create an instance of SearchInput from a JSON string
search_input_instance = SearchInput.from_json(json)
# print the JSON string representation of the object
print(SearchInput.to_json())

# convert the object into a dict
search_input_dict = search_input_instance.to_dict()
# create an instance of SearchInput from a dict
search_input_from_dict = SearchInput.from_dict(search_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


