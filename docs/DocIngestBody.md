# DocIngestBody

Public POST/PUT documents request body (design §3.2 / §3.3). ``content`` is the object to ingest (its ``uri`` = the SMM object_key). On PUT the ``doc_id`` rides the path, not the body; on POST no id is supplied — the engine mints it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Human-readable name for the document. Until the async ingest finishes this is the only handle the caller has — the document id is minted downstream, so GET .../documents is resolved by title. | 
**content** | [**ContentItem**](ContentItem.md) | The object to ingest (its uri &#x3D; the SMM object_key) | 
**category_id** | **str** | Category id in this kb; omit for LLM auto-classify | [optional] [default to '']

## Example

```python
from everos_cloud.models.doc_ingest_body import DocIngestBody

# TODO update the JSON string below
json = "{}"
# create an instance of DocIngestBody from a JSON string
doc_ingest_body_instance = DocIngestBody.from_json(json)
# print the JSON string representation of the object
print(DocIngestBody.to_json())

# convert the object into a dict
doc_ingest_body_dict = doc_ingest_body_instance.to_dict()
# create an instance of DocIngestBody from a dict
doc_ingest_body_from_dict = DocIngestBody.from_dict(doc_ingest_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


