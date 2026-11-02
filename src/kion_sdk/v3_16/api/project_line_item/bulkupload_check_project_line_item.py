from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bulkupload_check_project_line_item_body import BulkuploadCheckProjectLineItemBody
from ...models.bulkupload_check_project_line_item_response_200 import BulkuploadCheckProjectLineItemResponse200
from ...models.bulkupload_check_project_line_item_response_400 import BulkuploadCheckProjectLineItemResponse400
from ...models.bulkupload_check_project_line_item_response_401 import BulkuploadCheckProjectLineItemResponse401
from ...models.bulkupload_check_project_line_item_response_403 import BulkuploadCheckProjectLineItemResponse403
from ...models.bulkupload_check_project_line_item_response_404 import BulkuploadCheckProjectLineItemResponse404
from ...models.bulkupload_check_project_line_item_response_500 import BulkuploadCheckProjectLineItemResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    payer_id: int,
    *,
    body: BulkuploadCheckProjectLineItemBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/project-line-item/bulk-upload-check/{payer_id}".format(payer_id=quote(str(payer_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BulkuploadCheckProjectLineItemResponse200 | BulkuploadCheckProjectLineItemResponse400 | BulkuploadCheckProjectLineItemResponse401 | BulkuploadCheckProjectLineItemResponse403 | BulkuploadCheckProjectLineItemResponse404 | BulkuploadCheckProjectLineItemResponse500 | None:
    if response.status_code == 200:
        response_200 = BulkuploadCheckProjectLineItemResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = BulkuploadCheckProjectLineItemResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = BulkuploadCheckProjectLineItemResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = BulkuploadCheckProjectLineItemResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = BulkuploadCheckProjectLineItemResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = BulkuploadCheckProjectLineItemResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BulkuploadCheckProjectLineItemResponse200 | BulkuploadCheckProjectLineItemResponse400 | BulkuploadCheckProjectLineItemResponse401 | BulkuploadCheckProjectLineItemResponse403 | BulkuploadCheckProjectLineItemResponse404 | BulkuploadCheckProjectLineItemResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    payer_id: int,
    *,
    client: AuthenticatedClient,
    body: BulkuploadCheckProjectLineItemBody | Unset = UNSET,

) -> Response[BulkuploadCheckProjectLineItemResponse200 | BulkuploadCheckProjectLineItemResponse400 | BulkuploadCheckProjectLineItemResponse401 | BulkuploadCheckProjectLineItemResponse403 | BulkuploadCheckProjectLineItemResponse404 | BulkuploadCheckProjectLineItemResponse500]:
    """ Does csv check for bulk upload with project line items into the application.

    Args:
        payer_id (int):
        body (BulkuploadCheckProjectLineItemBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkuploadCheckProjectLineItemResponse200 | BulkuploadCheckProjectLineItemResponse400 | BulkuploadCheckProjectLineItemResponse401 | BulkuploadCheckProjectLineItemResponse403 | BulkuploadCheckProjectLineItemResponse404 | BulkuploadCheckProjectLineItemResponse500]
     """


    kwargs = _get_kwargs(
        payer_id=payer_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    payer_id: int,
    *,
    client: AuthenticatedClient,
    body: BulkuploadCheckProjectLineItemBody | Unset = UNSET,

) -> BulkuploadCheckProjectLineItemResponse200 | BulkuploadCheckProjectLineItemResponse400 | BulkuploadCheckProjectLineItemResponse401 | BulkuploadCheckProjectLineItemResponse403 | BulkuploadCheckProjectLineItemResponse404 | BulkuploadCheckProjectLineItemResponse500 | None:
    """ Does csv check for bulk upload with project line items into the application.

    Args:
        payer_id (int):
        body (BulkuploadCheckProjectLineItemBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkuploadCheckProjectLineItemResponse200 | BulkuploadCheckProjectLineItemResponse400 | BulkuploadCheckProjectLineItemResponse401 | BulkuploadCheckProjectLineItemResponse403 | BulkuploadCheckProjectLineItemResponse404 | BulkuploadCheckProjectLineItemResponse500
     """


    return sync_detailed(
        payer_id=payer_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    payer_id: int,
    *,
    client: AuthenticatedClient,
    body: BulkuploadCheckProjectLineItemBody | Unset = UNSET,

) -> Response[BulkuploadCheckProjectLineItemResponse200 | BulkuploadCheckProjectLineItemResponse400 | BulkuploadCheckProjectLineItemResponse401 | BulkuploadCheckProjectLineItemResponse403 | BulkuploadCheckProjectLineItemResponse404 | BulkuploadCheckProjectLineItemResponse500]:
    """ Does csv check for bulk upload with project line items into the application.

    Args:
        payer_id (int):
        body (BulkuploadCheckProjectLineItemBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkuploadCheckProjectLineItemResponse200 | BulkuploadCheckProjectLineItemResponse400 | BulkuploadCheckProjectLineItemResponse401 | BulkuploadCheckProjectLineItemResponse403 | BulkuploadCheckProjectLineItemResponse404 | BulkuploadCheckProjectLineItemResponse500]
     """


    kwargs = _get_kwargs(
        payer_id=payer_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    payer_id: int,
    *,
    client: AuthenticatedClient,
    body: BulkuploadCheckProjectLineItemBody | Unset = UNSET,

) -> BulkuploadCheckProjectLineItemResponse200 | BulkuploadCheckProjectLineItemResponse400 | BulkuploadCheckProjectLineItemResponse401 | BulkuploadCheckProjectLineItemResponse403 | BulkuploadCheckProjectLineItemResponse404 | BulkuploadCheckProjectLineItemResponse500 | None:
    """ Does csv check for bulk upload with project line items into the application.

    Args:
        payer_id (int):
        body (BulkuploadCheckProjectLineItemBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkuploadCheckProjectLineItemResponse200 | BulkuploadCheckProjectLineItemResponse400 | BulkuploadCheckProjectLineItemResponse401 | BulkuploadCheckProjectLineItemResponse403 | BulkuploadCheckProjectLineItemResponse404 | BulkuploadCheckProjectLineItemResponse500
     """


    return (await asyncio_detailed(
        payer_id=payer_id,
client=client,
body=body,

    )).parsed
