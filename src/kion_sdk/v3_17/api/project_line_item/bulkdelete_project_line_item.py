from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bulkdelete_project_line_item_response_200 import BulkdeleteProjectLineItemResponse200
from ...models.bulkdelete_project_line_item_response_400 import BulkdeleteProjectLineItemResponse400
from ...models.bulkdelete_project_line_item_response_401 import BulkdeleteProjectLineItemResponse401
from ...models.bulkdelete_project_line_item_response_403 import BulkdeleteProjectLineItemResponse403
from ...models.bulkdelete_project_line_item_response_422 import BulkdeleteProjectLineItemResponse422
from ...models.bulkdelete_project_line_item_response_500 import BulkdeleteProjectLineItemResponse500
from ...models.project_line_item_create import ProjectLineItemCreate
from typing import cast



def _get_kwargs(
    *,
    body: list[ProjectLineItemCreate],

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/project-line-item/bulk-delete",
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)



    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BulkdeleteProjectLineItemResponse200 | BulkdeleteProjectLineItemResponse400 | BulkdeleteProjectLineItemResponse401 | BulkdeleteProjectLineItemResponse403 | BulkdeleteProjectLineItemResponse422 | BulkdeleteProjectLineItemResponse500 | None:
    if response.status_code == 200:
        response_200 = BulkdeleteProjectLineItemResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = BulkdeleteProjectLineItemResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = BulkdeleteProjectLineItemResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = BulkdeleteProjectLineItemResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = BulkdeleteProjectLineItemResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = BulkdeleteProjectLineItemResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BulkdeleteProjectLineItemResponse200 | BulkdeleteProjectLineItemResponse400 | BulkdeleteProjectLineItemResponse401 | BulkdeleteProjectLineItemResponse403 | BulkdeleteProjectLineItemResponse422 | BulkdeleteProjectLineItemResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: list[ProjectLineItemCreate],

) -> Response[BulkdeleteProjectLineItemResponse200 | BulkdeleteProjectLineItemResponse400 | BulkdeleteProjectLineItemResponse401 | BulkdeleteProjectLineItemResponse403 | BulkdeleteProjectLineItemResponse422 | BulkdeleteProjectLineItemResponse500]:
    """ Deletes list of project line items in the application.

    Args:
        body (list[ProjectLineItemCreate]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkdeleteProjectLineItemResponse200 | BulkdeleteProjectLineItemResponse400 | BulkdeleteProjectLineItemResponse401 | BulkdeleteProjectLineItemResponse403 | BulkdeleteProjectLineItemResponse422 | BulkdeleteProjectLineItemResponse500]
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
    body: list[ProjectLineItemCreate],

) -> BulkdeleteProjectLineItemResponse200 | BulkdeleteProjectLineItemResponse400 | BulkdeleteProjectLineItemResponse401 | BulkdeleteProjectLineItemResponse403 | BulkdeleteProjectLineItemResponse422 | BulkdeleteProjectLineItemResponse500 | None:
    """ Deletes list of project line items in the application.

    Args:
        body (list[ProjectLineItemCreate]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkdeleteProjectLineItemResponse200 | BulkdeleteProjectLineItemResponse400 | BulkdeleteProjectLineItemResponse401 | BulkdeleteProjectLineItemResponse403 | BulkdeleteProjectLineItemResponse422 | BulkdeleteProjectLineItemResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: list[ProjectLineItemCreate],

) -> Response[BulkdeleteProjectLineItemResponse200 | BulkdeleteProjectLineItemResponse400 | BulkdeleteProjectLineItemResponse401 | BulkdeleteProjectLineItemResponse403 | BulkdeleteProjectLineItemResponse422 | BulkdeleteProjectLineItemResponse500]:
    """ Deletes list of project line items in the application.

    Args:
        body (list[ProjectLineItemCreate]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkdeleteProjectLineItemResponse200 | BulkdeleteProjectLineItemResponse400 | BulkdeleteProjectLineItemResponse401 | BulkdeleteProjectLineItemResponse403 | BulkdeleteProjectLineItemResponse422 | BulkdeleteProjectLineItemResponse500]
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
    body: list[ProjectLineItemCreate],

) -> BulkdeleteProjectLineItemResponse200 | BulkdeleteProjectLineItemResponse400 | BulkdeleteProjectLineItemResponse401 | BulkdeleteProjectLineItemResponse403 | BulkdeleteProjectLineItemResponse422 | BulkdeleteProjectLineItemResponse500 | None:
    """ Deletes list of project line items in the application.

    Args:
        body (list[ProjectLineItemCreate]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkdeleteProjectLineItemResponse200 | BulkdeleteProjectLineItemResponse400 | BulkdeleteProjectLineItemResponse401 | BulkdeleteProjectLineItemResponse403 | BulkdeleteProjectLineItemResponse422 | BulkdeleteProjectLineItemResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
