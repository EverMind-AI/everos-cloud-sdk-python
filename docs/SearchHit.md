# SearchHit

A topic hit from recall or a document hit from filter-only search.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | What this hit is. Always \&quot;topic\&quot; today — the unit of knowledge retrieval. | 
**id** | **str** | The topic&#39;s id; fetch its full body with GET .../topics/{topic_id}. | 
**doc_id** | **str** | The document the topic belongs to. | 
**kb_id** | **str** | The knowledge base searched. | 
**category_id** | **str** | The category that document is filed under; empty when uncategorized. | [optional] [default to '']
**category_name** | **str** |  | [optional] 
**name** | **str** | The topic&#39;s title. | 
**depth** | **int** | The topic&#39;s depth in the document tree. | [optional] [default to 0]
**summary** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**score** | **float** | Relevance of this topic to the query, and NOT a raw keyword or vector score: candidates from every method are reranked by a cross-encoder, min-max normalized WITHIN THIS RESPONSE, then given a category boost (up to 0.1) and, when &#x60;boost_tag_ids&#x60; was passed, a tag-coverage boost (up to 0.3). So it lands in roughly 0.0–1.4, the best hit of any response sits near the top of that range by construction, and scores compare inside one response but not across responses or queries. Three edge values to expect: every hit comes back at 0.5 when the reranker cannot separate the pool, every hit is 0.0 on a filter-only request (tags without a query, which never runs relevance at all), and a hit carries a synthetic -100.0 when its rerank batch failed — that is a fail-soft marker, not a relevance judgement. | 
**retrieval_method** | **str** | The retrieval strategy this search ran with, so every hit in one response carries the same value and a stored or traced response is self-describing. It echoes the request&#39;s &#x60;method&#x60;, except on a filter-only request (tags without a query), which reports \&quot;filter\&quot; because no retrieval ran. It is deliberately NOT per-hit provenance: in a hybrid search the two lanes are fused, and hits recalled by only one of them still report \&quot;hybrid\&quot;. | 
**source** | **str** |  | [optional] 
**document** | [**DocumentContext**](DocumentContext.md) |  | [optional] 
**tags** | [**List[TagRef]**](TagRef.md) | The semantic tags materialized on this topic. | 
**updated_at** | **datetime** |  | [optional] 

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


