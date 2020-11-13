## 不携带授权信息访问服务

```shell
curl -v  http://localhost:8081/test 
*   Trying ::1...
* TCP_NODELAY set
* Connected to localhost (::1) port 8081 (#0)
> GET /test HTTP/1.1
> Host: localhost:8081
> User-Agent: curl/7.54.0
> Accept: */*
> 
< HTTP/1.1 401 Unauthorized
< content-length: 69
< content-type: text/plain
< date: Mon, 02 Sep 2019 08:28:54 GMT
< server: envoy
< 
* Connection #0 to host localhost left intact
Need an Authorization Header with a 3 character bearer token! #secure%  


```


## 携带错误的授权信息访问服务

```shell
curl -v -H "Authorization: Bearer foo0"  http://localhost:8081/service
*   Trying ::1...
* TCP_NODELAY set
* Connected to localhost (::1) port 8081 (#0)
> GET /service HTTP/1.1
> Host: localhost:8081
> User-Agent: curl/7.54.0
> Accept: */*
> Authorization: Bearer foo0
> 
< HTTP/1.1 401 Unauthorized
< content-length: 69
< content-type: text/plain
< date: Mon, 02 Sep 2019 08:27:34 GMT
< server: envoy
< 
* Connection #0 to host localhost left intact
Need an Authorization Header with a 3 character bearer token! #secure%   

```

## 携带正常的授权信息访问服务

```shell
curl -v -H "Authorization: Bearer foo"  http://localhost:8081/test   
*   Trying ::1...
* TCP_NODELAY set
* Connected to localhost (::1) port 8081 (#0)
> GET /test HTTP/1.1
> Host: localhost:8081
> User-Agent: curl/7.54.0
> Accept: */*
> Authorization: Bearer foo
> 
< HTTP/1.1 200 OK
< content-type: text/html; charset=utf-8
< content-length: 10
< server: envoy
< date: Mon, 02 Sep 2019 08:27:49 GMT
< x-envoy-upstream-service-time: 19
< 
* Connection #0 to host localhost left intact
172.26.0.3%  

```

