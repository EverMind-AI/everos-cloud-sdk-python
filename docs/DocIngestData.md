# DocIngestData

202 response for document create / replace (design §3.2 / §3.3). ``id`` is the document id (engine-minted on create). The engine ingests synchronously; ``status`` / ``task_id`` mirror the async contract so this endpoint is wire-identical to the gateway edge — the real task lifecycle (queued -> processing -> success/failed) is maintained by msgbus/Redis, a separate layer. Ingest success is authoritative via GET documents/{id} (topic_count > 0).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document id. Present only when the engine is called directly; the gateway&#39;s async ack omits it (the id is minted downstream), so SDK callers resolve it from GET .../documents by title. | [optional] 
**status** | **str** | Async task status (contract-nominal at the engine) | [default to 'queued']
**task_id** | **str** | Async task handle (contract-nominal at the engine) | [default to '']

## Example

```python
from everos_cloud.models.doc_ingest_data import DocIngestData

# TODO update the JSON string below
json = "{}"
# create an instance of DocIngestData from a JSON string
doc_ingest_data_instance = DocIngestData.from_json(json)
# print the JSON string representation of the object
print(DocIngestData.to_json())

# convert the object into a dict
doc_ingest_data_dict = doc_ingest_data_instance.to_dict()
# create an instance of DocIngestData from a dict
doc_ingest_data_from_dict = DocIngestData.from_dict(doc_ingest_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


