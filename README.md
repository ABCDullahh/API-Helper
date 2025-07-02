# Streamlit API Toolkit

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-FF4B4B.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with Love](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-orange.svg)](https://www.streamlit.io)

This repository contains a collection of two interactive web applications built with Python and Streamlit, designed to help developers and API enthusiasts interact with and understand REST APIs more easily.

1.  **🛰️ API Explorer**: An application for manually sending HTTP requests (GET, POST, PUT, DELETE), similar to a lightweight version of Postman or Insomnia.
2.  **🗺️ OpenAPI/Swagger Viewer**: An application for visualizing API documentation from an `openapi.json` or `swagger.json` file, displaying all available endpoints in a structured manner.

## ✨ Key Features

-   **Two Apps in One Repo**: A tool for manual API testing and a tool for automatic API documentation discovery.
-   **Interactive Web Interface**: Built with Streamlit, providing a modern and responsive user experience without needing to install heavy software.
-   **Authentication Support**: Supports common authentication methods like `Bearer Token`, `Custom Header`, and `Query Parameter`.
-   **OpenAPI/Swagger Spec Visualization**: Automatically parses and displays an endpoint map, parameters, request bodies, and potential responses from an API specification.
-   **Easy Setup**: Simply run with a single Python command, and the application is ready to use in your browser.
-   **100% Open Source**: Free to use, modify, and distribute.

## 🖼️ Application Preview

#### 🛰️ API Explorer (`apichecker.py`)

This app allows you to make requests to any endpoint with a full set of configurations.

*(Recommendation: Replace this image URL with a screenshot of your own application)*


#### 🗺️ OpenAPI/Swagger Viewer (`swagger_app.py`)

Just enter the URL to a `swagger.json` file, and all endpoints will be neatly displayed.

*(Recommendation: Replace this image URL with a screenshot of your own application)*


---

## 🚀 Application Details

### 🛰️ 1. API Explorer (`apichecker.py`)

A lightweight tool for directly testing REST APIs. Think of it as a quick alternative to Postman when you just need to perform simple tests.

**Functionality:**

-   **HTTP Methods**: Supports `GET`, `POST`, `PUT`, and `DELETE`.
-   **URL Configuration**: Separates `Base URL` and `Endpoint` for ease of reuse.
-   **Authentication Management**:
    -   **Bearer Token**: Automatically adds the `Authorization: Bearer <token>` header.
    -   **Custom Header**: Allows you to specify a custom header name (e.g., `x-api-key`).
    -   **Query Parameter**: Adds the API key as a parameter in the URL (e.g., `?api_key=<token>`).
-   **Request Body**: Provides a text area to input a JSON-formatted body for `POST` and `PUT` requests.
-   **Response Display**:
    -   Shows the **Status Code** with appropriate colors (Green for 2xx, Yellow for 4xx, Red for 5xx).
    -   Displays the **Response Body** as pretty-printed JSON or as raw text if it's not JSON.
    -   Shows the **Response Headers** inside a collapsible section.

### 🗺️ 2. OpenAPI/Swagger Viewer (`swagger_app.py`)

This application acts as a modern API documentation reader. Instead of reading a complex JSON file, this app transforms it into an easy-to-navigate interface.

**Functionality:**

-   **Load from URL**: Fetches and parses an `openapi.json` or `swagger.json` file from a given URL.
-   **API Information**: Displays the API's title, version, and general description.
-   **Structured Endpoint Map**:
    -   Lists all available paths and HTTP methods.
    -   Uses a collapsible expander for each endpoint to keep the view clean.
    -   **Color-codes** the HTTP methods (`GET`, `POST`, `PUT`, `DELETE`) for quick identification.
-   **Comprehensive Endpoint Details**:
    -   Shows required **parameters** (in path, query, or header), along with their **Required/Optional** status.
    -   Displays the structure of the **Request Body** for `POST` and `PUT` methods.
    -   Lists possible **Responses** with their status codes and descriptions.

---

## 🛠️ Tech Stack

-   **Python**: The primary programming language.
-   **Streamlit**: The framework for building the interactive web apps.
-   **Requests**: The library for making HTTP requests.

## ⚙️ Installation and Usage

Follow these steps to run the applications on your local machine.

**1. Clone the Repository**

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

**2. Create and Activate a Virtual Environment (Recommended)**

-   **macOS / Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
-   **Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

**3. Install Dependencies**

Create a file named `requirements.txt` with the following content:

```txt
streamlit
requests
```

Then, install all required libraries with this command:

```bash
pip install -r requirements.txt
```

**4. Run the Applications**

You can run each application separately. Open two terminals or run them one at a time.

-   **To run the API Explorer:**
    ```bash
    streamlit run apichecker.py
    ```

-   **To run the OpenAPI/Swagger Viewer:**
    ```bash
    streamlit run swagger_app.py
    ```

The application will automatically open in a new browser tab. To stop the app, go back to your terminal and press `Ctrl+C`.

## 📂 Project Structure

```
.
├── apichecker.py         # Source code for the API Explorer app
├── swagger_app.py        # Source code for the OpenAPI Viewer app
├── requirements.txt      # List of Python dependencies
└── README.md             # The file you are currently reading
```
