import os
from dotenv import load_dotenv, set_key
from pathlib import Path
import pyautogui

def get_region():
    """Guide the user to select a region on the screen."""
    print("Please move your mouse to the top-left corner of the region and press Enter.")
    input("Press Enter when ready...")
    x1, y1 = pyautogui.position()
    print(f"Top-left corner recorded at: ({x1}, {y1})")

    print("Now move your mouse to the bottom-right corner of the region and press Enter.")
    input("Press Enter when ready...")
    x2, y2 = pyautogui.position()
    print(f"Bottom-right corner recorded at: ({x2}, {y2})")

    width = x2 - x1
    height = y2 - y1
    return x1, y1, width, height

def validate_image_path(image_path: str) -> str:
    """Check if the provided image path is valid."""
    if os.path.isfile(image_path):
        print(f"Image '{image_path}' found.")
        return image_path
    else:
        raise FileNotFoundError(f"Image '{image_path}' not found. Please ensure the path is correct.")

def write_env(tesseract_path: str, region: tuple, stop_rarities: list, spin_image: str, respin_image: str):
    """Write the configuration to the .env file."""
    env_file = Path('.env')
    load_dotenv(dotenv_path=env_file)

    set_key(dotenv_path=env_file, key_to_set='TESSERACT_PATH', value_to_set=tesseract_path)
    set_key(dotenv_path=env_file, key_to_set='REGION', value_to_set=','.join(map(str, region)))
    set_key(dotenv_path=env_file, key_to_set='STOP_RARITIES', value_to_set=','.join(stop_rarities))
    set_key(dotenv_path=env_file, key_to_set='SPIN_IMAGE_PATH', value_to_set=spin_image)
    set_key(dotenv_path=env_file, key_to_set='RESPIN_IMAGE_PATH', value_to_set=respin_image)

    print("Configuration saved to .env file.")

def main():
    # Setup Tesseract Path
    tesseract_path = input("Enter the full path to your Tesseract executable: ").strip()

    # Setup Region
    print("Let's set up the region to capture from the screen.")
    region = get_region()

    # Get Image Paths
    spin_image_path = validate_image_path(input("Enter the full path to the 'Spin' button image: ").strip())
    respin_image_path = validate_image_path(input("Enter the full path to the 'ReSpin' button image: ").strip())

    # Setup Stop Rarities
    stop_rarities = input("Enter the rarities to stop spinning at, separated by commas (e.g., Legendary,Mythical,Godly): ").strip().split(',')

    # Write to .env
    write_env(tesseract_path, region, stop_rarities, spin_image_path, respin_image_path)

    print("Setup complete. You can now run the main script with the configured settings.")
    input('Press Enter to continue...')

if __name__ == "__main__":
    main()
