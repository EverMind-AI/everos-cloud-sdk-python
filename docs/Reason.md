# Reason

Why the operator made the change. OPTIONAL on both ops: it is recorded on the audit event for quality analysis, never used to gate anything. When given, ``code`` is required and ``note`` is free text.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | What was wrong, from the fixed list — hallucination, wrong_subject, wrong_time, redundant, missing, privacy, style, other. Required whenever a reason is given. Same base list as &#x60;FeedbackInput.reason&#x60; plus &#x60;missing&#x60;, which only an edit can express (an operator fixes a record that left something out; a rating always names a memory that exists). On the contract this SDK is generated from (engine release-20260901_v15) &#x60;outdated&#x60; is not yet accepted here — the engine adds it in its next release; until then record an outdated-type fix as &#x60;wrong_time&#x60; or &#x60;other&#x60;. | 
**note** | **str** |  | [optional] 

## Example

```python
from everos_cloud.models.reason import Reason

# TODO update the JSON string below
json = "{}"
# create an instance of Reason from a JSON string
reason_instance = Reason.from_json(json)
# print the JSON string representation of the object
print(Reason.to_json())

# convert the object into a dict
reason_dict = reason_instance.to_dict()
# create an instance of Reason from a dict
reason_from_dict = Reason.from_dict(reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


