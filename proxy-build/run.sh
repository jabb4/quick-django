#!/bin/sh
set -e # Exit immediately if a command exits with a non-zero status.

envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf
nginx -g "daemon off;"