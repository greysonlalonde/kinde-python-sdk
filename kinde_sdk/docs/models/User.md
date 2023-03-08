# kinde_sdk.model.user.User

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  |

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Unique id of the user in Kinde | [optional]
**email** | str,  | str,  | Default email address of the user in Kinde | [optional]
**last_name** | str,  | str,  | User&#x27;s last name | [optional]
**first_name** | str,  | str,  | User&#x27;s first name | [optional]
**is_suspended** | bool,  | BoolClass,  | Whether the user is currently suspended or not | [optional]
**picture** | str,  | str,  | User&#x27;s profile picture URL | [optional]
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)