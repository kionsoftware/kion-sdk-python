from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_cloud_pulse_account_data_response_200 import GetCloudPulseAccountDataResponse200
from ...models.get_cloud_pulse_account_data_response_400 import GetCloudPulseAccountDataResponse400
from ...models.get_cloud_pulse_account_data_response_401 import GetCloudPulseAccountDataResponse401
from ...models.get_cloud_pulse_account_data_response_403 import GetCloudPulseAccountDataResponse403
from ...models.get_cloud_pulse_account_data_response_500 import GetCloudPulseAccountDataResponse500
from ...models.get_cloud_pulse_account_data_status import GetCloudPulseAccountDataStatus
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'alphabetical',
    sort_order: str | Unset = 'ASC',
    status: GetCloudPulseAccountDataStatus | Unset = UNSET,
    account_ids: str | Unset = UNSET,
    account_ids_exclusive: bool | Unset = UNSET,
    cft_ids: str | Unset = UNSET,
    cft_ids_exclusive: bool | Unset = UNSET,
    cloud_rule_ids: str | Unset = UNSET,
    cloud_rule_ids_exclusive: bool | Unset = UNSET,
    project_ids: str | Unset = UNSET,
    project_ids_exclusive: bool | Unset = UNSET,
    ou_ids: str | Unset = UNSET,
    ou_ids_exclusive: bool | Unset = UNSET,
    ou_direct_descendants_only: bool | Unset = UNSET,
    keyword: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["count"] = count

    params["sort_method"] = sort_method

    params["sort_order"] = sort_order

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["account_ids"] = account_ids

    params["account_ids_exclusive"] = account_ids_exclusive

    params["cft_ids"] = cft_ids

    params["cft_ids_exclusive"] = cft_ids_exclusive

    params["cloud_rule_ids"] = cloud_rule_ids

    params["cloud_rule_ids_exclusive"] = cloud_rule_ids_exclusive

    params["project_ids"] = project_ids

    params["project_ids_exclusive"] = project_ids_exclusive

    params["ou_ids"] = ou_ids

    params["ou_ids_exclusive"] = ou_ids_exclusive

    params["ou_direct_descendants_only"] = ou_direct_descendants_only

    params["keyword"] = keyword


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/cloud-pulse/account-data",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetCloudPulseAccountDataResponse200 | GetCloudPulseAccountDataResponse400 | GetCloudPulseAccountDataResponse401 | GetCloudPulseAccountDataResponse403 | GetCloudPulseAccountDataResponse500 | None:
    if response.status_code == 200:
        response_200 = GetCloudPulseAccountDataResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetCloudPulseAccountDataResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetCloudPulseAccountDataResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetCloudPulseAccountDataResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetCloudPulseAccountDataResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetCloudPulseAccountDataResponse200 | GetCloudPulseAccountDataResponse400 | GetCloudPulseAccountDataResponse401 | GetCloudPulseAccountDataResponse403 | GetCloudPulseAccountDataResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'alphabetical',
    sort_order: str | Unset = 'ASC',
    status: GetCloudPulseAccountDataStatus | Unset = UNSET,
    account_ids: str | Unset = UNSET,
    account_ids_exclusive: bool | Unset = UNSET,
    cft_ids: str | Unset = UNSET,
    cft_ids_exclusive: bool | Unset = UNSET,
    cloud_rule_ids: str | Unset = UNSET,
    cloud_rule_ids_exclusive: bool | Unset = UNSET,
    project_ids: str | Unset = UNSET,
    project_ids_exclusive: bool | Unset = UNSET,
    ou_ids: str | Unset = UNSET,
    ou_ids_exclusive: bool | Unset = UNSET,
    ou_direct_descendants_only: bool | Unset = UNSET,
    keyword: str | Unset = UNSET,

) -> Response[GetCloudPulseAccountDataResponse200 | GetCloudPulseAccountDataResponse400 | GetCloudPulseAccountDataResponse401 | GetCloudPulseAccountDataResponse403 | GetCloudPulseAccountDataResponse500]:
    """ Returns account data related to CloudFormation templates in the application.

    Args:
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        sort_method (str | Unset):  Default: 'alphabetical'.
        sort_order (str | Unset):  Default: 'ASC'.
        status (GetCloudPulseAccountDataStatus | Unset):
        account_ids (str | Unset):
        account_ids_exclusive (bool | Unset):
        cft_ids (str | Unset):
        cft_ids_exclusive (bool | Unset):
        cloud_rule_ids (str | Unset):
        cloud_rule_ids_exclusive (bool | Unset):
        project_ids (str | Unset):
        project_ids_exclusive (bool | Unset):
        ou_ids (str | Unset):
        ou_ids_exclusive (bool | Unset):
        ou_direct_descendants_only (bool | Unset):
        keyword (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCloudPulseAccountDataResponse200 | GetCloudPulseAccountDataResponse400 | GetCloudPulseAccountDataResponse401 | GetCloudPulseAccountDataResponse403 | GetCloudPulseAccountDataResponse500]
     """


    kwargs = _get_kwargs(
        page=page,
count=count,
sort_method=sort_method,
sort_order=sort_order,
status=status,
account_ids=account_ids,
account_ids_exclusive=account_ids_exclusive,
cft_ids=cft_ids,
cft_ids_exclusive=cft_ids_exclusive,
cloud_rule_ids=cloud_rule_ids,
cloud_rule_ids_exclusive=cloud_rule_ids_exclusive,
project_ids=project_ids,
project_ids_exclusive=project_ids_exclusive,
ou_ids=ou_ids,
ou_ids_exclusive=ou_ids_exclusive,
ou_direct_descendants_only=ou_direct_descendants_only,
keyword=keyword,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'alphabetical',
    sort_order: str | Unset = 'ASC',
    status: GetCloudPulseAccountDataStatus | Unset = UNSET,
    account_ids: str | Unset = UNSET,
    account_ids_exclusive: bool | Unset = UNSET,
    cft_ids: str | Unset = UNSET,
    cft_ids_exclusive: bool | Unset = UNSET,
    cloud_rule_ids: str | Unset = UNSET,
    cloud_rule_ids_exclusive: bool | Unset = UNSET,
    project_ids: str | Unset = UNSET,
    project_ids_exclusive: bool | Unset = UNSET,
    ou_ids: str | Unset = UNSET,
    ou_ids_exclusive: bool | Unset = UNSET,
    ou_direct_descendants_only: bool | Unset = UNSET,
    keyword: str | Unset = UNSET,

) -> GetCloudPulseAccountDataResponse200 | GetCloudPulseAccountDataResponse400 | GetCloudPulseAccountDataResponse401 | GetCloudPulseAccountDataResponse403 | GetCloudPulseAccountDataResponse500 | None:
    """ Returns account data related to CloudFormation templates in the application.

    Args:
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        sort_method (str | Unset):  Default: 'alphabetical'.
        sort_order (str | Unset):  Default: 'ASC'.
        status (GetCloudPulseAccountDataStatus | Unset):
        account_ids (str | Unset):
        account_ids_exclusive (bool | Unset):
        cft_ids (str | Unset):
        cft_ids_exclusive (bool | Unset):
        cloud_rule_ids (str | Unset):
        cloud_rule_ids_exclusive (bool | Unset):
        project_ids (str | Unset):
        project_ids_exclusive (bool | Unset):
        ou_ids (str | Unset):
        ou_ids_exclusive (bool | Unset):
        ou_direct_descendants_only (bool | Unset):
        keyword (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCloudPulseAccountDataResponse200 | GetCloudPulseAccountDataResponse400 | GetCloudPulseAccountDataResponse401 | GetCloudPulseAccountDataResponse403 | GetCloudPulseAccountDataResponse500
     """


    return sync_detailed(
        client=client,
page=page,
count=count,
sort_method=sort_method,
sort_order=sort_order,
status=status,
account_ids=account_ids,
account_ids_exclusive=account_ids_exclusive,
cft_ids=cft_ids,
cft_ids_exclusive=cft_ids_exclusive,
cloud_rule_ids=cloud_rule_ids,
cloud_rule_ids_exclusive=cloud_rule_ids_exclusive,
project_ids=project_ids,
project_ids_exclusive=project_ids_exclusive,
ou_ids=ou_ids,
ou_ids_exclusive=ou_ids_exclusive,
ou_direct_descendants_only=ou_direct_descendants_only,
keyword=keyword,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'alphabetical',
    sort_order: str | Unset = 'ASC',
    status: GetCloudPulseAccountDataStatus | Unset = UNSET,
    account_ids: str | Unset = UNSET,
    account_ids_exclusive: bool | Unset = UNSET,
    cft_ids: str | Unset = UNSET,
    cft_ids_exclusive: bool | Unset = UNSET,
    cloud_rule_ids: str | Unset = UNSET,
    cloud_rule_ids_exclusive: bool | Unset = UNSET,
    project_ids: str | Unset = UNSET,
    project_ids_exclusive: bool | Unset = UNSET,
    ou_ids: str | Unset = UNSET,
    ou_ids_exclusive: bool | Unset = UNSET,
    ou_direct_descendants_only: bool | Unset = UNSET,
    keyword: str | Unset = UNSET,

) -> Response[GetCloudPulseAccountDataResponse200 | GetCloudPulseAccountDataResponse400 | GetCloudPulseAccountDataResponse401 | GetCloudPulseAccountDataResponse403 | GetCloudPulseAccountDataResponse500]:
    """ Returns account data related to CloudFormation templates in the application.

    Args:
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        sort_method (str | Unset):  Default: 'alphabetical'.
        sort_order (str | Unset):  Default: 'ASC'.
        status (GetCloudPulseAccountDataStatus | Unset):
        account_ids (str | Unset):
        account_ids_exclusive (bool | Unset):
        cft_ids (str | Unset):
        cft_ids_exclusive (bool | Unset):
        cloud_rule_ids (str | Unset):
        cloud_rule_ids_exclusive (bool | Unset):
        project_ids (str | Unset):
        project_ids_exclusive (bool | Unset):
        ou_ids (str | Unset):
        ou_ids_exclusive (bool | Unset):
        ou_direct_descendants_only (bool | Unset):
        keyword (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCloudPulseAccountDataResponse200 | GetCloudPulseAccountDataResponse400 | GetCloudPulseAccountDataResponse401 | GetCloudPulseAccountDataResponse403 | GetCloudPulseAccountDataResponse500]
     """


    kwargs = _get_kwargs(
        page=page,
count=count,
sort_method=sort_method,
sort_order=sort_order,
status=status,
account_ids=account_ids,
account_ids_exclusive=account_ids_exclusive,
cft_ids=cft_ids,
cft_ids_exclusive=cft_ids_exclusive,
cloud_rule_ids=cloud_rule_ids,
cloud_rule_ids_exclusive=cloud_rule_ids_exclusive,
project_ids=project_ids,
project_ids_exclusive=project_ids_exclusive,
ou_ids=ou_ids,
ou_ids_exclusive=ou_ids_exclusive,
ou_direct_descendants_only=ou_direct_descendants_only,
keyword=keyword,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'alphabetical',
    sort_order: str | Unset = 'ASC',
    status: GetCloudPulseAccountDataStatus | Unset = UNSET,
    account_ids: str | Unset = UNSET,
    account_ids_exclusive: bool | Unset = UNSET,
    cft_ids: str | Unset = UNSET,
    cft_ids_exclusive: bool | Unset = UNSET,
    cloud_rule_ids: str | Unset = UNSET,
    cloud_rule_ids_exclusive: bool | Unset = UNSET,
    project_ids: str | Unset = UNSET,
    project_ids_exclusive: bool | Unset = UNSET,
    ou_ids: str | Unset = UNSET,
    ou_ids_exclusive: bool | Unset = UNSET,
    ou_direct_descendants_only: bool | Unset = UNSET,
    keyword: str | Unset = UNSET,

) -> GetCloudPulseAccountDataResponse200 | GetCloudPulseAccountDataResponse400 | GetCloudPulseAccountDataResponse401 | GetCloudPulseAccountDataResponse403 | GetCloudPulseAccountDataResponse500 | None:
    """ Returns account data related to CloudFormation templates in the application.

    Args:
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        sort_method (str | Unset):  Default: 'alphabetical'.
        sort_order (str | Unset):  Default: 'ASC'.
        status (GetCloudPulseAccountDataStatus | Unset):
        account_ids (str | Unset):
        account_ids_exclusive (bool | Unset):
        cft_ids (str | Unset):
        cft_ids_exclusive (bool | Unset):
        cloud_rule_ids (str | Unset):
        cloud_rule_ids_exclusive (bool | Unset):
        project_ids (str | Unset):
        project_ids_exclusive (bool | Unset):
        ou_ids (str | Unset):
        ou_ids_exclusive (bool | Unset):
        ou_direct_descendants_only (bool | Unset):
        keyword (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCloudPulseAccountDataResponse200 | GetCloudPulseAccountDataResponse400 | GetCloudPulseAccountDataResponse401 | GetCloudPulseAccountDataResponse403 | GetCloudPulseAccountDataResponse500
     """


    return (await asyncio_detailed(
        client=client,
page=page,
count=count,
sort_method=sort_method,
sort_order=sort_order,
status=status,
account_ids=account_ids,
account_ids_exclusive=account_ids_exclusive,
cft_ids=cft_ids,
cft_ids_exclusive=cft_ids_exclusive,
cloud_rule_ids=cloud_rule_ids,
cloud_rule_ids_exclusive=cloud_rule_ids_exclusive,
project_ids=project_ids,
project_ids_exclusive=project_ids_exclusive,
ou_ids=ou_ids,
ou_ids_exclusive=ou_ids_exclusive,
ou_direct_descendants_only=ou_direct_descendants_only,
keyword=keyword,

    )).parsed
