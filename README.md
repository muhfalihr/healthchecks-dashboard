# Healthchecks Status Dashboard

A standalone dashboard page showing the status of the checks in your Healthchecks server.

## Requirements

1. Install the required Python packages:

    ```sh
    pip install flask
    pip install gunicorn
    ```

## Cloning this repository

```sh
git clone https://github.com/muhfalihr/healthchecks-dashboard.git
cd healthchecks-dashboard
```

## How to Use

1. Create a `certs` and `logs` directory. Then go into the `certs` folder.

    ```sh
    mkdir certs
    mkdir logs
    cd certs
    ```

2. Create self-signed certificates for testing or temporary use.
    
    ```sh
    openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/C=ID/ST=<State-Province>/L=<Locality>/O=<Organization>/CN=<Common-Name>"
    ```

3. Create CSR to send to CA.

    ```sh
    openssl req -new -newkey rsa:2048 -nodes -keyout server.key -out server.csr -subj "/C=ID/ST=<State-Province>/L=<Locality>/O=<Organization>/CN=<Common-Name>"
    ```

4. Create a self-signed CA certificate.
    
    ```sh
    openssl req -new -x509 -days 365 -keyout ca.key -out ca.pem -subj "/C=ID/ST=<State-Province>/L=<Locality>/O=<Organization>/CN=<Common-Name>"
    ```

5. Sign the CSR with a self-signed CA to generate a valid server certificate.

    ```sh
    openssl x509 -req -days 365 -in server.csr -CA ca.pem -CAkey ca.key -CAcreateserial -out server.crt
    ```

6. Go to the previous directory. Edit the file `settings/loal_settingcs.py.example`.

    ```sh
    cd ..
    nano setting/loal_settingcs.py.example
    ```
    Edit it to look like this template.
    ```python
    # TITLE = "Healthchecks.io"
    PROJECTS = [ # Required
        {
            "name": "<Project-Name>",
            "ping_key_read_only": "<Ping-Key-Readonly>"
        }
    ]
    HOST = "<IP-Healthchecks>" # Required
    PORT = "<Port-Healthchecks>" # Required
    ```

7. Rename the file to `local_settings.py`

    ```sh
    mv setting/local_settings.py.example setting/local_settings.py
    ```

8. Run the server using gunicorn.
    ```sh
    gunicorn -b <IP-Host>:<Port> --forwarded-allow-ips <IP-Host> --log-level debug --proxy-allow-from <IP-Host> --keyfile certs/server.key --certfile certs/server.crt --ca-certs certs/ca.pem wsgi:application
    ```
    Runs in the background
    ```sh
    nohup gunicorn -b <IP-Host>:<Port> --forwarded-allow-ips <IP-Host> --log-level debug --proxy-allow-from <IP-Host> --keyfile certs/server.key --certfile certs/server.crt --ca-certs certs/ca.pem wsgi:application > logs/dashboard.log 2>&1 &
    ```

    ****NOTE** : The parameters for running a server using Gunicorn do not have to be the same as above. For more details see :

    ```sh
    gunicorn --help
    ```

9. To activate the dark theme, use this method.
    ```
    https://127.0.0.0:8080/#theme=dark
    ```