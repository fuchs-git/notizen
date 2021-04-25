# jq

## jq piping
```js
.... | jq '.Items[] | "\(.username):\(.password)"'
"{\"s\":\"Mgmt\"}:{\"S\":\"Management@#1@#\"}"
---[snip]...
.... | jq -r'.Items[] | "\(.username[]):\(.password[])"'
Mgmt:Management@#1@#
```