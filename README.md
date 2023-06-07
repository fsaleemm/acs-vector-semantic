
# Azure Cognitive Search - Vector, Semantic & Hybrid Search

This repo has python code to demonstrate the use of Azure Cognitive Search with Open AI to provide vector, semantic, and hybrid search capabilities. The code is based on the [Azure Cognitive Search - Vector Search (Preview)](https://github.com/Azure/cognitive-search-vector-pr).

## Infrastructure Setup

Clone the repo and create a virtual environment for the python scripts.

```ps
git clone https://github.com/fsaleemm/acs-vector-semantic.git
cd acs-vector-semantic
```

Deploy the following Cognitive Services:

1. Azure Open AI
1. Cognitive Search Service

```ps
$LOCATION="eastus"
az deployment sub create -n "acs-semantic-vector" -l $LOCATION -f infra/main.bicep -p infra/main.parameters.jsonc -p environmentName="semanticvectorsrc"
```

## Environment Setup

1. Rename .env-sample to .env and fill in the information from the deployed resources

   ```code
    AZURE_SEARCH_SERVICE_ENDPOINT=https://<Your-Search-Service>.search.windows.net
    AZURE_SEARCH_INDEX_NAME=semantic-vector
    AZURE_SEARCH_ADMIN_KEY=<Your-Search-Service-Admin-Key>
    OPENAI_ENDPOINT=https://<Your-Open-AI-Service>.openai.azure.com/
    OPENAI_API_KEY=<Your-Open-AI-Service-Key>
    OPENAI_API_VERSION=2023-05-15
    OPENAI_EMBEDDING_DEPLOYED_MODEL=acs-emb-ada-002
   ```

1. Install the required packages

    ```ps
    pip install -r requirements.txt
    ```

1. Create a virtual environment for the python scripts

    ```ps
    python -m venv acs-env --system-site-packages
    ```

1. Create pip.ini file in the virtual environment folder and add the following content

    ```code
    [global]
    index-url=https://pkgs.dev.azure.com/azure-sdk/public/_packaging/azure-sdk-for-python/pypi/simple/
    ```

1. Activate the virtual environment (Assuming you are running in PowerShell)

    ```ps
    .\acs-env\Scripts\Activate.ps1
    ```

1. Install the azure vector search package in preview

    ```ps
    pip install azure-search-documents==11.4.0a20230509004
    ```

## Search Setup & Vector Data Indexing

1. Run the index creation script

    ```ps
    python .\create-index.py
    ```

1. Run the Get Vector script

    ```ps
    python .\get-vector-data.py
    ```

1. Run the index vector data script

    ```ps
    python .\index-vector-data.py
    ```

## Test Search Features

You can run the scripts to see the results of the vector, hybrid, and semantic search features.

1. Run the search vector script

    ```ps
    python .\search-vector.py
    ```

    Response Output:

    ```code
    Score: 0.8404397
    Title: Azure Service Bus
    Content: Azure Service Bus is a fully managed, enterprise-grade messaging service that enables you to build reliable and scalable applications. It provides features like message queuing, publish-subscribe, and dead-lettering. Service Bus supports various messaging patterns, including point-to-point, broadcast, and request-reply. You can use Service Bus to integrate your applications and services, decouple your system components, and handle asynchronous communication. It also integrates with other Azure services, such as Azure Functions and Azure Logic Apps.
    Category: Integration

    Score: 0.8315571
    Title: Azure SignalR Service
    Content: Azure SignalR Service is a fully managed, real-time messaging service that enables you to build and scale real-time web applications. It provides features like automatic scaling, WebSocket support, and serverless integration. SignalR Service supports various programming languages, such as C#, JavaScript, and Java. You can use Azure SignalR Service to build chat applications, real-time dashboards, and collaborative tools. It also integrates with other Azure services, such as Azure Functions and Azure App Service.
    Category: Web

    Score: 0.82272965
    Title: Azure Queue Storage
    Content: Azure Queue Storage is a fully managed, scalable, and durable message queuing service that enables you to decouple your applications and build asynchronous solutions. It provides features like at-least-once delivery, message time-to-live, and a RESTful API. Queue Storage supports various programming languages, such as C#, Java, and Python. You can use Azure Queue Storage to build distributed applications, offload your databases, and process and store large volumes of messages. It also integrates with other Azure services, such as Azure Functions and Azure Logic Apps.
    Category: Storage

    Score: 0.82028526
    Title: Azure Web PubSub
    Content: Azure Web PubSub is a fully managed, real-time messaging service that enables you to build and scale real-time web applications using WebSockets. It provides features like automatic scaling, custom domains, and serverless integration. Web PubSub supports various programming languages, such as C#, JavaScript, and Java. You can use Azure Web PubSub to build chat applications, real-time dashboards, and collaborative tools. It also integrates with other Azure services, such as Azure Functions and Azure SignalR Service.
    Category: Web
    ```


## Troubleshooting

1. If you run into pip install issues, try the following:

    ```ps
    pip install --upgrade pip
    ```

1. If you run into issues with Open AI dependencies issue MissingDependencyError, try the following after deactivating the virtual environment:

    ```ps
    #Deactivate the virtual environment
    deactivate

    #Install the missing dependencies
    pip install openai [datalib]
    
    #Activate the virtual environment
    .\acs-env\Scripts\Activate.ps1

    #Install the required packages
    pip install -r requirements.txt.
    ```

## Disclaimer

This project is for demonstration purposes only. It is not intended for production use. It is provided without guarantee or support. Use at your own risk.