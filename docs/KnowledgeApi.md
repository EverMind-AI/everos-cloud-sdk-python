# everos_cloud.KnowledgeApi

All URIs are relative to *https://api.evermind.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_category**](KnowledgeApi.md#create_category) | **POST** /api/v2/knowledge_bases/{kb_id}/categories | Create a category
[**create_document**](KnowledgeApi.md#create_document) | **POST** /api/v2/knowledge_bases/{kb_id}/documents | Upload a document (async ingest)
[**create_knowledge_base**](KnowledgeApi.md#create_knowledge_base) | **POST** /api/v2/knowledge_bases | Create a knowledge base
[**delete_category**](KnowledgeApi.md#delete_category) | **DELETE** /api/v2/knowledge_bases/{kb_id}/categories/{category_id} | Delete a category
[**delete_document**](KnowledgeApi.md#delete_document) | **DELETE** /api/v2/knowledge_bases/{kb_id}/documents/{doc_id} | Delete a document (+ cascade nodes, P5)
[**delete_knowledge_base**](KnowledgeApi.md#delete_knowledge_base) | **DELETE** /api/v2/knowledge_bases/{kb_id} | Delete a knowledge base
[**get_document**](KnowledgeApi.md#get_document) | **GET** /api/v2/knowledge_bases/{kb_id}/documents/{doc_id} | Get a document (with topic_count)
[**get_knowledge_base**](KnowledgeApi.md#get_knowledge_base) | **GET** /api/v2/knowledge_bases/{kb_id} | Get a knowledge base
[**get_topic**](KnowledgeApi.md#get_topic) | **GET** /api/v2/knowledge_bases/{kb_id}/documents/{doc_id}/topics/{topic_id} | Get a topic&#39;s full content (inline / S3 transparent)
[**list_categories**](KnowledgeApi.md#list_categories) | **GET** /api/v2/knowledge_bases/{kb_id}/categories | List categories in a knowledge base
[**list_documents**](KnowledgeApi.md#list_documents) | **GET** /api/v2/knowledge_bases/{kb_id}/documents | List documents in a knowledge base
[**list_knowledge_bases**](KnowledgeApi.md#list_knowledge_bases) | **GET** /api/v2/knowledge_bases | List knowledge bases
[**list_topics**](KnowledgeApi.md#list_topics) | **GET** /api/v2/knowledge_bases/{kb_id}/documents/{doc_id}/topics | List a document&#39;s topic tree (optionally with each topic&#39;s content)
[**replace_document**](KnowledgeApi.md#replace_document) | **PUT** /api/v2/knowledge_bases/{kb_id}/documents/{doc_id} | Replace a document (async, atomic swap)
[**search_knowledge**](KnowledgeApi.md#search_knowledge) | **POST** /api/v2/knowledge_bases/{kb_id}/search | Search within a knowledge base (keyword / vector / hybrid)
[**update_category**](KnowledgeApi.md#update_category) | **PATCH** /api/v2/knowledge_bases/{kb_id}/categories/{category_id} | Update a category
[**update_document**](KnowledgeApi.md#update_document) | **PATCH** /api/v2/knowledge_bases/{kb_id}/documents/{doc_id} | Update document metadata (title / category)
[**update_knowledge_base**](KnowledgeApi.md#update_knowledge_base) | **PATCH** /api/v2/knowledge_bases/{kb_id} | Update a knowledge base


# **create_category**
> SuccessEnvelopeCategoryData create_category(kb_id, category_create_body)

Create a category

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.category_create_body import CategoryCreateBody
from everos_cloud.models.success_envelope_category_data import SuccessEnvelopeCategoryData
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
    api_instance = everos_cloud.KnowledgeApi(api_client)
    kb_id = 'kb_id_example' # str | 
    category_create_body = everos_cloud.CategoryCreateBody() # CategoryCreateBody | 

    try:
        # Create a category
        api_response = api_instance.create_category(kb_id, category_create_body)
        print("The response of KnowledgeApi->create_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->create_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**|  | 
 **category_create_body** | [**CategoryCreateBody**](CategoryCreateBody.md)|  | 

### Return type

[**SuccessEnvelopeCategoryData**](SuccessEnvelopeCategoryData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_document**
> SuccessEnvelopeDocIngestData create_document(kb_id, doc_ingest_body)

Upload a document (async ingest)

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.doc_ingest_body import DocIngestBody
from everos_cloud.models.success_envelope_doc_ingest_data import SuccessEnvelopeDocIngestData
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
    api_instance = everos_cloud.KnowledgeApi(api_client)
    kb_id = 'kb_id_example' # str | 
    doc_ingest_body = everos_cloud.DocIngestBody() # DocIngestBody | 

    try:
        # Upload a document (async ingest)
        api_response = api_instance.create_document(kb_id, doc_ingest_body)
        print("The response of KnowledgeApi->create_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->create_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**|  | 
 **doc_ingest_body** | [**DocIngestBody**](DocIngestBody.md)|  | 

### Return type

[**SuccessEnvelopeDocIngestData**](SuccessEnvelopeDocIngestData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_knowledge_base**
> SuccessEnvelopeKbData create_knowledge_base(kb_create_input)

Create a knowledge base

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.kb_create_input import KbCreateInput
from everos_cloud.models.success_envelope_kb_data import SuccessEnvelopeKbData
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
    api_instance = everos_cloud.KnowledgeApi(api_client)
    kb_create_input = everos_cloud.KbCreateInput() # KbCreateInput | 

    try:
        # Create a knowledge base
        api_response = api_instance.create_knowledge_base(kb_create_input)
        print("The response of KnowledgeApi->create_knowledge_base:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->create_knowledge_base: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_create_input** | [**KbCreateInput**](KbCreateInput.md)|  | 

### Return type

[**SuccessEnvelopeKbData**](SuccessEnvelopeKbData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_category**
> SuccessEnvelopeCategoryDeleteData delete_category(kb_id, category_id)

Delete a category

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.success_envelope_category_delete_data import SuccessEnvelopeCategoryDeleteData
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
    api_instance = everos_cloud.KnowledgeApi(api_client)
    kb_id = 'kb_id_example' # str | 
    category_id = 'category_id_example' # str | 

    try:
        # Delete a category
        api_response = api_instance.delete_category(kb_id, category_id)
        print("The response of KnowledgeApi->delete_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->delete_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**|  | 
 **category_id** | **str**|  | 

### Return type

[**SuccessEnvelopeCategoryDeleteData**](SuccessEnvelopeCategoryDeleteData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document**
> SuccessEnvelopeDocDeleteData delete_document(kb_id, doc_id)

Delete a document (+ cascade nodes, P5)

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.success_envelope_doc_delete_data import SuccessEnvelopeDocDeleteData
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
    api_instance = everos_cloud.KnowledgeApi(api_client)
    kb_id = 'kb_id_example' # str | 
    doc_id = 'doc_id_example' # str | 

    try:
        # Delete a document (+ cascade nodes, P5)
        api_response = api_instance.delete_document(kb_id, doc_id)
        print("The response of KnowledgeApi->delete_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->delete_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**|  | 
 **doc_id** | **str**|  | 

### Return type

[**SuccessEnvelopeDocDeleteData**](SuccessEnvelopeDocDeleteData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_knowledge_base**
> SuccessEnvelopeKbDeleteData delete_knowledge_base(kb_id)

Delete a knowledge base

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.success_envelope_kb_delete_data import SuccessEnvelopeKbDeleteData
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
    api_instance = everos_cloud.KnowledgeApi(api_client)
    kb_id = 'kb_id_example' # str | 

    try:
        # Delete a knowledge base
        api_response = api_instance.delete_knowledge_base(kb_id)
        print("The response of KnowledgeApi->delete_knowledge_base:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->delete_knowledge_base: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**|  | 

### Return type

[**SuccessEnvelopeKbDeleteData**](SuccessEnvelopeKbDeleteData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> SuccessEnvelopeDocData get_document(kb_id, doc_id)

Get a document (with topic_count)

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.success_envelope_doc_data import SuccessEnvelopeDocData
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
    api_instance = everos_cloud.KnowledgeApi(api_client)
    kb_id = 'kb_id_example' # str | 
    doc_id = 'doc_id_example' # str | 

    try:
        # Get a document (with topic_count)
        api_response = api_instance.get_document(kb_id, doc_id)
        print("The response of KnowledgeApi->get_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->get_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**|  | 
 **doc_id** | **str**|  | 

### Return type

[**SuccessEnvelopeDocData**](SuccessEnvelopeDocData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_knowledge_base**
> SuccessEnvelopeKbData get_knowledge_base(kb_id)

Get a knowledge base

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.success_envelope_kb_data import SuccessEnvelopeKbData
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
    api_instance = everos_cloud.KnowledgeApi(api_client)
    kb_id = 'kb_id_example' # str | 

    try:
        # Get a knowledge base
        api_response = api_instance.get_knowledge_base(kb_id)
        print("The response of KnowledgeApi->get_knowledge_base:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->get_knowledge_base: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**|  | 

### Return type

[**SuccessEnvelopeKbData**](SuccessEnvelopeKbData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic**
> SuccessEnvelopeTopicDetailData get_topic(kb_id, doc_id, topic_id)

Get a topic's full content (inline / S3 transparent)

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.success_envelope_topic_detail_data import SuccessEnvelopeTopicDetailData
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
    api_instance = everos_cloud.KnowledgeApi(api_client)
    kb_id = 'kb_id_example' # str | 
    doc_id = 'doc_id_example' # str | 
    topic_id = 'topic_id_example' # str | 

    try:
        # Get a topic's full content (inline / S3 transparent)
        api_response = api_instance.get_topic(kb_id, doc_id, topic_id)
        print("The response of KnowledgeApi->get_topic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->get_topic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**|  | 
 **doc_id** | **str**|  | 
 **topic_id** | **str**|  | 

### Return type

[**SuccessEnvelopeTopicDetailData**](SuccessEnvelopeTopicDetailData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_categories**
> SuccessEnvelopeCategoryListData list_categories(kb_id)

List categories in a knowledge base

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.success_envelope_category_list_data import SuccessEnvelopeCategoryListData
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
    api_instance = everos_cloud.KnowledgeApi(api_client)
    kb_id = 'kb_id_example' # str | 

    try:
        # List categories in a knowledge base
        api_response = api_instance.list_categories(kb_id)
        print("The response of KnowledgeApi->list_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->list_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**|  | 

### Return type

[**SuccessEnvelopeCategoryListData**](SuccessEnvelopeCategoryListData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_documents**
> SuccessEnvelopeDocListData list_documents(kb_id, category_id=category_id, page=page, page_size=page_size)

List documents in a knowledge base

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.success_envelope_doc_list_data import SuccessEnvelopeDocListData
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
    api_instance = everos_cloud.KnowledgeApi(api_client)
    kb_id = 'kb_id_example' # str | 
    category_id = 'category_id_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)

    try:
        # List documents in a knowledge base
        api_response = api_instance.list_documents(kb_id, category_id=category_id, page=page, page_size=page_size)
        print("The response of KnowledgeApi->list_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->list_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**|  | 
 **category_id** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]

### Return type

[**SuccessEnvelopeDocListData**](SuccessEnvelopeDocListData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_knowledge_bases**
> SuccessEnvelopeKbListData list_knowledge_bases(page=page, page_size=page_size, owner_id=owner_id)

List knowledge bases

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.success_envelope_kb_list_data import SuccessEnvelopeKbListData
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
    api_instance = everos_cloud.KnowledgeApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)
    owner_id = 'owner_id_example' # str |  (optional)

    try:
        # List knowledge bases
        api_response = api_instance.list_knowledge_bases(page=page, page_size=page_size, owner_id=owner_id)
        print("The response of KnowledgeApi->list_knowledge_bases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->list_knowledge_bases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]
 **owner_id** | **str**|  | [optional] 

### Return type

[**SuccessEnvelopeKbListData**](SuccessEnvelopeKbListData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_topics**
> SuccessEnvelopeTopicListData list_topics(kb_id, doc_id, include=include)

List a document's topic tree (optionally with each topic's content)

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.success_envelope_topic_list_data import SuccessEnvelopeTopicListData
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
    api_instance = everos_cloud.KnowledgeApi(api_client)
    kb_id = 'kb_id_example' # str | 
    doc_id = 'doc_id_example' # str | 
    include = ['include_example'] # List[Optional[str]] | Extra fields to hydrate, e.g. `include=content` for full bodies (optional)

    try:
        # List a document's topic tree (optionally with each topic's content)
        api_response = api_instance.list_topics(kb_id, doc_id, include=include)
        print("The response of KnowledgeApi->list_topics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->list_topics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**|  | 
 **doc_id** | **str**|  | 
 **include** | [**List[Optional[str]]**](str.md)| Extra fields to hydrate, e.g. &#x60;include&#x3D;content&#x60; for full bodies | [optional] 

### Return type

[**SuccessEnvelopeTopicListData**](SuccessEnvelopeTopicListData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_document**
> SuccessEnvelopeDocIngestData replace_document(kb_id, doc_id, doc_ingest_body)

Replace a document (async, atomic swap)

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.doc_ingest_body import DocIngestBody
from everos_cloud.models.success_envelope_doc_ingest_data import SuccessEnvelopeDocIngestData
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
    api_instance = everos_cloud.KnowledgeApi(api_client)
    kb_id = 'kb_id_example' # str | 
    doc_id = 'doc_id_example' # str | 
    doc_ingest_body = everos_cloud.DocIngestBody() # DocIngestBody | 

    try:
        # Replace a document (async, atomic swap)
        api_response = api_instance.replace_document(kb_id, doc_id, doc_ingest_body)
        print("The response of KnowledgeApi->replace_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->replace_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**|  | 
 **doc_id** | **str**|  | 
 **doc_ingest_body** | [**DocIngestBody**](DocIngestBody.md)|  | 

### Return type

[**SuccessEnvelopeDocIngestData**](SuccessEnvelopeDocIngestData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_knowledge**
> SuccessEnvelopeKbSearchData search_knowledge(kb_id, search_body)

Search within a knowledge base (keyword / vector / hybrid)

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.search_body import SearchBody
from everos_cloud.models.success_envelope_kb_search_data import SuccessEnvelopeKbSearchData
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
    api_instance = everos_cloud.KnowledgeApi(api_client)
    kb_id = 'kb_id_example' # str | 
    search_body = everos_cloud.SearchBody() # SearchBody | 

    try:
        # Search within a knowledge base (keyword / vector / hybrid)
        api_response = api_instance.search_knowledge(kb_id, search_body)
        print("The response of KnowledgeApi->search_knowledge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->search_knowledge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**|  | 
 **search_body** | [**SearchBody**](SearchBody.md)|  | 

### Return type

[**SuccessEnvelopeKbSearchData**](SuccessEnvelopeKbSearchData.md)

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

# **update_category**
> SuccessEnvelopeCategoryData update_category(kb_id, category_id, category_patch_body)

Update a category

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.category_patch_body import CategoryPatchBody
from everos_cloud.models.success_envelope_category_data import SuccessEnvelopeCategoryData
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
    api_instance = everos_cloud.KnowledgeApi(api_client)
    kb_id = 'kb_id_example' # str | 
    category_id = 'category_id_example' # str | 
    category_patch_body = everos_cloud.CategoryPatchBody() # CategoryPatchBody | 

    try:
        # Update a category
        api_response = api_instance.update_category(kb_id, category_id, category_patch_body)
        print("The response of KnowledgeApi->update_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->update_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**|  | 
 **category_id** | **str**|  | 
 **category_patch_body** | [**CategoryPatchBody**](CategoryPatchBody.md)|  | 

### Return type

[**SuccessEnvelopeCategoryData**](SuccessEnvelopeCategoryData.md)

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

# **update_document**
> SuccessEnvelopeDocPatchData update_document(kb_id, doc_id, doc_patch_body)

Update document metadata (title / category)

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.doc_patch_body import DocPatchBody
from everos_cloud.models.success_envelope_doc_patch_data import SuccessEnvelopeDocPatchData
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
    api_instance = everos_cloud.KnowledgeApi(api_client)
    kb_id = 'kb_id_example' # str | 
    doc_id = 'doc_id_example' # str | 
    doc_patch_body = everos_cloud.DocPatchBody() # DocPatchBody | 

    try:
        # Update document metadata (title / category)
        api_response = api_instance.update_document(kb_id, doc_id, doc_patch_body)
        print("The response of KnowledgeApi->update_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->update_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**|  | 
 **doc_id** | **str**|  | 
 **doc_patch_body** | [**DocPatchBody**](DocPatchBody.md)|  | 

### Return type

[**SuccessEnvelopeDocPatchData**](SuccessEnvelopeDocPatchData.md)

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

# **update_knowledge_base**
> SuccessEnvelopeKbData update_knowledge_base(kb_id, kb_patch_body)

Update a knowledge base

### Example

* Bearer Authentication (BearerAuth):

```python
import everos_cloud
from everos_cloud.models.kb_patch_body import KbPatchBody
from everos_cloud.models.success_envelope_kb_data import SuccessEnvelopeKbData
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
    api_instance = everos_cloud.KnowledgeApi(api_client)
    kb_id = 'kb_id_example' # str | 
    kb_patch_body = everos_cloud.KbPatchBody() # KbPatchBody | 

    try:
        # Update a knowledge base
        api_response = api_instance.update_knowledge_base(kb_id, kb_patch_body)
        print("The response of KnowledgeApi->update_knowledge_base:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->update_knowledge_base: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**|  | 
 **kb_patch_body** | [**KbPatchBody**](KbPatchBody.md)|  | 

### Return type

[**SuccessEnvelopeKbData**](SuccessEnvelopeKbData.md)

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

