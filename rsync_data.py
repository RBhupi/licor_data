import subprocess
import argparse
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname=s - %(message)s')

def sync_directories(args):
    """Synchronize the contents of the remote directory to the local directory using rsync."""
    rsync_cmd = f"rsync -avz -e 'sshpass -p {args.passwd} ssh -o StrictHostKeyChecking=no' {args.user}@{args.ip}:{args.licor_dir} {args.local_dir}"
    try:
        subprocess.run(rsync_cmd, shell=True, check=True)
        logging.info(f"Synchronization from {args.licor_dir} to {args.local_dir} completed.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Synchronization failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data Interface for SmartFlux")
    parser.add_argument('--ip', type=str, required=True, help='SmartFlux IP address')
    parser.add_argument('--port', type=int, default=7200, help='TCP connection port (default: 7200)')
    parser.add_argument('--user', type=str, default="licor", help='licor smartflux user id')
    parser.add_argument('--passwd', type=str, default="licor", help='licor smartflux password')
    parser.add_argument('--local_dir', type=str, default="/data/", help='Container directory for saving flux files.')
    parser.add_argument('--licor_dir', type=str, default="/home/licor/data/", help='licor smartflux data directory.')

    args = parser.parse_args()
    sync_directories(args)
