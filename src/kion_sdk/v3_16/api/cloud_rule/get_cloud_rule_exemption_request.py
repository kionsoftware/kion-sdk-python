from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_cloud_rule_exemption_request_response_200 import GetCloudRuleExemptionRequestResponse200
from ...models.get_cloud_rule_exemption_request_response_400 import GetCloudRuleExemptionRequestResponse400
from ...models.get_cloud_rule_exemption_request_response_401 import GetCloudRuleExemptionRequestResponse401
from ...models.get_cloud_rule_exemption_request_response_500 import GetCloudRuleExemptionRequestResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/cloud-rule/exemption-request",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetCloudRuleExemptionRequestResponse200 | GetCloudRuleExemptionRequestResponse400 | GetCloudRuleExemptionRequestResponse401 | GetCloudRuleExemptionRequestResponse500 | None:
    if response.status_code == 200:
        response_200 = GetCloudRuleExemptionRequestResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetCloudRuleExemptionRequestResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetCloudRuleExemptionRequestResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = GetCloudRuleExemptionRequestResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetCloudRuleExemptionRequestResponse200 | GetCloudRuleExemptionRequestResponse400 | GetCloudRuleExemptionRequestResponse401 | GetCloudRuleExemptionRequestResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetCloudRuleExemptionRequestResponse200 | GetCloudRuleExemptionRequestResponse400 | GetCloudRuleExemptionRequestResponse401 | GetCloudRuleExemptionRequestResponse500]:
    """ Returns list of pending cloud rule exemption requests.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCloudRuleExemptionRequestResponse200 | GetCloudRuleExemptionRequestResponse400 | GetCloudRuleExemptionRequestResponse401 | GetCloudRuleExemptionRequestResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> GetCloudRuleExemptionRequestResponse200 | GetCloudRuleExemptionRequestResponse400 | GetCloudRuleExemptionRequestResponse401 | GetCloudRuleExemptionRequestResponse500 | None:
    """ Returns list of pending cloud rule exemption requests.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCloudRuleExemptionRequestResponse200 | GetCloudRuleExemptionRequestResponse400 | GetCloudRuleExemptionRequestResponse401 | GetCloudRuleExemptionRequestResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetCloudRuleExemptionRequestResponse200 | GetCloudRuleExemptionRequestResponse400 | GetCloudRuleExemptionRequestResponse401 | GetCloudRuleExemptionRequestResponse500]:
    """ Returns list of pending cloud rule exemption requests.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCloudRuleExemptionRequestResponse200 | GetCloudRuleExemptionRequestResponse400 | GetCloudRuleExemptionRequestResponse401 | GetCloudRuleExemptionRequestResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> GetCloudRuleExemptionRequestResponse200 | GetCloudRuleExemptionRequestResponse400 | GetCloudRuleExemptionRequestResponse401 | GetCloudRuleExemptionRequestResponse500 | None:
    """ Returns list of pending cloud rule exemption requests.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCloudRuleExemptionRequestResponse200 | GetCloudRuleExemptionRequestResponse400 | GetCloudRuleExemptionRequestResponse401 | GetCloudRuleExemptionRequestResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
