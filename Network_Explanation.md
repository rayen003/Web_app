# Docker Network Configuration

## Network Setup
- **Network Name**: `app_network` (Custom bridge network)
- **Subnet**: `172.20.0.0/16` (Allows 65,536 IP addresses)
- **Gateway**: `172.20.0.1`

## Container IP Assignments
- **Web Service**: `172.20.0.2` (Exposed port: 5000)
- **Database**: `172.20.0.3` (Internal only)

## DNS Resolution
- Containers can use service names instead of IP addresses
- `web` automatically resolves to `172.20.0.2`
- `db` automatically resolves to `172.20.0.3`
- Example: Web service connects to database using hostname `db`

## Security
- Network is isolated from other Docker networks
- Database only accessible within the network
- Web service exposes only necessary port (5000)

## Verification Commands
```bash
# Check network
docker network inspect a3_app_network

# Test connectivity
docker exec a3-web-1 ping db
```
