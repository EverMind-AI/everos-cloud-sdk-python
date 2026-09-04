# ValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc** | [**List[ValidationErrorLocInner]**](ValidationErrorLocInner.md) | Path to the offending field, from the body root. | 
**msg** | **str** | What is wrong with it. | 
**type** | **str** | Machine-readable validation-error kind. | 

## Example

```python
from everos_cloud.models.validation_error import ValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationError from a JSON string
validation_error_instance = ValidationError.from_json(json)
# print the JSON string representation of the object
print(ValidationError.to_json())

# convert the object into a dict
validation_error_dict = validation_error_instance.to_dict()
# create an instance of ValidationError from a dict
validation_error_from_dict = ValidationError.from_dict(validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


