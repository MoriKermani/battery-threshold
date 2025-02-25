import os
import subprocess

def create_service_file(threshold):
    service_content = f"""[Unit]
Description=Set the battery charge threshold
After=multi-user.target

[Service]
Type=oneshot
ExecStart=/bin/bash -c 'echo {threshold} | sudo tee /sys/class/power_supply/BAT0/charge_control_end_threshold'

[Install]
WantedBy=multi-user.target
"""

    service_path = "/etc/systemd/system/battery-charge-threshold.service"

    try:
        # Create the service file directly in the /etc/systemd/system/ directory
        with open(service_path, "w") as f:
            f.write(service_content)

        # Run the necessary commands
        os.system("sudo chmod 644 /etc/systemd/system/battery-charge-threshold.service")
        os.system("sudo systemctl daemon-reload")
        os.system("sudo systemctl enable battery-charge-threshold.service")

        print(f"Service successfully created and enabled with threshold {threshold}%.")
    except Exception as e:
        print(f"Error creating service: {e}")

if __name__ == "__main__":
    # Get the threshold value from the user
    try:
        threshold = int(input("Enter the battery charge threshold (as an integer): "))
        create_service_file(threshold)
    except ValueError:
        print("Please enter a valid integer for the threshold.")

