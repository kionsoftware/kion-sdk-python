from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_cost_savings_opportunity_config_response_200 import GetCostSavingsOpportunityConfigResponse200
from ...models.get_cost_savings_opportunity_config_response_401 import GetCostSavingsOpportunityConfigResponse401
from ...models.get_cost_savings_opportunity_config_response_403 import GetCostSavingsOpportunityConfigResponse403
from ...models.get_cost_savings_opportunity_config_response_500 import GetCostSavingsOpportunityConfigResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/app-config/cost-savings-opportunity",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetCostSavingsOpportunityConfigResponse200 | GetCostSavingsOpportunityConfigResponse401 | GetCostSavingsOpportunityConfigResponse403 | GetCostSavingsOpportunityConfigResponse500 | None:
    if response.status_code == 200:
        response_200 = GetCostSavingsOpportunityConfigResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetCostSavingsOpportunityConfigResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetCostSavingsOpportunityConfigResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetCostSavingsOpportunityConfigResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetCostSavingsOpportunityConfigResponse200 | GetCostSavingsOpportunityConfigResponse401 | GetCostSavingsOpportunityConfigResponse403 | GetCostSavingsOpportunityConfigResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetCostSavingsOpportunityConfigResponse200 | GetCostSavingsOpportunityConfigResponse401 | GetCostSavingsOpportunityConfigResponse403 | GetCostSavingsOpportunityConfigResponse500]:
    """ Gets the cost savings opportunity config settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCostSavingsOpportunityConfigResponse200 | GetCostSavingsOpportunityConfigResponse401 | GetCostSavingsOpportunityConfigResponse403 | GetCostSavingsOpportunityConfigResponse500]
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

) -> GetCostSavingsOpportunityConfigResponse200 | GetCostSavingsOpportunityConfigResponse401 | GetCostSavingsOpportunityConfigResponse403 | GetCostSavingsOpportunityConfigResponse500 | None:
    """ Gets the cost savings opportunity config settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCostSavingsOpportunityConfigResponse200 | GetCostSavingsOpportunityConfigResponse401 | GetCostSavingsOpportunityConfigResponse403 | GetCostSavingsOpportunityConfigResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetCostSavingsOpportunityConfigResponse200 | GetCostSavingsOpportunityConfigResponse401 | GetCostSavingsOpportunityConfigResponse403 | GetCostSavingsOpportunityConfigResponse500]:
    """ Gets the cost savings opportunity config settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCostSavingsOpportunityConfigResponse200 | GetCostSavingsOpportunityConfigResponse401 | GetCostSavingsOpportunityConfigResponse403 | GetCostSavingsOpportunityConfigResponse500]
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

) -> GetCostSavingsOpportunityConfigResponse200 | GetCostSavingsOpportunityConfigResponse401 | GetCostSavingsOpportunityConfigResponse403 | GetCostSavingsOpportunityConfigResponse500 | None:
    """ Gets the cost savings opportunity config settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCostSavingsOpportunityConfigResponse200 | GetCostSavingsOpportunityConfigResponse401 | GetCostSavingsOpportunityConfigResponse403 | GetCostSavingsOpportunityConfigResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
