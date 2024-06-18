# CookieClickerBot

CookieClickerBot is a Python script that automates the clicking of the big cookie and purchasing of products in the Cookie Clicker game to maximize cookies per second (CPS). The script uses Selenium for browser automation and multithreading to handle clicking and purchasing concurrently.

## Overview

This bot performs the following actions:
- Continuously clicks the big cookie to generate cookies.
- Periodically checks for available products to purchase.
- Purchases the most expensive available product to maximize the CPS.

## Setup

### Prerequisites

- Python 3.x
- Google Chrome
- ChromeDriver

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/cookieclickerbot.git
    cd cookieclickerbot
    ```

2. Install the required Python packages:
    ```bash
    pip install selenium
    ```

3. Ensure `chromedriver` is installed and available in your PATH. You can download it from [here](https://sites.google.com/chromium.org/driver/).

## Usage

1. Update the URL in the script if necessary:
    ```python
    url = "https://orteil.dashnet.org/cookieclicker/"
    ```

2. Run the script:
    ```bash
    python cookieclickerbot.py
    ```

The bot will start clicking the big cookie and purchasing products to maximize the CPS.

## Upcoming Fixes

### Improved Product Purchasing Logic

To further optimize the product purchasing and maximize CPS, the following improvements are planned:
- **Calculate CPS Impact**: Evaluate the impact of each product on the overall CPS before purchasing. Prioritize products that offer the best CPS increase per cookie spent.
- **Golden Cookie Clicks**: Add functionality to detect and click golden cookies, which provide significant bonuses.
- **Upgrade Purchases**: Implement logic to purchase upgrades in addition to products, as upgrades can significantly boost CPS.
- **Product Affordability**: Check the affordability of products more frequently to ensure cookies are spent efficiently without waiting too long for more expensive products.

Stay tuned for these improvements in future releases!

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to discuss any changes or improvements.

