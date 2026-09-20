# FeedbackInput

Rate one memory record [Cloud-only].  The target is addressed the way the read APIs return it: ``memory_type`` + ``memory_id``, plus ``item_id`` for a profile, whose rateable unit is one item inside ``profile_data`` rather than the whole document. Everything identifying (tenant, submitter) is derived on the server; the whitelist is closed.  A reason is DESCRIPTIVE. No code triggers a mutation by itself — ``privacy`` in particular is a signal, not a deletion request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_type** | **str** | Kind of the target memory, as named by memory.get / search. | 
**memory_id** | **str** | The target&#39;s &#x60;id&#x60; from memory.get / search (the profile document&#39;s id for &#x60;profile&#x60;). | 
**item_id** | **str** |  | [optional] 
**rating** | **str** | Direction of the explicit assessment. | 
**reason** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**suggestion** | **str** |  | [optional] 

## Example

```python
from everos_cloud.models.feedback_input import FeedbackInput

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackInput from a JSON string
feedback_input_instance = FeedbackInput.from_json(json)
# print the JSON string representation of the object
print(FeedbackInput.to_json())

# convert the object into a dict
feedback_input_dict = feedback_input_instance.to_dict()
# create an instance of FeedbackInput from a dict
feedback_input_from_dict = FeedbackInput.from_dict(feedback_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


