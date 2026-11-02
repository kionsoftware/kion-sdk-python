from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.azure_create_new_subscription import AzureCreateNewSubscription
from ...models.create_new_subscription_response_201 import CreateNewSubscriptionResponse201
from ...models.create_new_subscription_response_400 import CreateNewSubscriptionResponse400
from ...models.create_new_subscription_response_401 import CreateNewSubscriptionResponse401
from ...models.create_new_subscription_response_403 import CreateNewSubscriptionResponse403
from ...models.create_new_subscription_response_500 import CreateNewSubscriptionResponse500
from typing import cast



def _get_kwargs(
    *,
    body: AzureCreateNewSubscription,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/azure/subscription",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateNewSubscriptionResponse201 | CreateNewSubscriptionResponse400 | CreateNewSubscriptionResponse401 | CreateNewSubscriptionResponse403 | CreateNewSubscriptionResponse500 | None:
    if response.status_code == 201:
        response_201 = CreateNewSubscriptionResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = CreateNewSubscriptionResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = CreateNewSubscriptionResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = CreateNewSubscriptionResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = CreateNewSubscriptionResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateNewSubscriptionResponse201 | CreateNewSubscriptionResponse400 | CreateNewSubscriptionResponse401 | CreateNewSubscriptionResponse403 | CreateNewSubscriptionResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AzureCreateNewSubscription,

) -> Response[CreateNewSubscriptionResponse201 | CreateNewSubscriptionResponse400 | CreateNewSubscriptionResponse401 | CreateNewSubscriptionResponse403 | CreateNewSubscriptionResponse500]:
    """ Creates an Azure Subscription.

     Returns id of the account of the subscription that was created.
    This is deprecated but retained for backwards compatibility.
    Use POST /v3/account-cache/create?account-type=azure instead.

    Args:
        body (AzureCreateNewSubscription): AzureCreateNewSubscription defines a new subscription
            to create in azure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateNewSubscriptionResponse201 | CreateNewSubscriptionResponse400 | CreateNewSubscriptionResponse401 | CreateNewSubscriptionResponse403 | CreateNewSubscriptionResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: AzureCreateNewSubscription,

) -> CreateNewSubscriptionResponse201 | CreateNewSubscriptionResponse400 | CreateNewSubscriptionResponse401 | CreateNewSubscriptionResponse403 | CreateNewSubscriptionResponse500 | None:
    """ Creates an Azure Subscription.

     Returns id of the account of the subscription that was created.
    This is deprecated but retained for backwards compatibility.
    Use POST /v3/account-cache/create?account-type=azure instead.

    Args:
        body (AzureCreateNewSubscription): AzureCreateNewSubscription defines a new subscription
            to create in azure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateNewSubscriptionResponse201 | CreateNewSubscriptionResponse400 | CreateNewSubscriptionResponse401 | CreateNewSubscriptionResponse403 | CreateNewSubscriptionResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AzureCreateNewSubscription,

) -> Response[CreateNewSubscriptionResponse201 | CreateNewSubscriptionResponse400 | CreateNewSubscriptionResponse401 | CreateNewSubscriptionResponse403 | CreateNewSubscriptionResponse500]:
    """ Creates an Azure Subscription.

     Returns id of the account of the subscription that was created.
    This is deprecated but retained for backwards compatibility.
    Use POST /v3/account-cache/create?account-type=azure instead.

    Args:
        body (AzureCreateNewSubscription): AzureCreateNewSubscription defines a new subscription
            to create in azure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateNewSubscriptionResponse201 | CreateNewSubscriptionResponse400 | CreateNewSubscriptionResponse401 | CreateNewSubscriptionResponse403 | CreateNewSubscriptionResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AzureCreateNewSubscription,

) -> CreateNewSubscriptionResponse201 | CreateNewSubscriptionResponse400 | CreateNewSubscriptionResponse401 | CreateNewSubscriptionResponse403 | CreateNewSubscriptionResponse500 | None:
    """ Creates an Azure Subscription.

     Returns id of the account of the subscription that was created.
    This is deprecated but retained for backwards compatibility.
    Use POST /v3/account-cache/create?account-type=azure instead.

    Args:
        body (AzureCreateNewSubscription): AzureCreateNewSubscription defines a new subscription
            to create in azure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateNewSubscriptionResponse201 | CreateNewSubscriptionResponse400 | CreateNewSubscriptionResponse401 | CreateNewSubscriptionResponse403 | CreateNewSubscriptionResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
