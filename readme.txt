# Django Food App with Heroku Deployment 🍔🚀

Welcome to the Django Food App with Heroku Deployment repository! This project showcases the power of Django's ModelSerializer while providing a delightful food experience. With added emojis to enhance user engagement, this app is sure to make your mouth water! 🍔🍟

## Project Overview

This Django app is designed to display various food items and their details. Leveraging Django's ModelSerializer, the app efficiently serializes and presents food data to users. From mouth-watering burgers to crispy fries, this app has it all!

## Features

- 🍔 Delicious Food Items: Browse through a wide range of food items with enticing details.
- 🍟 Food Details: View detailed information about each food item, including ingredients, calories, and price.
- 🥤 Refreshing Beverages: Quench your thirst with refreshing beverage options available in the app.
- 🍕 Emoji Integration: Experience enhanced user engagement with emojis sprinkled throughout the app.

## Setup Instructions

Follow these steps to set up the Django project and deploy it to Heroku:

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   ```

2. **Install Dependencies:**
   Navigate to the project directory and install dependencies:
   ```bash
   cd Django-Food-App-With-Heroku-Deployment
   pip install -r requirements.txt
   ```

3. **Run Migrations:**
   Apply database migrations to set up the initial database schema:
   ```bash
   python manage.py migrate
   ```

4. **Create Superuser:**
   Create a superuser to access the Django admin panel:
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the Development Server:**
   Start the Django development server:
   ```bash
   python manage.py runserver
   ```

6. **Explore the App:**
   Open your web browser and navigate to `http://localhost:8000` to explore the app.

## Heroku Deployment

To deploy the Django app on Heroku, follow these additional steps:

1. **Create a Heroku Account:**
   If you haven't already, sign up for a free account on [Heroku](https://www.heroku.com/).

2. **Install Heroku CLI:**
   Install the Heroku Command Line Interface (CLI) by following the instructions on the [Heroku Dev Center](https://devcenter.heroku.com/articles/heroku-cli).

3. **Login to Heroku:**
   Log in to your Heroku account using the CLI:
   ```bash
   heroku login
   ```

4. **Initialize a Git Repository:**
   Initialize a Git repository if you haven't already:
   ```bash
   git init
   ```

5. **Create a Heroku App:**
   Create a new Heroku app:
   ```bash
   heroku create
   ```

6. **Deploy to Heroku:**
   Deploy the code to Heroku:
   ```bash
   git push heroku master
   ```

7. **Run Migrations on Heroku:**
   Run database migrations on the deployed Heroku app:
   ```bash
   heroku run python manage.py migrate
   ```

8. **Create a Superuser on Heroku:**
   Create a superuser on the deployed Heroku app:
   ```bash
   heroku run python manage.py createsuperuser
   ```

9. **Open the App:**
   Open the deployed app in your browser:
   ```bash
   heroku open
   ```

## 🍔🍟 Enjoy Your Meal!

Congratulations! You now have a mouth-watering Django Food App deployed on Heroku. Explore the app, indulge in delicious food items, and enjoy the immersive experience enhanced with emojis. Bon appétit! 🥤🍕
