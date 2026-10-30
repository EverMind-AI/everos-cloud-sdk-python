# ContextInput

Request body of `POST /api/v2/memory/context`.  The same fields as the `/search` request, except that `method` is fixed to `\"context\"`, `min_score` is not supported, and `radius`, `enable_llm_rerank` and `with_readable_episode` are not accepted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | Scope to search in, defaulting to \&quot;default\&quot;. Must match the pair used on write. | [optional] [default to 'default']
**project_id** | **str** | Second half of the scope, defaulting to \&quot;default\&quot;. | [optional] [default to 'default']
**user_id** | **str** |  | [optional] 
**agent_id** | **str** |  | [optional] 
**query** | **str** | The question to retrieve for. The loop keeps searching until it judges the evidence sufficient to answer it, so pass the whole question, not keywords. | 
**method** | **str** | Fixed to &#x60;\&quot;context\&quot;&#x60;; may be omitted. Any other value is a 422. | [optional] [default to 'context']
**top_k** | **int** | Maximum number of episodes returned. Either -1 (the default, letting the engine decide) or a value from 1 to 100; anything else is rejected with 422. | [optional] [default to -1]
**min_score** | **float** |  | [optional] 
**include_profile** | **bool** | Also return the user&#39;s profile alongside the episodes, as on /search. | [optional] [default to False]
**filters** | [**FilterNode**](FilterNode.md) |  | [optional] 

## Example

```python
from everos_cloud.models.context_input import ContextInput

# TODO update the JSON string below
json = "{}"
# create an instance of ContextInput from a JSON string
context_input_instance = ContextInput.from_json(json)
# print the JSON string representation of the object
print(ContextInput.to_json())

# convert the object into a dict
context_input_dict = context_input_instance.to_dict()
# create an instance of ContextInput from a dict
context_input_from_dict = ContextInput.from_dict(context_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


