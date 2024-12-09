# Appointment Reminder System

## Overview
This **Appointment Reminder System** is a Django-based application designed to send automated SMS reminders to customers about their upcoming appointments. It uses the Vonage API for sending SMS notifications.

## Features
- Automatically sends appointment reminders via SMS.
- Allows admins to cancel appointments, with an SMS notification sent to the client about the cancellation.
- Ensures customers are notified only once for each appointment.
- Includes a Django admin interface for managing appointments.

## Prerequisites
Before running the application, ensure the following tools are installed:
- Python 3.10+
- Django 4.x+
- Virtual environment (`venv`)
- Vonage API account (free trial or paid account)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/AppointmentReminderSystem.git
   cd AppointmentReminderSystem
2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate   # For Linux/Mac
   env\Scripts\activate      # For Windows
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Install the Vonage Python SDK:
   ```bash
   pip install vonage
5. Set up the database:
   ```bash
   python manage.py migrate
6. Add your Vonage API credentials to the .env file (or directly to settings.py):
   ```bash
   VONAGE_API_KEY=your_api_key
   VONAGE_API_SECRET=your_api_secret
7. Run the development server:
   ```bash
   python manage.py

### Example Model Usage
1. Here’s how the `Appointment` model works:
   ```python
   from dashboard.models import Appointment
   
   appointment = Appointment(
      customer_name="Jane Doe",
      phone_number="639123456789",
      appointment_date="2024-12-15 14:00:00"
   )
   appointment.save()  # This will trigger the SMS reminder.

# Appointment Reminder System

## How It Works

### Admin Panel:
1. Navigate to the Django Admin panel http://127.0.0.1:8000

2. Log in with the superuser account.

3. Add a new appointment in the **Appointment** model, specifying:
- **Customer Name**
- **Phone Number** (in the international format, e.g., `639XXXXXXXXX` for the Philippines)
- **Appointment Date and Time**

### SMS Reminder:
1. When an appointment is saved, an SMS reminder is sent to the specified phone number.

2. The message includes:
- The customer's name.
- The appointment date and time.

3. The **`is_notified`** flag ensures that reminders are sent only once for each appointment.

### Appointment Logic:
**Example SMS:**
Hello John Doe, this is a reminder for your appointment on 2024-12-15 14:00:00. Please contact us if you have questions.

## Troubleshooting

### SMS not sending?
1. Verify that your Vonage API credentials in the `.env` file are correct.
2. Ensure the phone number is in the correct format (e.g., `639XXXXXXXXX`).
3. Check your Vonage account balance or trial limits.

### SMS error messages:
- Review the logs in your console for specific error details.

### Appointment not updating:
- Ensure the **`is_notified`** flag is reset if you want to resend the reminder.

## License
This project is for educational purposes and is not licensed for commercial use.

