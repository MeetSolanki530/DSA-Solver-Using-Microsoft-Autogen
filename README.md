# [DSA Solver Setup Guide](https://meetsolanki530.github.io/DSA-Solver-Using-Microsoft-Autogen/)

Welcome! Here’s how you can get your DSA Solver up and running quickly.

## 1. Install Docker
First, make sure you have Docker installed on your machine. If you don’t have it yet, download it from [Docker’s official site](https://www.docker.com/products/docker-desktop/) and follow the installation steps for your operating system.

## 2. Start Docker
Once Docker is installed, launch Docker Desktop and let it finish starting up. You’ll usually see a little whale icon in your system tray when it’s ready.

## 3. Install Python
Next, you’ll need Python (version 3.8 or above is recommended). If you don’t have Python, grab it from [python.org](https://www.python.org/downloads/). Make sure to check the box to add Python to your PATH during installation.

## 4. Install Project Dependencies
Open a terminal in this folder (`dsa_solver`). Then run:

```
pip install -r requirements.txt
```

This will install all the Python packages you need.

## 5. Add Your Google API Key
To use the LLM features, you’ll need a Google API key. Here’s how to set it up:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/apis/credentials) and sign in with your Google account.
2. Click “Create credentials” and choose “API key.”
3. Copy the API key that’s generated.
4. Open the `.env` file in this folder (`dsa_solver`).
	(The file is already there just paste your API key inside.)
5. Add your Google API key to the file like this:

```
GOOGLE_API_KEY=your-google-api-key-here
```

Save the file. That’s it—your key will be picked up automatically when you run the app.

## 6. Run the Streamlit App
To launch the app, just run:

```
streamlit run app_frontend.py
```

This will open up your browser with the DSA Solver interface. If it doesn’t open automatically, copy the link from the terminal and paste it into your browser.

---

That’s it! You’re all set. If you run into any issues, double-check each step or reach out for help. Enjoy solving DSA problems!

---

If you find this project helpful, don’t forget to star the repo! 
