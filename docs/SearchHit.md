# SearchHit

A single search hit. ``object`` self-describes the unit (currently always topic).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'topic']
**id** | **str** |  | 
**doc_id** | **str** |  | 
**kb_id** | **str** |  | 
**category_id** | **str** |  | [optional] [default to '']
**category_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] [default to '']
**depth** | **int** |  | [optional] [default to 0]
**summary** | **str** |  | [optional] [default to '']
**content** | **str** |  | [optional] 
**score** | **float** |  | [optional] [default to 0.0]
**retrieval_method** | **str** |  | [optional] [default to 'hybrid']
**source** | **str** |  | [optional] 
**document** | [**DocumentContext**](DocumentContext.md) |  | [optional] 

## Example

```python
from everos_cloud.models.search_hit import SearchHit

# TODO update the JSON string below
json = "{}"
# create an instance of SearchHit from a JSON string
search_hit_instance = SearchHit.from_json(json)
# print the JSON string representation of the object
print(SearchHit.to_json())

# convert the object into a dict
search_hit_dict = search_hit_instance.to_dict()
# create an instance of SearchHit from a dict
search_hit_from_dict = SearchHit.from_dict(search_hit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


