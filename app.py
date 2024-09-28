import streamlit as st
from PIL import Image
import exifread
import folium
from streamlit_folium import st_folium
import pluscodes
from pluscodes import PlusCode, Area, Point , openlocationcode


# Helper function to convert GPS coordinates from DMS to Decimal format
def dms_to_decimal(dms, ref):
    """Convert degrees, minutes, seconds (DMS) to decimal format."""
    degrees = dms[0].num / dms[0].den
    minutes = dms[1].num / dms[1].den
    seconds = dms[2].num / dms[2].den

    decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
    if ref == 'S' or ref == 'W':
        decimal = -decimal
    return decimal

def get_gps_from_exif(image_path):
    """Extract GPS data from an image's EXIF metadata."""
    with open(image_path, 'rb') as img_file:
        tags = exifread.process_file(img_file)

    gps_latitude = tags.get('GPS GPSLatitude')
    gps_latitude_ref = tags.get('GPS GPSLatitudeRef')
    gps_longitude = tags.get('GPS GPSLongitude')
    gps_longitude_ref = tags.get('GPS GPSLongitudeRef')

    if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
        lat = dms_to_decimal(gps_latitude.values, gps_latitude_ref.values)
        lon = dms_to_decimal(gps_longitude.values, gps_longitude_ref.values)
        return lat, lon
    else:
        return None, None

def generate_google_maps_link(lat, lon):
    """Generate a Google Maps link based on the latitude and longitude."""
    return f"https://www.google.com/maps?q={lat},{lon}"

# Streamlit app
st.title("Extract GPS Data from Image and View on Map with Google Maps Link")

# Upload an image
uploaded_file = st.file_uploader("Upload an image with GPS metadata...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Save the uploaded file to a temporary location
    temp_file_path = "temp_image.jpg"
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Extract GPS coordinates from the image's EXIF metadata
    lat, lon = get_gps_from_exif(temp_file_path)



    def generate_plus_code(lat, lon):
        plus = pluscodes.encode(lat, lon)
        return plus
    
    if lat is not None and lon is not None:
        # Display the extracted latitude and longitude
        st.write(f"**Latitude:** {lat}")
        st.write(f"**Longitude:** {lon}")

        # Display the map with a marker at the extracted GPS coordinates
        map_ = folium.Map(location=[lat, lon], zoom_start=12)
        folium.Marker([lat, lon], popup="Extracted Location").add_to(map_)

        # Render the map in Streamlit
        st_folium(map_, width=700, height=500)

        # Button to generate the Google Maps lin
        plus_code = generate_plus_code(lat, lon)
        st.write(f"**Plus Code:** {plus_code}")

        if st.button("Generate Google Maps Link"):
            google_maps_link = generate_google_maps_link(lat, lon)

            st.write(f"[View Location on Google Maps]({google_maps_link})")
    else:
        st.write("No GPS information found in the image.")
