from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.cost_savings_opportunity_config import CostSavingsOpportunityConfig
from ...models.put_cost_savings_opportunity_config_response_200 import PutCostSavingsOpportunityConfigResponse200
from ...models.put_cost_savings_opportunity_config_response_401 import PutCostSavingsOpportunityConfigResponse401
from ...models.put_cost_savings_opportunity_config_response_403 import PutCostSavingsOpportunityConfigResponse403
from ...models.put_cost_savings_opportunity_config_response_500 import PutCostSavingsOpportunityConfigResponse500
from typing import cast



def _get_kwargs(
    *,
    body: CostSavingsOpportunityConfig,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v3/app-config/cost-savings-opportunity",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PutCostSavingsOpportunityConfigResponse200 | PutCostSavingsOpportunityConfigResponse401 | PutCostSavingsOpportunityConfigResponse403 | PutCostSavingsOpportunityConfigResponse500 | None:
    if response.status_code == 200:
        response_200 = PutCostSavingsOpportunityConfigResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = PutCostSavingsOpportunityConfigResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PutCostSavingsOpportunityConfigResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = PutCostSavingsOpportunityConfigResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PutCostSavingsOpportunityConfigResponse200 | PutCostSavingsOpportunityConfigResponse401 | PutCostSavingsOpportunityConfigResponse403 | PutCostSavingsOpportunityConfigResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CostSavingsOpportunityConfig,

) -> Response[PutCostSavingsOpportunityConfigResponse200 | PutCostSavingsOpportunityConfigResponse401 | PutCostSavingsOpportunityConfigResponse403 | PutCostSavingsOpportunityConfigResponse500]:
    """ Sets the cost savings opportunity config settings

    Args:
        body (CostSavingsOpportunityConfig): CostSavingsOpportunityConfig represents the system
            settings for cost savings opportunities

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutCostSavingsOpportunityConfigResponse200 | PutCostSavingsOpportunityConfigResponse401 | PutCostSavingsOpportunityConfigResponse403 | PutCostSavingsOpportunityConfigResponse500]
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
    body: CostSavingsOpportunityConfig,

) -> PutCostSavingsOpportunityConfigResponse200 | PutCostSavingsOpportunityConfigResponse401 | PutCostSavingsOpportunityConfigResponse403 | PutCostSavingsOpportunityConfigResponse500 | None:
    """ Sets the cost savings opportunity config settings

    Args:
        body (CostSavingsOpportunityConfig): CostSavingsOpportunityConfig represents the system
            settings for cost savings opportunities

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutCostSavingsOpportunityConfigResponse200 | PutCostSavingsOpportunityConfigResponse401 | PutCostSavingsOpportunityConfigResponse403 | PutCostSavingsOpportunityConfigResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CostSavingsOpportunityConfig,

) -> Response[PutCostSavingsOpportunityConfigResponse200 | PutCostSavingsOpportunityConfigResponse401 | PutCostSavingsOpportunityConfigResponse403 | PutCostSavingsOpportunityConfigResponse500]:
    """ Sets the cost savings opportunity config settings

    Args:
        body (CostSavingsOpportunityConfig): CostSavingsOpportunityConfig represents the system
            settings for cost savings opportunities

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutCostSavingsOpportunityConfigResponse200 | PutCostSavingsOpportunityConfigResponse401 | PutCostSavingsOpportunityConfigResponse403 | PutCostSavingsOpportunityConfigResponse500]
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
    body: CostSavingsOpportunityConfig,

) -> PutCostSavingsOpportunityConfigResponse200 | PutCostSavingsOpportunityConfigResponse401 | PutCostSavingsOpportunityConfigResponse403 | PutCostSavingsOpportunityConfigResponse500 | None:
    """ Sets the cost savings opportunity config settings

    Args:
        body (CostSavingsOpportunityConfig): CostSavingsOpportunityConfig represents the system
            settings for cost savings opportunities

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutCostSavingsOpportunityConfigResponse200 | PutCostSavingsOpportunityConfigResponse401 | PutCostSavingsOpportunityConfigResponse403 | PutCostSavingsOpportunityConfigResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
