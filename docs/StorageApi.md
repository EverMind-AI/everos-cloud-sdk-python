# everos_cloud.StorageApi

All URIs are relative to *https://api.evermind.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sign_objects**](StorageApi.md#sign_objects) | **POST** /api/v2/object/sign | Get multimodal upload URLs


# **sign_objects**
> SignEnvelope sign_objects(sign_request)

Get multimodal upload URLs

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.sign_envelope import SignEnvelope
from everos_cloud.models.sign_request import SignRequest
from everos_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.evermind.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = everos_cloud.Configuration(
    host = "https://api.evermind.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = everos_cloud.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with everos_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = everos_cloud.StorageApi(api_client)
    sign_request = everos_cloud.SignRequest() # SignRequest | 

    try:
        # Get multimodal upload URLs
        api_response = api_instance.sign_objects(sign_request)
        print("The response of StorageApi->sign_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->sign_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sign_request** | [**SignRequest**](SignRequest.md)|  | 

### Return type

[**SignEnvelope**](SignEnvelope.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Envelope response (MMS returns HTTP 200 for every business outcome; only unmatched routes return 404). &#x60;status: 0&#x60; means success and &#x60;result.data&#x60; is a SignResponse. Non-zero &#x60;status&#x60; values seen on this endpoint:  - &#x60;20003&#x60; — request body bind failure (malformed JSON). - &#x60;2018&#x60;  — parameter validation failed (e.g. missing &#x60;objectList&#x60;,   &#x60;fileId&#x60;, &#x60;fileName&#x60;, or &#x60;fileType&#x60;); &#x60;result.data&#x60; is the   validator error string. - &#x60;1012&#x60;  — &#x60;mms-token&#x60; missing, invalid, expired, or revoked   (emitted by the auth middleware before the handler runs). - &#x60;1013&#x60;  — token lacks the required &#x60;object:sign&#x60; scope. - &#x60;1007&#x60;  — &#x60;objectList&#x60; exceeds the per-request limit of 50. - &#x60;1002&#x60;  — &#x60;fileType&#x60; not one of image/video/file. - &#x60;1009&#x60;  — duplicate &#x60;fileId&#x60; within the request. - &#x60;1004&#x60;  — S3 operation failed (bucket unavailable). - &#x60;1005&#x60;  — presigned POST generation failed. - &#x60;2015&#x60;  — object metadata persistence failed. - &#x60;20001&#x60; — unhandled internal server error.  |  -  |
**401** | Missing or invalid bearer token. |  -  |
**403** | Authenticated but not permitted — either rejected by the auth service, or the account&#39;s memory API version does not match the interface version implied by the path (a v1 account calling an /api/v2 route). |  -  |
**429** | Rate limit or quota exceeded. |  -  |
**503** | The gateway could not reach the authentication service. Transient — retry with backoff. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

