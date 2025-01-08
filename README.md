# Music Moods

## Overview

Music Moods is a Full-Stack project designed to recognize emotions based on a photo of a person and recommend a song to enhance that emotion. The project utilizes React for the frontend, FastAPI for the backend, and PyTorch for the emotion recognition model.

## Technologies Used

- **Frontend**: React
- **Backend**: FastAPI
- **Machine Learning**: PyTorch

## Features

- Upload a photo to detect the emotion of the person.
- Receive a song recommendation based on the detected emotion.
- User-friendly interface for seamless interaction.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/bollitodev/music-moods.git
    cd music-moods
    ```

2. Set up the backend:
    ```bash
    cd music-moods-api
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    uvicorn main:app --reload
    ```

3. Set up the frontend:
    ```bash
    cd frontend
    npm install
    npm start
    ```

## Usage

1. Start the backend server:
    ```bash
    uvicorn main:app --reload
    ```

2. Start the frontend development server:
    ```bash
    npm start
    ```

3. Open your browser and navigate to `http://localhost:3000` to use the application.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
