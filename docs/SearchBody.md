# SearchBody

POST body (kb_id rides the path, not the body).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | 
**method** | **str** |  | [optional] [default to 'hybrid']
**top_k** | **int** |  | [optional] [default to 10]
**score_threshold** | **float** |  | [optional] 
**include** | **List[str]** | e.g. [&#39;content&#39;] | [optional] 
**filters** | [**SearchFilters**](SearchFilters.md) |  | [optional] 

## Example

```python
from everos_cloud.models.search_body import SearchBody

# TODO update the JSON string below
json = "{}"
# create an instance of SearchBody from a JSON string
search_body_instance = SearchBody.from_json(json)
# print the JSON string representation of the object
print(SearchBody.to_json())

# convert the object into a dict
search_body_dict = search_body_instance.to_dict()
# create an instance of SearchBody from a dict
search_body_from_dict = SearchBody.from_dict(search_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


