# Icinga2 Integration Pack

## Description

Icinga2 version 2.4.0 introduced API and since then it was possible to subscribe to Icinga2 events. This pack does exactly that. So far only StateChange event type is supported.
Please, read http://docs.icinga.org/icinga2/latest/doc/module/icinga2/toc#!/icinga2/latest/doc/module/icinga2/chapter/icinga2-api#icinga2-api for more information on Icinga2 API.

## Configuration

`api_state_change_url` - URL to the API stream, e.g. `https://localhost:5665/v1/events?queue=state_change&types=StateChange`
`api_state_change_user` - API user name created on the Icinga2 host, which you are going to connect to, e.g. `root`
`api_state_change_password` - password for the user name mentioned above


