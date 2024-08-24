

---

# FitTrack Pro 🏋️‍♂️

![FitTrack Pro](https://user-images.githubusercontent.com/yourimage.png) <!-- Replace with your image URL -->

**FitTrack Pro** is a comprehensive fitness tracking web application built with Django. It allows users to monitor their workouts, calculate BMI, track calories, and manage their fitness goals. The app is designed to be user-friendly, with a sleek interface powered by Bootstrap, and it includes robust authentication features provided by Django Allauth.

## Features ✨

- **Workout Tracking**: Log your workouts, set goals, and track your progress over time.
- **BMI Calculation**: Instantly calculate your Body Mass Index (BMI) based on your height and weight.
- **Calorie Tracking**: Monitor your daily caloric intake and ensure you stay on track with your diet.
- **User Authentication**: Secure login and registration system powered by Django Allauth.
- **Responsive Design**: A fully responsive design that looks great on both mobile and desktop devices.
- **Secure & Scalable**: Deployed on Render.com with a PostgreSQL database and optimized for performance with Whitenoise.



## Installation & Setup 🚀

1. **Clone the repository**:
    ```bash
    git clone https://github.com/R4255/fittrackpro.git
    cd fittrackpro
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

Now, you can access the app at `http://127.0.0.1:8000/`.



## Technologies Used 🛠️

- **Django**: Backend framework for building robust and scalable web applications.
- **PostgreSQL**: Database management system for storing user data.
- **Bootstrap**: Frontend framework for creating responsive and visually appealing designs.
- **Django Allauth**: Handles authentication, registration, and account management.
- **Whitenoise**: For serving static files efficiently in a production environment.
- **Render.com**: Hosting platform with a secure and scalable environment.

## Contributing 🤝

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License 📜

This project is licensed under the MIT License. 

---



SOME Screenshots of the website 

![image](https://github.com/user-attachments/assets/be9dc8ea-bf2d-49a8-9e0c-cfda91bce3df)

![image](https://github.com/user-attachments/assets/cd77987d-7366-41a4-99e7-e059932a0bce)

![image](https://github.com/user-attachments/assets/099030a4-9c8f-425f-99e0-cf7436ee2bab)


Hosted on Render.com 
live link - https://fitness-tracker-kj78.onrender.com