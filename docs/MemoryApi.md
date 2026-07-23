# everos_cloud_sdk.MemoryApi

All URIs are relative to *https://api.evermind.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_memory**](MemoryApi.md#add_memory) | **POST** /api/v2/memory/add | Add messages [OSS + Cloud]
[**delete_memory**](MemoryApi.md#delete_memory) | **POST** /api/v2/memory/delete | Delete memories [Cloud-only]
[**edit_profile**](MemoryApi.md#edit_profile) | **POST** /api/v2/memory/edit | Edit profile items [Cloud-only]
[**flush_api_v2_memory_flush_post**](MemoryApi.md#flush_api_v2_memory_flush_post) | **POST** /api/v2/memory/flush | Force boundary detection + extraction [OSS + Cloud]
[**get_memory**](MemoryApi.md#get_memory) | **POST** /api/v2/memory/get | Get memories (paginated) [OSS + Cloud]
[**search_memory**](MemoryApi.md#search_memory) | **POST** /api/v2/memory/search | Search memories [OSS + Cloud]


# **add_memory**
> SuccessEnvelopeAddData add_memory(add_input)

Add messages [OSS + Cloud]

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud_sdk
from everos_cloud_sdk.models.add_input import AddInput
from everos_cloud_sdk.models.success_envelope_add_data import SuccessEnvelopeAddData
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
    api_instance = everos_cloud_sdk.MemoryApi(api_client)
    add_input = everos_cloud_sdk.AddInput() # AddInput | 

    try:
        # Add messages [OSS + Cloud]
        api_response = api_instance.add_memory(add_input)
        print("The response of MemoryApi->add_memory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->add_memory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_input** | [**AddInput**](AddInput.md)|  | 

### Return type

[**SuccessEnvelopeAddData**](SuccessEnvelopeAddData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Synchronous write result (async_mode&#x3D;false). |  -  |
**422** | Validation Error |  -  |
**202** | Accepted for asynchronous processing (async_mode&#x3D;true, default). |  -  |
**401** | Missing or invalid bearer token. |  -  |
**403** | Authenticated but not permitted for this resource. |  -  |
**429** | Rate limit or quota exceeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_memory**
> SuccessEnvelopeDeleteData delete_memory(delete_input)

Delete memories [Cloud-only]

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud_sdk
from everos_cloud_sdk.models.delete_input import DeleteInput
from everos_cloud_sdk.models.success_envelope_delete_data import SuccessEnvelopeDeleteData
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
    api_instance = everos_cloud_sdk.MemoryApi(api_client)
    delete_input = everos_cloud_sdk.DeleteInput() # DeleteInput | 

    try:
        # Delete memories [Cloud-only]
        api_response = api_instance.delete_memory(delete_input)
        print("The response of MemoryApi->delete_memory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->delete_memory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_input** | [**DeleteInput**](DeleteInput.md)|  | 

### Return type

[**SuccessEnvelopeDeleteData**](SuccessEnvelopeDeleteData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**401** | Missing or invalid bearer token. |  -  |
**403** | Authenticated but not permitted for this resource. |  -  |
**429** | Rate limit or quota exceeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_profile**
> SuccessEnvelopeEditData edit_profile(edit_input)

Edit profile items [Cloud-only]

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud_sdk
from everos_cloud_sdk.models.edit_input import EditInput
from everos_cloud_sdk.models.success_envelope_edit_data import SuccessEnvelopeEditData
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
    api_instance = everos_cloud_sdk.MemoryApi(api_client)
    edit_input = everos_cloud_sdk.EditInput() # EditInput | 

    try:
        # Edit profile items [Cloud-only]
        api_response = api_instance.edit_profile(edit_input)
        print("The response of MemoryApi->edit_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->edit_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_input** | [**EditInput**](EditInput.md)|  | 

### Return type

[**SuccessEnvelopeEditData**](SuccessEnvelopeEditData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**401** | Missing or invalid bearer token. |  -  |
**403** | Authenticated but not permitted for this resource. |  -  |
**429** | Rate limit or quota exceeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flush_api_v2_memory_flush_post**
> SuccessEnvelopeFlushData flush_api_v2_memory_flush_post(flush_input)

Force boundary detection + extraction [OSS + Cloud]

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud_sdk
from everos_cloud_sdk.models.flush_input import FlushInput
from everos_cloud_sdk.models.success_envelope_flush_data import SuccessEnvelopeFlushData
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
    api_instance = everos_cloud_sdk.MemoryApi(api_client)
    flush_input = everos_cloud_sdk.FlushInput() # FlushInput | 

    try:
        # Force boundary detection + extraction [OSS + Cloud]
        api_response = api_instance.flush_api_v2_memory_flush_post(flush_input)
        print("The response of MemoryApi->flush_api_v2_memory_flush_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->flush_api_v2_memory_flush_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flush_input** | [**FlushInput**](FlushInput.md)|  | 

### Return type

[**SuccessEnvelopeFlushData**](SuccessEnvelopeFlushData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_memory**
> SuccessEnvelopeGetData get_memory(get_input)

Get memories (paginated) [OSS + Cloud]

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud_sdk
from everos_cloud_sdk.models.get_input import GetInput
from everos_cloud_sdk.models.success_envelope_get_data import SuccessEnvelopeGetData
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
    api_instance = everos_cloud_sdk.MemoryApi(api_client)
    get_input = everos_cloud_sdk.GetInput() # GetInput | 

    try:
        # Get memories (paginated) [OSS + Cloud]
        api_response = api_instance.get_memory(get_input)
        print("The response of MemoryApi->get_memory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->get_memory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_input** | [**GetInput**](GetInput.md)|  | 

### Return type

[**SuccessEnvelopeGetData**](SuccessEnvelopeGetData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**401** | Missing or invalid bearer token. |  -  |
**403** | Authenticated but not permitted for this resource. |  -  |
**429** | Rate limit or quota exceeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_memory**
> SuccessEnvelopeSearchData search_memory(search_input)

Search memories [OSS + Cloud]

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud_sdk
from everos_cloud_sdk.models.search_input import SearchInput
from everos_cloud_sdk.models.success_envelope_search_data import SuccessEnvelopeSearchData
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
    api_instance = everos_cloud_sdk.MemoryApi(api_client)
    search_input = everos_cloud_sdk.SearchInput() # SearchInput | 

    try:
        # Search memories [OSS + Cloud]
        api_response = api_instance.search_memory(search_input)
        print("The response of MemoryApi->search_memory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryApi->search_memory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_input** | [**SearchInput**](SearchInput.md)|  | 

### Return type

[**SuccessEnvelopeSearchData**](SuccessEnvelopeSearchData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**401** | Missing or invalid bearer token. |  -  |
**403** | Authenticated but not permitted for this resource. |  -  |
**429** | Rate limit or quota exceeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

