from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_service_catalog_portfolio_response_201 import PostServiceCatalogPortfolioResponse201
from ...models.post_service_catalog_portfolio_response_400 import PostServiceCatalogPortfolioResponse400
from ...models.post_service_catalog_portfolio_response_401 import PostServiceCatalogPortfolioResponse401
from ...models.post_service_catalog_portfolio_response_403 import PostServiceCatalogPortfolioResponse403
from ...models.post_service_catalog_portfolio_response_422 import PostServiceCatalogPortfolioResponse422
from ...models.post_service_catalog_portfolio_response_500 import PostServiceCatalogPortfolioResponse500
from ...models.service_catalog_portfolio_create import ServiceCatalogPortfolioCreate
from typing import cast



def _get_kwargs(
    *,
    body: ServiceCatalogPortfolioCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/service-catalog",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostServiceCatalogPortfolioResponse201 | PostServiceCatalogPortfolioResponse400 | PostServiceCatalogPortfolioResponse401 | PostServiceCatalogPortfolioResponse403 | PostServiceCatalogPortfolioResponse422 | PostServiceCatalogPortfolioResponse500 | None:
    if response.status_code == 201:
        response_201 = PostServiceCatalogPortfolioResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostServiceCatalogPortfolioResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostServiceCatalogPortfolioResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostServiceCatalogPortfolioResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostServiceCatalogPortfolioResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostServiceCatalogPortfolioResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostServiceCatalogPortfolioResponse201 | PostServiceCatalogPortfolioResponse400 | PostServiceCatalogPortfolioResponse401 | PostServiceCatalogPortfolioResponse403 | PostServiceCatalogPortfolioResponse422 | PostServiceCatalogPortfolioResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ServiceCatalogPortfolioCreate,

) -> Response[PostServiceCatalogPortfolioResponse201 | PostServiceCatalogPortfolioResponse400 | PostServiceCatalogPortfolioResponse401 | PostServiceCatalogPortfolioResponse403 | PostServiceCatalogPortfolioResponse422 | PostServiceCatalogPortfolioResponse500]:
    """ Registers an Service Catalog portfolio with the application.

     Portfolios exist in AWS accounts that are attached to a project.

    Args:
        body (ServiceCatalogPortfolioCreate): ServiceCatalogPortfolioCreate defines a Service
            Catalog portfolio creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServiceCatalogPortfolioResponse201 | PostServiceCatalogPortfolioResponse400 | PostServiceCatalogPortfolioResponse401 | PostServiceCatalogPortfolioResponse403 | PostServiceCatalogPortfolioResponse422 | PostServiceCatalogPortfolioResponse500]
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
    body: ServiceCatalogPortfolioCreate,

) -> PostServiceCatalogPortfolioResponse201 | PostServiceCatalogPortfolioResponse400 | PostServiceCatalogPortfolioResponse401 | PostServiceCatalogPortfolioResponse403 | PostServiceCatalogPortfolioResponse422 | PostServiceCatalogPortfolioResponse500 | None:
    """ Registers an Service Catalog portfolio with the application.

     Portfolios exist in AWS accounts that are attached to a project.

    Args:
        body (ServiceCatalogPortfolioCreate): ServiceCatalogPortfolioCreate defines a Service
            Catalog portfolio creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServiceCatalogPortfolioResponse201 | PostServiceCatalogPortfolioResponse400 | PostServiceCatalogPortfolioResponse401 | PostServiceCatalogPortfolioResponse403 | PostServiceCatalogPortfolioResponse422 | PostServiceCatalogPortfolioResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ServiceCatalogPortfolioCreate,

) -> Response[PostServiceCatalogPortfolioResponse201 | PostServiceCatalogPortfolioResponse400 | PostServiceCatalogPortfolioResponse401 | PostServiceCatalogPortfolioResponse403 | PostServiceCatalogPortfolioResponse422 | PostServiceCatalogPortfolioResponse500]:
    """ Registers an Service Catalog portfolio with the application.

     Portfolios exist in AWS accounts that are attached to a project.

    Args:
        body (ServiceCatalogPortfolioCreate): ServiceCatalogPortfolioCreate defines a Service
            Catalog portfolio creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServiceCatalogPortfolioResponse201 | PostServiceCatalogPortfolioResponse400 | PostServiceCatalogPortfolioResponse401 | PostServiceCatalogPortfolioResponse403 | PostServiceCatalogPortfolioResponse422 | PostServiceCatalogPortfolioResponse500]
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
    body: ServiceCatalogPortfolioCreate,

) -> PostServiceCatalogPortfolioResponse201 | PostServiceCatalogPortfolioResponse400 | PostServiceCatalogPortfolioResponse401 | PostServiceCatalogPortfolioResponse403 | PostServiceCatalogPortfolioResponse422 | PostServiceCatalogPortfolioResponse500 | None:
    """ Registers an Service Catalog portfolio with the application.

     Portfolios exist in AWS accounts that are attached to a project.

    Args:
        body (ServiceCatalogPortfolioCreate): ServiceCatalogPortfolioCreate defines a Service
            Catalog portfolio creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServiceCatalogPortfolioResponse201 | PostServiceCatalogPortfolioResponse400 | PostServiceCatalogPortfolioResponse401 | PostServiceCatalogPortfolioResponse403 | PostServiceCatalogPortfolioResponse422 | PostServiceCatalogPortfolioResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
