# Steps to Clone and Run the Application

This guide walks you through cloning a repository, setting up a virtual environment, installing dependencies, and running a Python-based Streamlit application.

## Step 1: Clone the Repository

1. Open your terminal or command prompt.
2. Run the following command to clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

3. Navigate to the project directory:

   ```bash
   cd <repository-directory>
   ```

   Replace `<repository-directory>` with the name of the cloned project directory.

## Step 2: Set Up the Virtual Environment (Optional but Recommended)

It is a good practice to use a virtual environment to manage dependencies for your project. You can create a virtual environment using `venv`:

1. Create the virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

   - **For Windows:**
     ```bash
     venv\Scripts\activate
     ```

   - **For macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

## Step 3: Install Dependencies

Install the required dependencies using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, you can install the packages manually:

```bash
pip install streamlit Pillow exifread folium streamlit-folium pluscodes
```

## Step 4: Run the Streamlit Application

Once the dependencies are installed, run the Streamlit application with the following command:

```bash
streamlit run <filename>.py
```

Replace `<filename>.py` with the name of your Python file (e.g., `app.py`) that contains the Streamlit code.

## Step 5: Access the App in Your Browser

After running the command, Streamlit will automatically launch the app in your default web browser. You can also access it by navigating to the URL shown in the terminal, typically:

```
http://localhost:8501
```

## Step 6: Use the App

1. **Upload an Image**: Upload an image that contains GPS metadata (images taken by smartphones with location services enabled typically have this data).
2. **View the Image**: The app will display the uploaded image on the page.
3. **Extract GPS Coordinates**: The app will extract the latitude and longitude from the image (if available).
4. **View the Map**: A Folium map will be generated, marking the location based on the extracted GPS data.
5. **Plus Code**: The app will generate a Plus Code based on the coordinates.
6. **Google Maps Link**: A button will generate a Google Maps link for the location.

## Step 7: Stop the Application

To stop the application, go back to the terminal where the app is running and press `Ctrl + C`.

## Example Usage

1. **Upload an image**: Upload an image taken by a GPS-enabled device.
2. **View Coordinates**: The app will extract and display the GPS coordinates.
3. **Map Display**: The location is displayed on an interactive map.
4. **Plus Code**: A Plus Code for the location is generated.
5. **Google Maps Link**: A Google Maps link is generated to view the location.

## Notes

- If the image does not contain GPS metadata, the app will notify the user.
- Supported image formats: `jpg`, `jpeg`, and `png`.

## License

This project is licensed under the MIT License.
