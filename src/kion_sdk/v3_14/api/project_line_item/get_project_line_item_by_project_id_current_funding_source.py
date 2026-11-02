from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_project_line_item_by_project_id_current_funding_source_response_200 import GetProjectLineItemByProjectIDCurrentFundingSourceResponse200
from ...models.get_project_line_item_by_project_id_current_funding_source_response_400 import GetProjectLineItemByProjectIDCurrentFundingSourceResponse400
from ...models.get_project_line_item_by_project_id_current_funding_source_response_401 import GetProjectLineItemByProjectIDCurrentFundingSourceResponse401
from ...models.get_project_line_item_by_project_id_current_funding_source_response_403 import GetProjectLineItemByProjectIDCurrentFundingSourceResponse403
from ...models.get_project_line_item_by_project_id_current_funding_source_response_404 import GetProjectLineItemByProjectIDCurrentFundingSourceResponse404
from ...models.get_project_line_item_by_project_id_current_funding_source_response_500 import GetProjectLineItemByProjectIDCurrentFundingSourceResponse500
from typing import cast



def _get_kwargs(
    project_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/project/{project_id}/line-item/current-funding-source".format(project_id=quote(str(project_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetProjectLineItemByProjectIDCurrentFundingSourceResponse200 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse400 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse401 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse403 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse404 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse500 | None:
    if response.status_code == 200:
        response_200 = GetProjectLineItemByProjectIDCurrentFundingSourceResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetProjectLineItemByProjectIDCurrentFundingSourceResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetProjectLineItemByProjectIDCurrentFundingSourceResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetProjectLineItemByProjectIDCurrentFundingSourceResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetProjectLineItemByProjectIDCurrentFundingSourceResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetProjectLineItemByProjectIDCurrentFundingSourceResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetProjectLineItemByProjectIDCurrentFundingSourceResponse200 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse400 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse401 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse403 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse404 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetProjectLineItemByProjectIDCurrentFundingSourceResponse200 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse400 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse401 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse403 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse404 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse500]:
    """ Returns a list of project line items by project id for all current funding sources from the
    application.

    Args:
        project_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectLineItemByProjectIDCurrentFundingSourceResponse200 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse400 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse401 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse403 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse404 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse500]
     """


    kwargs = _get_kwargs(
        project_id=project_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id: int,
    *,
    client: AuthenticatedClient,

) -> GetProjectLineItemByProjectIDCurrentFundingSourceResponse200 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse400 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse401 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse403 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse404 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse500 | None:
    """ Returns a list of project line items by project id for all current funding sources from the
    application.

    Args:
        project_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectLineItemByProjectIDCurrentFundingSourceResponse200 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse400 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse401 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse403 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse404 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse500
     """


    return sync_detailed(
        project_id=project_id,
client=client,

    ).parsed

async def asyncio_detailed(
    project_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetProjectLineItemByProjectIDCurrentFundingSourceResponse200 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse400 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse401 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse403 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse404 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse500]:
    """ Returns a list of project line items by project id for all current funding sources from the
    application.

    Args:
        project_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectLineItemByProjectIDCurrentFundingSourceResponse200 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse400 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse401 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse403 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse404 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse500]
     """


    kwargs = _get_kwargs(
        project_id=project_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id: int,
    *,
    client: AuthenticatedClient,

) -> GetProjectLineItemByProjectIDCurrentFundingSourceResponse200 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse400 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse401 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse403 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse404 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse500 | None:
    """ Returns a list of project line items by project id for all current funding sources from the
    application.

    Args:
        project_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectLineItemByProjectIDCurrentFundingSourceResponse200 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse400 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse401 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse403 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse404 | GetProjectLineItemByProjectIDCurrentFundingSourceResponse500
     """


    return (await asyncio_detailed(
        project_id=project_id,
client=client,

    )).parsed
