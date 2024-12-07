# Deployment

## get your own instance (Debian 12 here)

### install caddy server
first install standard caddy
```bash
sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https curl
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo apt update
sudo apt install caddy
```
if needed, f.e. for cloudflare support, install xcaddy, which needs a recent version of golang (heads up 1GB+ ram is needed)
```bash
wget https://go.dev/dl/go1.23.2.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.23.2.linux-amd64.tar.gz
```
add the following to your ~/.profile
```
export PATH=$PATH:/usr/local/go/bin
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin
```
now it's time for xcaddy
```bash
sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/xcaddy/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-xcaddy-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/xcaddy/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-xcaddy.list
sudo apt update
sudo apt install xcaddy
```
then build your custom caddy with cf enabled
```bash
xcaddy build --with github.com/caddy-dns/cloudflare
```
make custom caddy the default in systemctl
```bash
sudo dpkg-divert --divert /usr/bin/caddy.default --rename /usr/bin/caddy
sudo mv ./caddy /usr/bin/caddy.custom
sudo update-alternatives --install /usr/bin/caddy caddy /usr/bin/caddy.default 10
sudo update-alternatives --install /usr/bin/caddy caddy /usr/bin/caddy.custom 50
```
### configure caddy with Caddyfile
make sure that your dns record is set

save as `/etc/caddy/Caddyfile`
```json
your.hostname.de {
    tls {
        dns cloudflare your_cf_token
    }
    reverse_proxy localhost:8000
}

:80 {
    redir https://{host}{uri} permanent
}
```

### run
```bash
python src/ots.py
```