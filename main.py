import time
from typing import Tuple, List
import pyautogui
import pytesseract
from PIL import Image
import win32gui
import autoit
from dotenv import load_dotenv
import os

class SpinBot:
    def __init__(self, tesseract_path: str, region: Tuple[int, int, int, int], stop_rarities: List[str], spin_image: str, respin_image: str):
        # Initialize Tesseract command path and region for screenshot
        pytesseract.pytesseract.tesseract_cmd = tesseract_path
        self.region = region
        self.stop_rarities = stop_rarities
        self.spin_image = spin_image
        self.re_spin_image = respin_image
        self.spin_counts = {
            'spins': 0,
            'commons': 0,
            'rares': 0,
            'legendaries': 0,
            'mythicals': 0,
            'godlys': 0,
            'primordials': 0
        }

    def locate_and_click(self, image_path: str, confidence: float = 0.6) -> None:
        """Locate an image on the screen and click it."""
        try:
            pos2 = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if pos2:
                x, y = pos2.left + pos2.width // 2, pos2.top + pos2.height // 2
                pyautogui.moveTo(x, y)
                autoit.mouse_click('left', int(x), int(y))
        except pyautogui.ImageNotFoundException:
            # Retry if image not found
            time.sleep(10)
            self.locate_and_click(image_path, confidence)

    def process_spin_result(self, text: str) -> None:
        """Process the result text and increment the corresponding spin count."""
        spin_types = {
            'Common': 'commons',
            'Rare': 'rares',
            'Legendary': 'legendaries',
            'Mythical': 'mythicals',
            'Godly': 'godlys'
        }

        # Increment spin count
        self.spin_counts['spins'] += 1

        # Increment specific type count
        if text in spin_types:
            self.spin_counts[spin_types[text]] += 1
        else:
            self.spin_counts['primordials'] += 1

        # Check if the rarity is in the stop list
        if text in self.stop_rarities:
            print(f"Stopping spin as '{text}' was found.")
            self.end_session()

        # If the result is of a high rarity, trigger a re-spin
        if text in {'Legendary', 'Mythical', 'Godly'}:
            self.locate_and_click(self.spin_image)
            time.sleep(0.5)
            self.locate_and_click(self.re_spin_image)

    def run(self) -> None:
        """Main loop to run the spin bot."""
        try:
            while True:
                self.locate_and_click(self.spin_image)

                time.sleep(2.5)
                img = pyautogui.screenshot(region=self.region)

                # Check if the spin animation is running
                if pyautogui.pixelMatchesColor(1906, 1304, (0, 0, 0), tolerance=0.2):
                    print('Animation detected. Waiting...')
                    time.sleep(10)
                    img = pyautogui.screenshot(region=self.region)

                text = pytesseract.image_to_string(img).strip()
                print(f'Got: {repr(text)}')

                self.process_spin_result(text)
        except KeyboardInterrupt:
            self.end_session()

    def end_session(self) -> None:
        """Print the session results and exit."""
        print('Ending Spin-Session:')
        for key, value in self.spin_counts.items():
            print(f'\t{key.capitalize()}: {value}')
        
        input('Press Enter to continue...')
        exit()

if __name__ == "__main__":
    load_dotenv()  # Load variables from .env file

    # Load environment variables
    TESSERACT_PATH = os.getenv('TESSERACT_PATH')
    REGION = tuple(map(int, os.getenv('REGION').split(',')))
    STOP_RARITIES = os.getenv('STOP_RARITIES').split(',')
    SPIN_IMAGE_PATH = os.getenv('SPIN_IMAGE_PATH')
    RESPIN_IMAGE_PATH = os.getenv('RESPIN_IMAGE_PATH')

    spin_bot = SpinBot(TESSERACT_PATH, REGION, STOP_RARITIES, SPIN_IMAGE_PATH, RESPIN_IMAGE_PATH)
    spin_bot.run()
