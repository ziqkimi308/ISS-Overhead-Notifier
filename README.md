# ISS Overhead Notifier via Email

- This project is a Python-based application that tracks the International Space Station's (ISS) location and sends an email notification when the ISS is visible overhead during the night.

---

### Features:

- Fetches the ISS's real-time location using the Open Notify API.
- Determines whether the ISS is overhead based on your location.
- Uses the Sunrise-Sunset API to check if it's nighttime.
- Sends an email notification when both conditions are met.
- Can be set to run continuously at regular intervals.

---

### How It Works:

- The script fetches the current position of the ISS using the Open Notify API:
  - http://api.open-notify.org/iss-now.json
- It checks if the ISS is close to your location (within a range of 5 degrees).
- Simultaneously, it uses the Sunrise-Sunset API to determine if it’s nighttime at your location:
  - https://api.sunrise-sunset.org/json
- If the ISS is overhead and it’s nighttime, the script sends an email notification to the specified recipient.

---
### Screenshots:

<img width="881" alt="image" src="https://github.com/user-attachments/assets/d1ddba82-269b-4993-bcd9-e1dbc5019e90" />

