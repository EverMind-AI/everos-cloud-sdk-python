# KbSearchData

Knowledge search response payload. Prefixed ``Kb`` to stay distinct from ``memory_api.SearchData`` — two same-named models under ``SuccessEnvelope[...]`` collide to a non-deterministic OpenAPI component name (see openapi-sync / check-openapi).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hits** | [**List[SearchHit]**](SearchHit.md) |  | [optional] 
**total** | **int** |  | [optional] [default to 0]
**took_ms** | **float** |  | [optional] [default to 0.0]

## Example

```python
from everos_cloud.models.kb_search_data import KbSearchData

# TODO update the JSON string below
json = "{}"
# create an instance of KbSearchData from a JSON string
kb_search_data_instance = KbSearchData.from_json(json)
# print the JSON string representation of the object
print(KbSearchData.to_json())

# convert the object into a dict
kb_search_data_dict = kb_search_data_instance.to_dict()
# create an instance of KbSearchData from a dict
kb_search_data_from_dict = KbSearchData.from_dict(kb_search_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


