# Tapo Camera Privacy Mode Switch

> Lightweight server that is taking post data and turn on/off camera privacy mode set in environment variable `DYNACONF_CAMERA_ACCOUNTS`

### Accepted Payload

#### Turning on
`true`, `y`, `yes`, `on`

#### Turning off
`false`, `n`, `no`, `off`

### `DYNACONF_CAMERA_ACCOUNTS` Sample

```
@json [{"host":"192.168.1.100","user":"user1","password":"password1"},{"host":"192.168.1.101","user":"user2","password":"password2"}]
```
