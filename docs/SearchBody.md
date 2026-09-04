# SearchBody

POST body (kb_id rides the path, not the body).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | [optional] 
**method** | **str** | Retrieval strategy: \&quot;keyword\&quot; (lexical), \&quot;vector\&quot; (embedding similarity) or \&quot;hybrid\&quot; (default, both). | [optional] [default to 'hybrid']
**page** | **int** | Filter-only page number; query search supports page 1 only | [optional] [default to 1]
**top_k** | **int** | Maximum number of topics to return, 1 to 100 (default 10). On a query search the server also bounds the result by its rerank pool — 50 candidates by default — so asking for more than that returns what the pool held. On a filter-only request (tags without a query) it is the page size instead, and &#x60;page&#x60; walks the rest. | [optional] [default to 10]
**score_threshold** | **float** |  | [optional] 
**include** | **List[str]** | e.g. [&#39;content&#39;] | [optional] [default to []]
**boost_tag_ids** | **List[str]** | Reweight, do not filter: topics carrying these tags are pushed up, and topics without them still come back. Use &#x60;filters.tag_ids&#x60; when the intent is to exclude everything else. | [optional] [default to []]
**filters** | [**SearchFilters**](SearchFilters.md) | Optional filters narrowing what is searched. | [optional] 

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


