# everos_cloud_sdk.HealthApi

All URIs are relative to *https://api.evermind.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check_health_get**](HealthApi.md#health_check_health_get) | **GET** /health | Health check


# **health_check_health_get**
> Dict[str, object] health_check_health_get()

Health check

Check system health status

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud_sdk
from everos_cloud_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.evermind.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = everos_cloud_sdk.Configuration(
    host = "https://api.evermind.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = everos_cloud_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with everos_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = everos_cloud_sdk.HealthApi(api_client)

    try:
        # Health check
        api_response = api_instance.health_check_health_get()
        print("The response of HealthApi->health_check_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->health_check_health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

